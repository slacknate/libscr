import io
import ast
import struct
import contextlib
import collections

import astor

from .symbols import *
from .commands import *
from .const import *

ASCII_RANGE = frozenset(list(range(20, 127)) + [0])

SLOT_TYPE_ID = 2

INPUT_CODES = {

    INPUT_RELEASE_A: "INPUT_RELEASE_A",
    INPUT_PRESS_A: "INPUT_PRESS_A",
    INPUT_RELEASE_B: "INPUT_RELEASE_B",
    INPUT_PRESS_B: "INPUT_PRESS_B",
    INPUT_RELEASE_C: "INPUT_RELEASE_C",
    INPUT_PRESS_C: "INPUT_PRESS_C",
    INPUT_RELEASE_D: "INPUT_RELEASE_D",
    INPUT_PRESS_D: "INPUT_PRESS_D",
    INPUT_236: "INPUT_236",
    INPUT_623: "INPUT_623",
    INPUT_214: "INPUT_214",
    INPUT_41236: "INPUT_41236",
    INPUT_63214: "INPUT_63214",
    INPUT_22: "INPUT_22",
    INPUT_2HOLD8: "INPUT_2HOLD8",
    INPUT_236236: "INPUT_236236",
    INPUT_214214: "INPUT_214214",
    INPUT_632146: "INPUT_632146",
}

INPUT_NORMAL_BUTTON_BYTE = {

    1: "A",
    2: "B",
    3: "C",
    4: "D"  
}

INPUT_NORMAL_DIRECTION_BYTE = {

    0: "INPUT_1",
    1: "INPUT_2",
    2: "INPUT_3",
    3: "INPUT_4",
    4: "INPUT_5",
    5: "INPUT_6",
    6: "INPUT_7",
    7: "INPUT_8",
    8: "INPUT_9",
    9: "INPUT_J1",
    10: "INPUT_J2",
    11: "INPUT_J3",
    12: "INPUT_J4",
    13: "INPUT_J5",
    14: "INPUT_J6",
    15: "INPUT_J7",
    16: "INPUT_J8",
    17: "INPUT_J9"
}

MOVE_TYPES = {

    MOVE_TYPE_SPECIAL: "MOVE_TYPE_SPECIAL",
    MOVE_TYPE_DISTORTION: "MOVE_TYPE_DISTORTION",
    MOVE_TYPE_ASTRAL: "MOVE_TYPE_ASTRAL",
    1536: "MOVE_TYPE_UNKNOWN_1536",
    1537: "MOVE_TYPE_UNKNOWN_1537",
    1538: "MOVE_TYPE_UNKNOWN_1538",
    1539: "MOVE_TYPE_UNKNOWN_1539",
    1540: "MOVE_TYPE_UNKNOWN_1540",
    1541: "MOVE_TYPE_UNKNOWN_1541",
}

OPERATOR_CODES = {

    0: ast.Add,
    1: ast.Sub,
    2: ast.Mult,
    3: ast.Div,
    9: ast.Eq,
    10: ast.Gt,
    11: ast.Lt,
    12: ast.GtE,
    13: ast.LtE,
    15: ast.And,  # FIXME: this is def wrong
    16: ast.Or,  # FIXME: this is def wrong
}

SLOTS = {

    0: "RETURN_VAL",
    18: "FRAME_COUNTER",
    47: "IS_IN_OVERDRIVE",
    54: "IS_IN_OVERDRIVE_2",
    91: "IS_PLAYER2",
    106: "IS_IN_OVERDRIVE_3",
    112: "IS_UNLIMITED_CHARACTER"
}

UPON = {

    0: "immediate",
    1: "state_end",
    2: "landing",
    3: "clear_or_exit",
    10: "on_hit_or_block",
}


def is_ascii_str(bytes_value):
    """
    Helper to determine if a bytestring contains human readable text.
    """
    non_ascii_bytes = set(bytes_value) - ASCII_RANGE
    return not non_ascii_bytes


def bytes_to_str(bytes_value):
    """
    Helper to strip off NULL characters for bytestrings that are names and return the decoded string.
    """
    return bytes_value.strip(b"\x00").decode("ascii")


@contextlib.contextmanager
def output_script(py_output):
    """
    Helper context manager that either wraps `open()` or simply yields an `io.BytesIO`.
    Also provides basic type validation.
    """
    if isinstance(py_output, str):
        with open(py_output, "w") as hpl_fp:
            yield hpl_fp

    elif isinstance(py_output, io.BytesIO):
        yield py_output

    else:
        raise TypeError(f"Unsupported output script type {py_output}!")


