import io
import ast
import json
import base64
import struct
import contextlib
import collections

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

COMMAND_HAS_BODY = (CMD_START_STATE, CMD_START_SUBROUTINE, CMD_IF, CMD_IF_NOT, CMD_ELSE, CMD_UPON)
COMMAND_BODY_END = (CMD_END_STATE, CMD_END_IF, CMD_END_SUBROUTINE, CMD_END_IF_NOT, CMD_END_ELSE, CMD_END_UPON)


class AstNode:
    def __init__(self, has_body=False):
        self.body = [] if has_body else None

    def to_json(self):
        return [node.to_json() for node in self.body]


class ScrNode(AstNode):
    def __init__(self, cmd_name, cmd_id, cmd_args, has_body=False):
        AstNode.__init__(self, has_body)
        self.cmd_name = cmd_name
        self.cmd_args = cmd_args
        self.cmd_id = cmd_id

    def to_json(self):
        cmd_args = list(self.cmd_args)

        for index, arg in enumerate(cmd_args):
            if isinstance(arg, bytes):
                cmd_args[index] = base64.b64encode(arg).decode("UTF-8")

        return {"cmd_name": self.cmd_name, "cmd_id": self.cmd_id,
                "cmd_args": cmd_args, "body": [node.to_json() for node in self.body]}


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
def output_file(ast_output):
    """
    Helper context manager that either wraps `open()` or simply yields an `io.BytesIO`.
    Also provides basic type validation.
    """
    if isinstance(ast_output, str):
        with open(ast_output, "w") as ast_fp:
            yield ast_fp

    elif isinstance(ast_output, io.BytesIO):
        yield ast_output

    else:
        raise TypeError(f"Unsupported output type {ast_output}!")


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


def _parse_tokens(tokens):
    """
    Parse the script tokens into an AST so we can later
    attempt to use the script data, or edit said data, in as human-readable a form as possible.
    """
    root_node = AstNode(has_body=True)

    ast_stack = collections.deque()
    ast_stack.append(root_node.body)

    for command_id, command_info, command_args in tokens:
        fmt = command_info["format"]
        size = command_info["size"]

        if struct.calcsize(fmt) != size:
            raise ValueError(f"Data size mismatch ({command_id}): {fmt} - {size}")

        command_args = _unpack_command_args(fmt, command_args)
        node = ScrNode(command_info["name"], command_id, command_args, has_body=True)

        if command_id in COMMAND_HAS_BODY:
            ast_stack[-1].append(node)
            ast_stack.append(node.body)

        elif command_id in COMMAND_BODY_END:
            ast_stack.pop()

        else:
            ast_stack[-1].append(node)

    return root_node


def parse_script(scr_path, ast_output=None):
    """
    ???.

    Reference: https://github.com/dantarion/bbtools/blob/master/bbcf_bbtag_script_parser.py
    """
    with open(scr_path, "rb") as scr_fp:
        scr_contents = scr_fp.read()

    if ast_output is None:
        ast_output = scr_path.replace(".bin", ".json")

    functions = _parse_header(scr_contents)
    tokens = _parse_script(scr_contents, len(functions))
    root_node = _parse_tokens(tokens)

    with output_file(ast_output) as json_fp:
        json.dump(root_node.to_json(), json_fp, indent=4)
