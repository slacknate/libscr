import io
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
MATCH_INIT_SUBROUTINE = "MatchInit"

MOTION_CODES = {

    MOTION_6: "6",
    MOTION_236: "236",
    MOTION_623: "623",
    MOTION_214: "214",
    MOTION_41236: "41236",
    MOTION_63214: "63214",
    MOTION_22: "22",
    MOTION_2HOLD8: "2HOLD8",
    MOTION_236236: "236236",
    MOTION_214214: "214214",
    MOTION_632146: "632146",
}

SPECIAL_CODES = {

    SPECIAL_RELEASE_A: "A",
    SPECIAL_PRESS_A: "A",
    SPECIAL_RELEASE_B: "B",
    SPECIAL_PRESS_B: "B",
    SPECIAL_RELEASE_C: "C",
    SPECIAL_PRESS_C: "C",
    SPECIAL_RELEASE_D: "D",
    SPECIAL_PRESS_D: "D",
}

INPUT_NORMAL_BUTTON_BYTE = {

    1: "A",
    2: "B",
    3: "C",
    4: "D"  
}

INPUT_NORMAL_DIRECTION_BYTE = {

    0: "1",
    1: "2",
    2: "3",
    3: "4",
    4: "5",
    5: "6",
    6: "7",
    7: "8",
    8: "9",
    9: "J1",
    10: "J2",
    11: "J3",
    12: "J4",
    13: "J5",
    14: "J6",
    15: "J7",
    16: "J8",
    17: "J9"
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


def get_normal_input_str(move_value):
    """
    Get a human readable string representation of a normal move input.
    """
    direction_byte = move_value & 0x00FF
    button_byte = (move_value & 0xFF00) >> 8

    direction = INPUT_NORMAL_DIRECTION_BYTE[direction_byte]
    button = INPUT_NORMAL_BUTTON_BYTE[button_byte]

    return direction + button


def get_special_input_str(motion_value, button_value):
    """
    Get a human readable string representation of a special move input.
    This is also used for distortions/astrals.
    """
    motion = MOTION_CODES.get(motion_value, "")
    button = SPECIAL_CODES[button_value]

    return motion + button


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
            # FIXME: parser is sometimes popping out the root node. this is definitely a bug, but
            #        for now as a stop-gap we just re-append the root if the stack is empty.
            if not ast_stack:
                ast_stack.append(root_node.body)

            ast_stack[-1].append(node)
            ast_stack.append(node.body)

        elif command_id in COMMAND_BODY_END:
            ast_stack.pop()

        else:
            ast_stack[-1].append(node)

    return root_node


def parse_script(scr_path, ast_output=None):
    """
    Parse a BlazBlue script file and render the tokens as a JSON document.

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