def make_func_call(name, args, statement: bool, aio: bool):
    """
    Apparently ast.Expr and ast.Expression are used for different things.
    We use ast.Expr for an expressiong statement, and ast.Expression for other
    expressions, like the condition of an `if` statement.
    The ast.Call class exists but its an ast.expr which is something else?
    And it doesn't seem to work right with astor? Why is this is so weird??
    """
    expr_str = f"{name}({', '.join(args)})"
    if aio:
        expr_str = "await " + expr_str

    expression_value = ast.Name(id=expr_str)
    expr_cls = ast.Expr if statement else ast.Expression
    return expr_cls(expression_value)


def _parse_header(scr_contents):
    """
    Parse the header of the script. The header contains a function count and a number of
    entries defining those functions. It seems like these entries are declarations of some sort,
    perhaps of functions to be exported by the script?
    Additionally, the remaining data after each name appears to be a command id? Not sure, it
    could also be a signature definition. Unsure of what this data is actually for.
    """
    functions = []

    num_functions = struct.unpack_from("<I", scr_contents)[0]
    scr_contents = scr_contents[INT_SIZE:]

    for func_index in range(num_functions):
        offset = (func_index * FUNCTION_ENTRY_LEN)
        entry = scr_contents[offset:offset+FUNCTION_ENTRY_LEN]

        function_name = bytes_to_str(entry[:FUNCTION_NAME_LEN])
        function_data = entry[FUNCTION_NAME_LEN:]

        functions.append((function_name, function_data))

    if len(functions) != num_functions:
        raise ValueError("Function count mismatch!")

    return functions


def _parse_script(scr_contents, num_functions):
    """
    Parse the script into meaningful commands/symbols.
    """
    tokens = []

    script_start = INT_SIZE + (FUNCTION_ENTRY_LEN * num_functions)
    remaining = scr_contents[script_start:]

    while remaining:
        command_id, command_info, command_args, remaining = get_command(remaining)
        tokens.append((command_id, command_info, command_args))

    return tokens


def _unpack_command_args(fmt, command_args):
    """
    To begin the parsing process call `struct.unpack()` on our binary data.
    We automatically attempt to decode bytestrings as ASCII if they contain human readable text.
    """
    command_args = list(struct.unpack(fmt, command_args))

    for i, arg in enumerate(command_args):
        if isinstance(arg, bytes) and is_ascii_str(arg):
            command_args[i] = bytes_to_str(arg)

    return command_args


def _handle_function_def(command_id, command_args):
    """
    Create a function def AST node.
    """
    func_type_cls = ast.AsyncFunctionDef if command_id == 0 else ast.FunctionDef
    func_def = func_type_cls(

        command_args[0],
        ast.arguments([], [], None, None, [], None, []),
        [],
        []
    )
    return func_def


def _handle_if_stmt(command_id, command_args):
    """
    Create a if statement AST node.
    """
    slot_name = SLOTS.get(command_args[1], f"SLOT_UNKNOWN_{command_args[1]}")
    cond_expr = ast.Name(slot_name)

    # Command ID 54 is "If Not" so we invert the boolean result of the condition.
    if command_id in (54,):
        cond_expr = ast.UnaryOp(ast.Not(), cond_expr)

    if_stmt = ast.If(

        cond_expr,
        [],
        []
    )

    return if_stmt


def _handle_binary_op(command_id, command_args):
    """
    Create a binary operator AST node.
    """
    operator_code = command_args[0]
    lval_type = command_args[1]
    lval = command_args[2]
    rval_type = command_args[3]
    rval = command_args[4]

    if lval_type == SLOT_TYPE_ID:
        slot_name = SLOTS.get(lval, f"SLOT_UNKNOWN_{lval}")
        lval = ast.Name(slot_name)
    else:
        lval = ast.Num(lval)

    if rval_type == SLOT_TYPE_ID:
        slot_name = SLOTS.get(rval, f"SLOT_UNKNOWN_{rval}")
        rval = ast.Name(slot_name)
    else:
        rval = ast.Num(rval)

    op_cls = OPERATOR_CODES[operator_code]

    if command_id in (40,):
        op_expr = ast.Expr(ast.Compare(lval, [op_cls()], [rval]))
    elif command_id in (49,):
        op_expr = ast.Assign([lval], ast.BinOp(lval, op_cls(), rval))
    else:
        raise ValueError(f"Unknown binary operator: command ID {command_id}")

    return op_expr


