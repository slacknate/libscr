__all__ = [

    "get_command",
]

import struct

from .const import *

# Script command information map.
# Reference: https://github.com/dantarion/bbtools/blob/master/static_db/bbcf/commandsDB.json
CMD_MAP = {

    0: {
        
        "size": 32,
        "format": "32s",
        "name": "startState"
    },
    1: {
        
        "size": 0,
        "format": "",
        "name": "endState"
    },
    2: {
        
        "size": 36,
        "format": "32si",
        "name": "sprite"
    },
    3: {
        
        "size": 0,
        "format": "",
        "name": "loopRest"
    },
    4: {
        
        "size": 8,
        "format": "ii",
        "name": "if"
    },
    5: {
        
        "size": 0,
        "format": "",
        "name": "endIf"
    },
    6: {
        
        "size": 4,
        "format": "i",
        "name": "label"
    },
    7: {
        
        "size": 4,
        "format": "i",
        "name": "gotoLabel"
    },
    8: {
        
        "size": 32,
        "format": "32s",
        "name": "startSubroutine"
    },
    9: {
        
        "size": 0,
        "format": "",
        "name": "endSubroutine"
    },
    10: {
        
        "size": 32,
        "format": "32s",
        "name": "callSubroutine"
    },
    11: {
        
        "size": 4,
        "format": "i",
        "name": "sendToLabel"
    },
    12: {
        
        "size": 0,
        "format": "",
        "name": "ExitState"
    },
    13: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    15: {
        
        "size": 4,
        "format": "i",
        "name": "upon"
    },
    16: {
        
        "size": 0,
        "format": "",
        "name": "endUpon"
    },
    17: {
        
        "size": 4,
        "format": "i",
        "name": "clearUponHandler"
    },
    18: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    19: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    20: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    21: {
        
        "size": 32,
        "format": "32s",
        "name": "enterState"
    },
    22: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    24: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    25: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    26: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    28: {
        
        "size": 36,
        "format": "i32s",
        "name": "<unknown>"
    },
    29: {
        
        "size": 8,
        "format": "ii",
        "name": "sendToLabelUpon"
    },
    30: {
        
        "size": 8,
        "format": "ii",
        "name": "loopRelated"
    },
    31: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    32: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    35: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    36: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    38: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    39: {
        
        "size": 12,
        "format": "iii",
        "name": "random_"
    },
    40: {
        
        "size": 20,
        "format": "iiiii",
        "name": "op"
    },
    41: {
        
        "size": 16,
        "format": "iiii",
        "name": "StoreValue"
    },
    42: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    43: {
        
        "size": 4,
        "format": "i",
        "name": "CheckInput"
    },
    44: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    45: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    46: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    47: {
        
        "size": 28,
        "format": "28s",
        "name": "<unknown>"
    },
    48: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    49: {
        
        "size": 20,
        "format": "iiiii",
        "name": "ModifyVar_"
    },
    50: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    51: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    52: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    53: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    54: {
        
        "size": 8,
        "format": "ii",
        "name": "ifNot"
    },
    55: {
        
        "size": 0,
        "format": "",
        "name": "endIfNot"
    },
    56: {
        
        "size": 0,
        "format": "",
        "name": "else"
    },
    57: {
        
        "size": 0,
        "format": "",
        "name": "endElse"
    },
    58: {
        
        "size": 40,
        "format": "32sii",
        "name": "<unknown>"
    },
    59: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    60: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    61: {
        
        "size": 48,
        "format": "12i",
        "name": "<unknown>"
    },
    62: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    63: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    64: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    65: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    66: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    67: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    68: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    69: {
        
        "size": 16,
        "format": "16s",
        "name": "PartnerChar"
    },
    70: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    103: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1002: {
        
        "size": 4,
        "format": "i",
        "name": "teleportRelativeX"
    },
    1003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1004: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1005: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1006: {
        
        "size": 4,
        "format": "i",
        "name": "teleportRelativeY"
    },
    1007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1009: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1010: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1011: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1012: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1013: {
        
        "size": 4,
        "format": "i",
        "name": "physicsXImpulse"
    },
    1014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1016: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1017: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1018: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1020: {
        
        "size": 4,
        "format": "i",
        "name": "physicsYImpulse"
    },
    1021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1022: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1023: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1024: {
        
        "size": 4,
        "format": "i",
        "name": "YAccel"
    },
    1025: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1026: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1027: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1028: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1031: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1032: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1033: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1035: {
        
        "size": 4,
        "format": "i",
        "name": "setGravity"
    },
    1036: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1037: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1038: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1040: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1041: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1042: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1043: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1044: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1047: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1049: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1050: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1051: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1052: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1053: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1054: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1055: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1056: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1058: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1059: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1060: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1061: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1062: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1063: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1064: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1065: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1066: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1067: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1068: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1069: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1070: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1071: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1072: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1073: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1074: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1075: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1076: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1077: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1078: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1079: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1080: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1081: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1082: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1083: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1084: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1085: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    1086: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1087: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1088: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1089: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1090: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1091: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1092: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1093: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1094: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1095: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1096: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1097: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1098: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1099: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1100: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1101: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1102: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1103: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1104: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1105: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1108: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    1109: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1110: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1111: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    1112: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1114: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    1116: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2000: {
        
        "size": 0,
        "format": "",
        "name": "RefreshMultihit"
    },
    2001: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2002: {
        
        "size": 0,
        "format": "",
        "name": "StartMultihit"
    },
    2003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2004: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    2005: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2006: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2007: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2009: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2010: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2011: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2012: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2016: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2017: {
        
        "size": 4,
        "format": "i",
        "name": "EnableCollision"
    },
    2018: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    2019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2022: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2023: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    2034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2035: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2036: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    2037: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2040: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2041: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2042: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2044: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2047: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2049: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2050: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2052: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2053: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2054: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2055: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2056: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2058: {
        
        "size": 4,
        "format": "i",
        "name": "ConsumeSuperMeter"
    },
    2059: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2060: {
        
        "size": 0,
        "format": "",
        "name": "Recovery"
    },
    2061: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2062: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2063: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    2064: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2065: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2066: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2067: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    2068: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2070: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    2071: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    2072: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    2073: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2074: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    2075: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3002: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3016: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3017: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3018: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3025: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3027: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3028: {
        
        "size": 8,
        "format": "ii",
        "name": "ScreenShake"
    },
    3029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3031: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    3032: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    3033: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    3034: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    3035: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    3038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3040: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3041: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3042: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3044: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3047: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3053: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3054: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3055: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3056: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3058: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3059: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3060: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    3061: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3062: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3063: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3064: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3065: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3066: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3067: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    3068: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    3069: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3070: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3071: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3072: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    3073: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    3074: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    3075: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    3076: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3077: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3078: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    3079: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4000: {
        
        "size": 36,
        "format": "36s",
        "name": "GFX_0"
    },
    4001: {
        
        "size": 36,
        "format": "36s",
        "name": "GFX_1"
    },
    4002: {
        
        "size": 32,
        "format": "32s",
        "name": "GFX_2"
    },
    4003: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    4004: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    4006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4014: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    4015: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    4016: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    4017: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    4018: {
        
        "size": 48,
        "format": "48s",
        "name": "<unknown>"
    },
    4019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4021: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    4022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4025: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4045: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    4046: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    4047: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    4048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4049: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4050: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4051: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4052: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    4053: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    4054: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4055: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    4061: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    5000: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    5001: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    5003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    5004: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    5005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    6001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    7000: {
        
        "size": 32,
        "format": "32s",
        "name": "SFX_0"
    },
    7001: {
        
        "size": 16,
        "format": "16s",
        "name": "SFX_1"
    },
    7002: {
        
        "size": 32,
        "format": "32s",
        "name": "SFX_2"
    },
    7003: {
        
        "size": 32,
        "format": "32s",
        "name": "SFX_3"
    },
    7004: {
        
        "size": 16,
        "format": "16s",
        "name": "SFX_4"
    },
    7005: {
        
        "size": 68,
        "format": "i16s16s16s16s",
        "name": "tag_voice"
    },
    7006: {
        
        "size": 80,
        "format": "16s4i4i4i4i",
        "name": "<unknown>"
    },
    7007: {
        
        "size": 80,
        "format": "80s",
        "name": "<unknown>"
    },
    7008: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    7009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    7010: {
        
        "size": 20,
        "format": "i16s",
        "name": "<unknown>"
    },
    7011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    7012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    7013: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    7014: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    7015: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    7500: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    8000: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8001: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    8002: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    8003: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8004: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8005: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8006: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8007: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8008: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    8010: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    8011: {
        
        "size": 12,
        "format": "iii",
        "name": "SFX_FOOTSTEP_"
    },
    9000: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9002: {
        
        "size": 4,
        "format": "i",
        "name": "AttackLevel_"
    },
    9003: {
        
        "size": 4,
        "format": "i",
        "name": "Damage"
    },
    9004: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9007: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    9008: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    9009: {
        
        "size": 84,
        "format": "84s",
        "name": "<unknown>"
    },
    9010: {
        
        "size": 84,
        "format": "84s",
        "name": "<unknown>"
    },
    9011: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    9012: {
        
        "size": 28,
        "format": "28s",
        "name": "<unknown>"
    },
    9013: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    9015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9016: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9017: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9018: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9070: {
        
        "size": 4,
        "format": "i",
        "name": "AirPushbackX"
    },
    9071: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9072: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9073: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9082: {
        
        "size": 4,
        "format": "i",
        "name": "AirPushbackY"
    },
    9083: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9084: {
        
        "size": 4,
        "format": "i",
        "name": "CounterHitAirPushbackY"
    },
    9085: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9094: {
        
        "size": 4,
        "format": "i",
        "name": "YImpluseBeforeWallbounce"
    },
    9095: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9096: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9097: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9106: {
        
        "size": 4,
        "format": "i",
        "name": "WallbounceReboundTime"
    },
    9107: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9108: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9109: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9118: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9119: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9120: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9121: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9130: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9131: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9132: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9133: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9142: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9143: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9144: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9145: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9154: {
        
        "size": 4,
        "format": "i",
        "name": "hitstun"
    },
    9155: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9156: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9157: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9166: {
        
        "size": 4,
        "format": "i",
        "name": "AirUntechableTime"
    },
    9167: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9168: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9169: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9170: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9178: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9179: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9180: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9181: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9190: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9191: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9192: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9193: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9202: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9203: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9204: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9205: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9214: {
        
        "size": 4,
        "format": "i",
        "name": "PushbackX"
    },
    9215: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9216: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9217: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9218: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9219: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9238: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9239: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9240: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9241: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9250: {
        
        "size": 4,
        "format": "i",
        "name": "FreezeCount"
    },
    9251: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9252: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9253: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9262: {
        
        "size": 4,
        "format": "i",
        "name": "FreezeDuration"
    },
    9263: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9264: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9265: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9266: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9274: {
        
        "size": 4,
        "format": "i",
        "name": "AttackP1"
    },
    9275: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9276: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9277: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9286: {
        
        "size": 4,
        "format": "i",
        "name": "AttackP2"
    },
    9287: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9288: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9289: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9310: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9311: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9312: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9313: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9322: {
        
        "size": 4,
        "format": "i",
        "name": "GroundedHitstunAnimation"
    },
    9323: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9324: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9325: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9334: {
        
        "size": 4,
        "format": "i",
        "name": "AirHitstunAnimation"
    },
    9335: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9336: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9337: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9346: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9347: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9348: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9349: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9358: {
        
        "size": 4,
        "format": "i",
        "name": "AirHitstunAfterWallbounce"
    },
    9359: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9360: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9361: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    9362: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9363: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9364: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9365: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    9366: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    10000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    10001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11000: {
        
        "size": 4,
        "format": "i",
        "name": "Hitstop"
    },
    11001: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    11002: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11025: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11028: {
        
        "size": 4,
        "format": "i",
        "name": "blockstun"
    },
    11029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11031: {
        
        "size": 4,
        "format": "i",
        "name": "ChipDamagePct"
    },
    11032: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    11033: {
        
        "size": 4,
        "format": "i",
        "name": "ProjectileDurabilityLvl"
    },
    11034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11035: {
        
        "size": 4,
        "format": "i",
        "name": "HitLow"
    },
    11036: {
        
        "size": 4,
        "format": "i",
        "name": "HitOverhead"
    },
    11037: {
        
        "size": 4,
        "format": "i",
        "name": "HitAirUnblockable"
    },
    11038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11040: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11042: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11044: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11047: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    11048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11049: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11050: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    11051: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    11052: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11053: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11054: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11055: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11056: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11058: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    11059: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11060: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11061: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11062: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11063: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11064: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11065: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11066: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11067: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11068: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11069: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    11070: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11071: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11072: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    11073: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11074: {
        
        "size": 28,
        "format": "28s",
        "name": "<unknown>"
    },
    11075: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    11076: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11077: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11078: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11079: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11080: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11081: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11082: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11083: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11084: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11085: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11086: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11087: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    11088: {
        
        "size": 4,
        "format": "i",
        "name": "FatalCounter"
    },
    11089: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11090: {
        
        "size": 4,
        "format": "i",
        "name": "BonusProrationPct"
    },
    11091: {
        
        "size": 4,
        "format": "i",
        "name": "MinimumDamagePct"
    },
    11092: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11093: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11094: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11095: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11096: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    11097: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    11098: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    11099: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11100: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11101: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11102: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11103: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    11104: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11105: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11106: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11107: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    11108: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    11109: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    11110: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12000: {
        
        "size": 4,
        "format": "i",
        "name": "WalkFSpeed"
    },
    12001: {
        
        "size": 4,
        "format": "i",
        "name": "WalkBSpeed"
    },
    12002: {
        
        "size": 4,
        "format": "i",
        "name": "DashFInitialVelocity"
    },
    12003: {
        
        "size": 4,
        "format": "i",
        "name": "DashFAccel"
    },
    12004: {
        
        "size": 4,
        "format": "i",
        "name": "DashFMaxVelocity"
    },
    12005: {
        
        "size": 4,
        "format": "i",
        "name": "JumpYVelocity"
    },
    12006: {
        
        "size": 4,
        "format": "i",
        "name": "SuperJumpYVelocity"
    },
    12007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12012: {
        
        "size": 4,
        "format": "i",
        "name": "DoubleJumpCount"
    },
    12013: {
        
        "size": 4,
        "format": "i",
        "name": "AirDashCount"
    },
    12014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12015: {
        
        "size": 4,
        "format": "i",
        "name": "Health"
    },
    12016: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    12017: {
        
        "size": 4,
        "format": "i",
        "name": "ComboRate"
    },
    12018: {
        
        "size": 36,
        "format": "i32s",
        "name": "<unknown>"
    },
    12019: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    12020: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    12021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12025: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12027: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12028: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12031: {
        
        "size": 4,
        "format": "i",
        "name": "JumpStartup"
    },
    12032: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    12033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12035: {
        
        "size": 4,
        "format": "i",
        "name": "AirBDashDuration"
    },
    12036: {
        
        "size": 4,
        "format": "i",
        "name": "SuperFreezeDuration"
    },
    12037: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12039: {
        
        "size": 4,
        "format": "i",
        "name": "AirDashBSpeed"
    },
    12040: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12041: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    12042: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12044: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12045: {
        
        "size": 64,
        "format": "16i",
        "name": "<unknown>"
    },
    12046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12047: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12049: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12050: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12051: {
        
        "size": 4,
        "format": "i",
        "name": "StarterRating"
    },
    12052: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12053: {
        
        "size": 40,
        "format": "10i",
        "name": "OverdriveDuration"
    },
    12054: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    12055: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12056: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    12057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12058: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    12059: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    12060: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13002: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13016: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13017: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13018: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13027: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13028: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13031: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13032: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13035: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13036: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13037: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13040: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    13041: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    13042: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    13043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13044: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    13054: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14000: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14001: {
        
        "size": 36,
        "format": "32si",
        "name": "Move_Register"
    },
    14002: {
        
        "size": 0,
        "format": "",
        "name": "Move_EndRegister"
    },
    14003: {
        
        "size": 4,
        "format": "i",
        "name": "Move_AirGround_"
    },
    14004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14012: {
        
        "size": 4,
        "format": "i",
        "name": "Move_Input_"
    },
    14013: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14015: {
        
        "size": 24,
        "format": "iiiiii",
        "name": "<unknown>"
    },
    14017: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    14018: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    14019: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14022: {
        
        "size": 4,
        "format": "i",
        "name": "MoveMaxChainRepeat"
    },
    14023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14024: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14025: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14027: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14035: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    14043: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14044: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    14045: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    14046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14047: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14048: {
        
        "size": 40,
        "format": "32sii",
        "name": "<unknown>"
    },
    14049: {
        
        "size": 72,
        "format": "32s32sii",
        "name": "<unknown>"
    },
    14067: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14068: {
        
        "size": 32,
        "format": "32s",
        "name": "WhiffCancel"
    },
    14069: {
        
        "size": 32,
        "format": "32s",
        "name": "HitOrBlockCancel"
    },
    14070: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14071: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14072: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14073: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14074: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14075: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14076: {
        
        "size": 4,
        "format": "i",
        "name": "WhiffCancelEnable"
    },
    14077: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14078: {
        
        "size": 4,
        "format": "i",
        "name": "HitOrBlockJumpCancel"
    },
    14079: {
        
        "size": 4,
        "format": "i",
        "name": "JumpCancel_"
    },
    14080: {
        
        "size": 32,
        "format": "32s",
        "name": "HitCancel"
    },
    14081: {
        
        "size": 4,
        "format": "i",
        "name": "HitJumpCancel"
    },
    14082: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14083: {

        # Reference says this should be size 4 but that does not work for us??
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14084: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14085: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14086: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    14087: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14088: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    14090: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14091: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14092: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14093: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    14094: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    15000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15001: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    15003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    15009: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    15010: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    15011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15015: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    15016: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    15017: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    15018: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15020: {
        
        "size": 16,
        "format": "4i",
        "name": "<unknown>"
    },
    15021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15022: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    15023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    15024: {
        
        "size": 68,
        "format": "32s32si",
        "name": "<unknown>"
    },
    15025: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    15026: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    15027: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    16000: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    16001: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    17000: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_StandingNormal"
    },
    17001: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_AirNormal"
    },
    17002: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_StandingSpecial"
    },
    17003: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17004: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_StandingDD"
    },
    17005: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_AirDD"
    },
    17006: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_CrouchingNormal"
    },
    17007: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17009: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17010: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17011: {
        
        "size": 44,
        "format": "32siii",
        "name": "<unknown>"
    },
    17012: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    17013: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17014: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17015: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17016: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17017: {
        
        "size": 0,
        "format": "",
        "name": "AttackDefaults_Astral"
    },
    17018: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17019: {
        
        "size": 0,
        "format": "",
        "name": "ScriptEndGroundBOunce_"
    },
    17020: {
        
        "size": 0,
        "format": "",
        "name": "ScriptSameAttackComboNoSpecialCancel"
    },
    17021: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17022: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17023: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17024: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    17025: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    18001: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    18003: {
        
        "size": 128,
        "format": "128s",
        "name": "<unknown>"
    },
    18004: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    18005: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    18006: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    18007: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    18008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    18009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    18010: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    18011: {
        
        "size": 144,
        "format": "16s64h",
        "name": "<unknown>"
    },
    19000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19002: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19003: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19004: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    19005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19007: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19008: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19010: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    19011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19012: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19013: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19014: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    19015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    19016: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    20000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20002: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20005: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    20006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20007: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    20010: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    20011: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    21000: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21002: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21003: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    21004: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21006: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    21007: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    21008: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21009: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    21010: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21012: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    21013: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    21014: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    21015: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    22000: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    22001: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22002: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    22003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22004: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    22005: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    22006: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22007: {
        
        "size": 4,
        "format": "i",
        "name": "setInvincible"
    },
    22008: {
        
        "size": 4,
        "format": "i",
        "name": "setInvincibleFor"
    },
    22009: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22019: {
        
        "size": 20,
        "format": "20s",
        "name": "<unknown>"
    },
    22020: {
        
        "size": 4,
        "format": "i",
        "name": "GuardPoint_"
    },
    22021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22023: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22025: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    22026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22027: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22028: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22031: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    22032: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22035: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22036: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22037: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    22500: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23000: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23001: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23002: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23003: {
        
        "size": 32,
        "format": "8i",
        "name": "<unknown>"
    },
    23004: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23005: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23006: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23007: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23008: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23009: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23010: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23011: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23012: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23013: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23014: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23015: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23016: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23017: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23018: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23019: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23020: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23021: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23022: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23023: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23024: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23025: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23026: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23027: {
        
        "size": 0,
        "format": "",
        "name": "DisableAttackRestOfMove"
    },
    23028: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23029: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23030: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    23031: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23032: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23034: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23035: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23036: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23037: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23038: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23039: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23040: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23041: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23042: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23043: {
        
        "size": 12,
        "format": "iii",
        "name": "PhysicsPull"
    },
    23044: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23045: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    23046: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    23047: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    23048: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    23049: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    23050: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    23051: {
        
        "size": 64,
        "format": "64s",
        "name": "<unknown>"
    },
    23052: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    23053: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    23054: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    23055: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23056: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23057: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23058: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23059: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23060: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23066: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23067: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23068: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23069: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23070: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23071: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23072: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23073: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23074: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23075: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23076: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23077: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23078: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23079: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23080: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23081: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23082: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    23083: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23084: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23085: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23086: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23087: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23088: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23089: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23090: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23091: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23093: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23094: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23095: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23096: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23097: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23098: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23099: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23100: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23101: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23102: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23103: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23104: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23105: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23106: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23107: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23108: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23109: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23110: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23111: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23112: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23113: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23114: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23115: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23116: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23117: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23118: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23119: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23120: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23121: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23122: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23123: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23124: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23125: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23126: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23130: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23131: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23132: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23141: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23142: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23143: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    23144: {
        
        "size": 44,
        "format": "44s",
        "name": "<unknown>"
    },
    23145: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23146: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    23147: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23148: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23149: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23150: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23151: {
        
        "size": 8,
        "format": "ii",
        "name": "<unknown>"
    },
    23152: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23153: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23154: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23155: {
        
        "size": 40,
        "format": "40s",
        "name": "<unknown>"
    },
    23156: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23157: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23158: {

        # Reference says this should be size 8 but that does not work for us??
        "size": 12,
        "format": "12s",
        "name": "<unknown>"
    },
    23159: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23160: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23161: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23162: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23163: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23164: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23165: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23166: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23167: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23168: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23169: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23170: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23177: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    23178: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23179: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23180: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23181: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23182: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    23183: {
        
        "size": 44,
        "format": "44s",
        "name": "<unknown>"
    },
    23184: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    23185: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    30000: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30001: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    30002: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    30003: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30004: {
        
        "size": 12,
        "format": "12s",
        "name": "<unknown>"
    },
    30005: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30006: {
        
        "size": 12,
        "format": "iii",
        "name": "<unknown>"
    },
    30007: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30008: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    30009: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30010: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30011: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30012: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30013: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30014: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30015: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30016: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30017: {
        
        "size": 4,
        "format": "4s",
        "name": "<unknown>"
    },
    30018: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30019: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    30020: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30021: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30026: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30027: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30028: {
        
        "size": 4,
        "format": "i",
        "name": "selfDamage"
    },
    30029: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30030: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30031: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30032: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30033: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30034: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30035: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30036: {
        
        "size": 36,
        "format": "36s",
        "name": "<unknown>"
    },
    30037: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30038: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30039: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30040: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30041: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30042: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30043: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30044: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30045: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30046: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30047: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30048: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30049: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    30050: {
        
        "size": 24,
        "format": "24s",
        "name": "<unknown>"
    },
    30051: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30052: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30053: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30054: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30055: {
        
        "size": 12,
        "format": "12s",
        "name": "<unknown>"
    },
    30056: {
        
        "size": 12,
        "format": "12s",
        "name": "<unknown>"
    },
    30057: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30058: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30059: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30060: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    30061: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30062: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30063: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30064: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30065: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30066: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30067: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30068: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30069: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30070: {
        
        "size": 32,
        "format": "32s",
        "name": "<unknown>"
    },
    30071: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30072: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30073: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30074: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30075: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30076: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30077: {
        
        "size": 8,
        "format": "8s",
        "name": "<unknown>"
    },
    30078: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30079: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30080: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30081: {
        
        "size": 0,
        "format": "",
        "name": "<unknown>"
    },
    30082: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30083: {
        
        "size": 16,
        "format": "16s",
        "name": "<unknown>"
    },
    30084: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30085: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30086: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30087: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30088: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30089: {
        
        "size": 4,
        "format": "i",
        "name": "<unknown>"
    },
    30090: {
        
        "size": 32,
        "format": "16s16s",
        "name": "<unknown>"
    },
    30092: {
        
        "size": 32,
        "format": "16s16s",
        "name": "<unknown>"
    },
    30093: {
        
        "size": 20,
        "format": "iiiii",
        "name": "<unknown>"
    }
}


def get_command(scr_data):
    """
    ???.
    """
    command_id = struct.unpack_from("<I", scr_data)[0]
    scr_data = scr_data[INT_SIZE:]

    try:
        command_info = CMD_MAP[command_id]

    except KeyError:
        raise RuntimeError(f"Unknown command ID: {command_id}")

    size = command_info["size"]

    command_args = scr_data[:size]
    scr_data = scr_data[size:]

    return command_id, command_info, command_args, scr_data
