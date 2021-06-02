import struct

from .commands import *
from .const import *


def _parse_header(scr_contents):
    """
    ???.
    """
    functions = {}

    num_functions = struct.unpack_from("<I", scr_contents)[0]
    scr_contents = scr_contents[INT_SIZE:]

    for func_index in range(num_functions):
        offset = (func_index * FUNCTION_ENTRY_LEN)
        entry = scr_contents[offset:offset+FUNCTION_ENTRY_LEN]

        function_name = entry[:FUNCTION_NAME_LEN].strip(b"\x00").decode("UTF-8")
        function_data = entry[FUNCTION_NAME_LEN:]

        functions[function_name] = function_data

    if len(functions) != num_functions:
        raise ValueError("Function count mismatch!")

    return functions


def _parse_script(scr_contents, num_functions):
    """
    ???.
    """
    script_start = INT_SIZE + (FUNCTION_ENTRY_LEN * num_functions)
    remaining = scr_contents[script_start:]

    while remaining:
        command_id, command_data, remaining = get_command(remaining)


def parse_script(scr_path):
    """
    ???.
    Reference: https://github.com/dantarion/bbtools/blob/master/bbcf_bbtag_script_parser.py
    """
    with open(scr_path, "rb") as scr_fp:
        scr_contents = scr_fp.read()

    functions = _parse_header(scr_contents)
    _parse_script(scr_contents, len(functions))