def _handle_assign(command_args):
    """
    Create an assignment expression AST node.
    """
    lval_type = command_args[0]
    lval = command_args[1]
    rval_type = command_args[2]
    rval = command_args[3]

    if lval_type == SLOT_TYPE_ID:
        slot_name = SLOTS.get(lval, f"SLOT_UNKNOWN_{lval}")
        lval = ast.Name(slot_name)
    else:
        lval = ast.Num(lval)

    if rval_type == SLOT_TYPE_ID:
        slot_name = SLOTS.get(rval, f"SLOT_UNKNOWN_{rval}")
        rval = ast.Name(slot_name)
    else:
        rval = ast.Num(rval)

    return ast.Assign([lval], rval)


def _parse_tokens(tokens):
    """
    Parse the script tokens into a Python AST so we can later
    attempt to edit the script in as human-readable a form as possible.
    """
    root_node = ast.Module(body=[ast.ImportFrom("libscr.symbols", [ast.Name("*")], 0)])

    ast_stack = collections.deque()
    ast_stack.append(root_node.body)

    for command_id, command_info, command_args in tokens:
        fmt = command_info["format"]
        size = command_info["size"]

        if struct.calcsize(fmt) != size:
            raise ValueError("Data size mismatch!")

        command_args = _unpack_command_args(fmt, command_args)

        if command_id in (0, 8):
            func_def = _handle_function_def(command_id, command_args)
            ast_stack[-1].append(func_def)
            ast_stack.append(func_def.body)

        elif command_id in (3,):
            args = [repr(arg) for arg in command_args]
            await_stmt = make_func_call(command_info["name"], args, statement=True, aio=True)
            ast_stack[-1].append(await_stmt)

        elif command_id in (4, 54):
            if_stmt = _handle_if_stmt(command_id, command_args)
            ast_stack[-1].append(if_stmt)
            ast_stack.append(if_stmt.body)

        elif command_id in (56,):
            ifnode = ast_stack[-1][-1]
            ast_stack.append(ifnode.orelse)

        elif command_id in (18,):
            args = [repr(arg) for arg in command_args]
            func_call = make_func_call(command_info["name"], args, statement=True, aio=False)
            ast_stack[-1].append(func_call)

        elif command_id in (15,):  # TODO: pretty sure theres more work to be done here...
            upon_type = UPON.get(command_args[0], f"UNKNOWN_UPON_{command_args[0]}")
            func_def = ast.FunctionDef(

                "upon_" + upon_type,
                ast.arguments([], [], None, None, [], None, []),
                [],
                []
            )
            ast_stack[-1].append(func_def)
            ast_stack.append(func_def.body)

        elif command_id in (1, 5, 9, 16, 55, 57):
            node_body = ast_stack.pop()
            # If any node that features an indented code block has an empty body we should populate it with a `pass`.
            if not node_body:
                node_body.append(ast.Pass())

        elif command_id in (40, 49):
            op_expr = _handle_binary_op(command_id, command_args)
            ast_stack[-1].append(op_expr)

        elif command_id in (41,):
            assign_expr = _handle_assign(command_args)
            ast_stack[-1].append(assign_expr)

        elif command_id in (14001,):
            move_name = command_args[0]
            move_data = command_args[1]

            move_data_arg = MOVE_TYPES.get(move_data, None)
            if move_data_arg is None:
                direction_byte = move_data & 0x00FF
                button_byte = (move_data & 0xFF00) >> 8
                move_data_arg = INPUT_NORMAL_DIRECTION_BYTE[direction_byte] + INPUT_NORMAL_BUTTON_BYTE[button_byte]

            args = [repr(move_name), move_data_arg]
            func_call = make_func_call(command_info["name"], args, statement=True, aio=False)
            ast_stack[-1].append(func_call)

        elif command_id in (14012,):
            args = [INPUT_CODES.get(command_args[0], f"INPUT_UNKNOWN_{command_args[0]}")]
            func_call = make_func_call(command_info["name"], args, statement=True, aio=False)
            ast_stack[-1].append(func_call)

        else:
            args = [repr(arg) for arg in command_args]
            func_call = make_func_call(command_info["name"], args, statement=True, aio=False)
            ast_stack[-1].append(func_call)

    return root_node


def parse_script(scr_path, py_output=None):
    """
    ???.

    Reference: https://github.com/dantarion/bbtools/blob/master/bbcf_bbtag_script_parser.py
    """
    with open(scr_path, "rb") as scr_fp:
        scr_contents = scr_fp.read()

    if py_output is None:
        py_output = scr_path.replace(".bin", ".py")

    functions = _parse_header(scr_contents)
    tokens = _parse_script(scr_contents, len(functions))
    root_node = _parse_tokens(tokens)

    source = astor.to_source(root_node)
    with output_script(py_output) as py_fp:
        py_fp.write(source)
