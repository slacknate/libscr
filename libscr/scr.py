import io
import ast
import struct
import contextlib
import collections

import astor

from .commands import *
from .const import *


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

        function_name = entry[:FUNCTION_NAME_LEN].strip(b"\x00").decode("UTF-8")
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


def _parse_tokens(tokens):
    """
    Parse the script tokens into a Python AST so we can later
    attempt to edit the script in as human-readable a form as possible.
    """
    root_node = ast.Module(body=[])
    ast_stack = collections.deque()
    ast_stack.append(root_node.body)

    for command_id, command_info, command_args in tokens:
        fmt = command_info["format"]
        size = command_info["size"]

        if struct.calcsize(fmt) != size:
            raise ValueError("Data size mismatch!")

        command_args = struct.unpack(fmt, command_args)

        if command_id in (0, 8):
            func_id = "state" if command_id == 0 else "subroutine"
            func_def = ast.FunctionDef(

                command_args[0].strip(b"\x00").decode("UTF-8"),
                ast.arguments([], [], None, None, [], None, []),
                [],
                [ast.Name(id=func_id)]
            )
            ast_stack[-1].append(func_def)
            ast_stack.append(func_def.body)

        elif command_id in (4, 54):  # FIXME - not correctly implemented, also cmd ID 54 is "if not"
            if_statement = ast.If(

                ast.Name(id=str(command_args[1])),
                [],
                []
            )
            ast_stack[-1].append(if_statement)
            ast_stack.append(if_statement.body)

        elif command_id in (56,):
            ifnode = ast_stack[-1][-1]
            ast_stack.append(ifnode.orelse)

        elif command_id in (15,):
            func_def = ast.FunctionDef(

                command_args[0],
                ast.arguments([], [], None, None, [], None, []),
                [],
                []
            )
            ast_stack[-1].append(func_def)
            ast_stack.append(func_def.body)

        elif command_id in (1, 5, 9, 16, 55, 57):
            node_body = ast_stack.pop()

            # If any node that features an indented code block has an empty body we should populate it with a `pass`.
            if command_id in (1, 5, 9, 55) and node_body == []:
                node_body.append(ast.Pass())

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

    with output_script(py_output) as py_fp:
        py_fp.write(astor.to_source(root_node))
