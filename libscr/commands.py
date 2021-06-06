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
        "format": "<32s",
        "name": "startState",
    },
    1: {

        "size": 0,
        "format": "<",
        "name": "endState",
    },
    2: {

        "size": 36,
        "format": "<32si",
        "name": "sprite",
    },
    3: {

        "size": 0,
        "format": "<",
        "name": "yield_control",
    },
    4: {

        "size": 8,
        "format": "<ii",
        "name": "if",
    },
    5: {

        "size": 0,
        "format": "<",
        "name": "endIf",
    },
    6: {

        "size": 4,
        "format": "<i",
        "name": "label",
    },
    7: {

        "size": 4,
        "format": "<i",
        "name": "gotoLabel",
    },
    8: {

        "size": 32,
        "format": "<32s",
        "name": "startSubroutine",
    },
    9: {

        "size": 0,
        "format": "<",
        "name": "endSubroutine",
    },
    10: {

        "size": 32,
        "format": "<32s",
        "name": "callSubroutine",
    },
    11: {

        "size": 4,
        "format": "<i",
        "name": "sendToLabel",
    },
    12: {

        "size": 0,
        "format": "<",
        "name": "ExitState",
    },
    13: {

        "size": 4,
        "format": "<i",
        "name": "command_13",
    },
    14: {

        "size": 0,
        "format": "<",
        "name": "command_14",
    },
    15: {

        "size": 4,
        "format": "<i",
        "name": "upon",
    },
    16: {

        "size": 0,
        "format": "<",
        "name": "endUpon",
    },
    17: {

        "size": 4,
        "format": "<i",
        "name": "clearUponHandler",
    },
    18: {

        "size": 12,
        "format": "<iii",
        "name": "gotolabel_cond",
    },
    19: {

        "size": 12,
        "format": "<iii",
        "name": "command_19",
    },
    20: {

        "size": 12,
        "format": "<iii",
        "name": "command_20",
    },
    21: {

        "size": 32,
        "format": "<32s",
        "name": "enterState",
    },
    22: {

        "size": 32,
        "format": "<32s",
        "name": "command_22",
    },
    23: {

        "size": 64,
        "format": "<64s",
        "name": "command_23",
    },
    24: {

        "size": 36,
        "format": "<36s",
        "name": "command_24",
    },
    25: {

        "size": 36,
        "format": "<36s",
        "name": "command_25",
    },
    26: {

        "size": 32,
        "format": "<32s",
        "name": "command_26",
    },
    28: {

        "size": 36,
        "format": "<i32s",
        "name": "command_28",
    },
    29: {

        "size": 8,
        "format": "<ii",
        "name": "sendToLabelUpon",
    },
    30: {

        "size": 8,
        "format": "<ii",
        "name": "loopRelated",
    },
    31: {

        "size": 8,
        "format": "<ii",
        "name": "command_31",
    },
    32: {

        "size": 16,
        "format": "<16s",
        "name": "command_32",
    },
    35: {

        "size": 0,
        "format": "<",
        "name": "command_35",
    },
    36: {

        "size": 4,
        "format": "<i",
        "name": "command_36",
    },
    38: {

        "size": 8,
        "format": "<ii",
        "name": "command_38",
    },
    39: {

        "size": 12,
        "format": "<iii",
        "name": "random_",
    },
    40: {

        "size": 20,
        "format": "<iiiii",
        "name": "op",
    },
    41: {

        "size": 16,
        "format": "<iiii",
        "name": "StoreValue",
    },
    42: {

        "size": 16,
        "format": "<16s",
        "name": "command_42",
    },
    43: {

        "size": 4,
        "format": "<i",
        "name": "CheckInput",
    },
    44: {

        "size": 4,
        "format": "<i",
        "name": "command_44",
    },
    45: {

        "size": 16,
        "format": "<16s",
        "name": "command_45",
    },
    46: {

        "size": 4,
        "format": "<i",
        "name": "command_46",
    },
    47: {

        "size": 28,
        "format": "<28s",
        "name": "command_47",
    },
    48: {

        "size": 24,
        "format": "<24s",
        "name": "command_48",
    },
    49: {

        "size": 20,
        "format": "<iiiii",
        "name": "ModifyVar_",
    },
    50: {

        "size": 4,
        "format": "<i",
        "name": "command_50",
    },
    51: {

        "size": 4,
        "format": "<i",
        "name": "command_51",
    },
    52: {

        "size": 4,
        "format": "<i",
        "name": "command_52",
    },
    53: {

        "size": 4,
        "format": "<i",
        "name": "command_53",
    },
    54: {

        "size": 8,
        "format": "<ii",
        "name": "ifNot",
    },
    55: {

        "size": 0,
        "format": "<",
        "name": "endIfNot",
    },
    56: {

        "size": 0,
        "format": "<",
        "name": "else",
    },
    57: {

        "size": 0,
        "format": "<",
        "name": "endElse",
    },
    58: {

        "size": 40,
        "format": "<32sii",
        "name": "command_58",
    },
    59: {

        "size": 16,
        "format": "<16s",
        "name": "command_59",
    },
    60: {

        "size": 16,
        "format": "<16s",
        "name": "command_60",
    },
    61: {

        "size": 48,
        "format": "<12i",
        "name": "command_61",
    },
    62: {

        "size": 24,
        "format": "<24s",
        "name": "command_62",
    },
    63: {

        "size": 16,
        "format": "<16s",
        "name": "command_63",
    },
    64: {

        "size": 4,
        "format": "<i",
        "name": "command_64",
    },
    65: {

        "size": 4,
        "format": "<i",
        "name": "command_65",
    },
    66: {

        "size": 24,
        "format": "<24s",
        "name": "command_66",
    },
    67: {

        "size": 20,
        "format": "<20s",
        "name": "command_67",
    },
    68: {

        "size": 20,
        "format": "<20s",
        "name": "command_68",
    },
    69: {

        "size": 16,
        "format": "<16s",
        "name": "PartnerChar",
    },
    70: {

        "size": 64,
        "format": "<64s",
        "name": "command_70",
    },
    103: {

        "size": 8,
        "format": "<ii",
        "name": "command_103",
    },
    1000: {

        "size": 4,
        "format": "<i",
        "name": "command_1000",
    },
    1001: {

        "size": 4,
        "format": "<i",
        "name": "command_1001",
    },
    1002: {

        "size": 4,
        "format": "<i",
        "name": "teleportRelativeX",
    },
    1003: {

        "size": 4,
        "format": "<i",
        "name": "command_1003",
    },
    1004: {

        "size": 0,
        "format": "<",
        "name": "command_1004",
    },
    1005: {

        "size": 0,
        "format": "<",
        "name": "command_1005",
    },
    1006: {

        "size": 4,
        "format": "<i",
        "name": "teleportRelativeY",
    },
    1007: {

        "size": 4,
        "format": "<i",
        "name": "command_1007",
    },
    1008: {

        "size": 0,
        "format": "<",
        "name": "command_1008",
    },
    1009: {

        "size": 0,
        "format": "<",
        "name": "command_1009",
    },
    1010: {

        "size": 8,
        "format": "<ii",
        "name": "command_1010",
    },
    1011: {

        "size": 8,
        "format": "<ii",
        "name": "command_1011",
    },
    1012: {

        "size": 8,
        "format": "<ii",
        "name": "command_1012",
    },
    1013: {

        "size": 4,
        "format": "<i",
        "name": "physicsXImpulse",
    },
    1014: {

        "size": 4,
        "format": "<i",
        "name": "command_1014",
    },
    1015: {

        "size": 4,
        "format": "<i",
        "name": "command_1015",
    },
    1016: {

        "size": 4,
        "format": "<i",
        "name": "command_1016",
    },
    1017: {

        "size": 0,
        "format": "<",
        "name": "command_1017",
    },
    1018: {

        "size": 0,
        "format": "<",
        "name": "command_1018",
    },
    1019: {

        "size": 4,
        "format": "<i",
        "name": "command_1019",
    },
    1020: {

        "size": 4,
        "format": "<i",
        "name": "physicsYImpulse",
    },
    1021: {

        "size": 4,
        "format": "<i",
        "name": "command_1021",
    },
    1022: {

        "size": 0,
        "format": "<",
        "name": "command_1022",
    },
    1023: {

        "size": 0,
        "format": "<",
        "name": "command_1023",
    },
    1024: {

        "size": 4,
        "format": "<i",
        "name": "YAccel",
    },
    1025: {

        "size": 8,
        "format": "<ii",
        "name": "command_1025",
    },
    1026: {

        "size": 8,
        "format": "<ii",
        "name": "command_1026",
    },
    1027: {

        "size": 8,
        "format": "<ii",
        "name": "command_1027",
    },
    1028: {

        "size": 4,
        "format": "<i",
        "name": "command_1028",
    },
    1029: {

        "size": 4,
        "format": "<i",
        "name": "command_1029",
    },
    1030: {

        "size": 4,
        "format": "<i",
        "name": "command_1030",
    },
    1031: {

        "size": 4,
        "format": "<i",
        "name": "command_1031",
    },
    1032: {

        "size": 0,
        "format": "<",
        "name": "command_1032",
    },
    1033: {

        "size": 0,
        "format": "<",
        "name": "command_1033",
    },
    1034: {

        "size": 4,
        "format": "<i",
        "name": "command_1034",
    },
    1035: {

        "size": 4,
        "format": "<i",
        "name": "setGravity",
    },
    1036: {

        "size": 4,
        "format": "<i",
        "name": "command_1036",
    },
    1037: {

        "size": 0,
        "format": "<",
        "name": "command_1037",
    },
    1038: {

        "size": 0,
        "format": "<",
        "name": "command_1038",
    },
    1039: {

        "size": 4,
        "format": "<i",
        "name": "command_1039",
    },
    1040: {

        "size": 8,
        "format": "<ii",
        "name": "command_1040",
    },
    1041: {

        "size": 8,
        "format": "<ii",
        "name": "command_1041",
    },
    1042: {

        "size": 8,
        "format": "<ii",
        "name": "command_1042",
    },
    1043: {

        "size": 0,
        "format": "<",
        "name": "command_1043",
    },
    1044: {

        "size": 0,
        "format": "<",
        "name": "command_1044",
    },
    1045: {

        "size": 4,
        "format": "<i",
        "name": "command_1045",
    },
    1046: {

        "size": 4,
        "format": "<i",
        "name": "command_1046",
    },
    1047: {

        "size": 4,
        "format": "<i",
        "name": "command_1047",
    },
    1048: {

        "size": 4,
        "format": "<i",
        "name": "command_1048",
    },
    1049: {

        "size": 0,
        "format": "<",
        "name": "command_1049",
    },
    1050: {

        "size": 0,
        "format": "<",
        "name": "command_1050",
    },
    1051: {

        "size": 4,
        "format": "<i",
        "name": "command_1051",
    },
    1052: {

        "size": 4,
        "format": "<i",
        "name": "command_1052",
    },
    1053: {

        "size": 8,
        "format": "<ii",
        "name": "command_1053",
    },
    1054: {

        "size": 8,
        "format": "<ii",
        "name": "command_1054",
    },
    1055: {

        "size": 0,
        "format": "<",
        "name": "command_1055",
    },
    1056: {

        "size": 4,
        "format": "<i",
        "name": "command_1056",
    },
    1057: {

        "size": 4,
        "format": "<i",
        "name": "command_1057",
    },
    1058: {

        "size": 4,
        "format": "<i",
        "name": "command_1058",
    },
    1059: {

        "size": 4,
        "format": "<i",
        "name": "command_1059",
    },
    1060: {

        "size": 4,
        "format": "<i",
        "name": "command_1060",
    },
    1061: {

        "size": 4,
        "format": "<i",
        "name": "command_1061",
    },
    1062: {

        "size": 8,
        "format": "<ii",
        "name": "command_1062",
    },
    1063: {

        "size": 8,
        "format": "<ii",
        "name": "command_1063",
    },
    1064: {

        "size": 4,
        "format": "<i",
        "name": "command_1064",
    },
    1065: {

        "size": 4,
        "format": "<i",
        "name": "command_1065",
    },
    1066: {

        "size": 4,
        "format": "<i",
        "name": "command_1066",
    },
    1067: {

        "size": 4,
        "format": "<i",
        "name": "command_1067",
    },
    1068: {

        "size": 4,
        "format": "<i",
        "name": "command_1068",
    },
    1069: {

        "size": 4,
        "format": "<i",
        "name": "command_1069",
    },
    1070: {

        "size": 8,
        "format": "<ii",
        "name": "command_1070",
    },
    1071: {

        "size": 8,
        "format": "<ii",
        "name": "command_1071",
    },
    1072: {

        "size": 4,
        "format": "<i",
        "name": "command_1072",
    },
    1073: {

        "size": 4,
        "format": "<i",
        "name": "command_1073",
    },
    1074: {

        "size": 4,
        "format": "<i",
        "name": "command_1074",
    },
    1075: {

        "size": 4,
        "format": "<i",
        "name": "command_1075",
    },
    1076: {

        "size": 4,
        "format": "<i",
        "name": "command_1076",
    },
    1077: {

        "size": 8,
        "format": "<ii",
        "name": "command_1077",
    },
    1078: {

        "size": 8,
        "format": "<ii",
        "name": "command_1078",
    },
    1079: {

        "size": 0,
        "format": "<",
        "name": "command_1079",
    },
    1080: {

        "size": 4,
        "format": "<i",
        "name": "command_1080",
    },
    1081: {

        "size": 4,
        "format": "<i",
        "name": "command_1081",
    },
    1082: {

        "size": 4,
        "format": "<i",
        "name": "command_1082",
    },
    1083: {

        "size": 4,
        "format": "<i",
        "name": "command_1083",
    },
    1084: {

        "size": 4,
        "format": "<i",
        "name": "command_1084",
    },
    1085: {

        "size": 12,
        "format": "<iii",
        "name": "command_1085",
    },
    1086: {

        "size": 4,
        "format": "<i",
        "name": "command_1086",
    },
    1087: {

        "size": 8,
        "format": "<ii",
        "name": "command_1087",
    },
    1088: {

        "size": 4,
        "format": "<i",
        "name": "command_1088",
    },
    1089: {

        "size": 4,
        "format": "<i",
        "name": "command_1089",
    },
    1090: {

        "size": 4,
        "format": "<i",
        "name": "command_1090",
    },
    1091: {

        "size": 4,
        "format": "<i",
        "name": "command_1091",
    },
    1092: {

        "size": 4,
        "format": "<i",
        "name": "command_1092",
    },
    1093: {

        "size": 4,
        "format": "<i",
        "name": "command_1093",
    },
    1094: {

        "size": 8,
        "format": "<ii",
        "name": "command_1094",
    },
    1095: {

        "size": 8,
        "format": "<ii",
        "name": "command_1095",
    },
    1096: {

        "size": 4,
        "format": "<i",
        "name": "command_1096",
    },
    1097: {

        "size": 4,
        "format": "<i",
        "name": "command_1097",
    },
    1098: {

        "size": 4,
        "format": "<i",
        "name": "command_1098",
    },
    1099: {

        "size": 4,
        "format": "<i",
        "name": "command_1099",
    },
    1100: {

        "size": 4,
        "format": "<i",
        "name": "command_1100",
    },
    1101: {

        "size": 4,
        "format": "<i",
        "name": "command_1101",
    },
    1102: {

        "size": 8,
        "format": "<ii",
        "name": "command_1102",
    },
    1103: {

        "size": 8,
        "format": "<ii",
        "name": "command_1103",
    },
    1104: {

        "size": 4,
        "format": "<i",
        "name": "command_1104",
    },
    1105: {

        "size": 4,
        "format": "<i",
        "name": "command_1105",
    },
    1108: {

        "size": 4,
        "format": "<i",
        "name": "command_1108",
    },
    1109: {

        "size": 8,
        "format": "<ii",
        "name": "command_1109",
    },
    1110: {

        "size": 8,
        "format": "<ii",
        "name": "command_1110",
    },
    1111: {

        "size": 8,
        "format": "<ii",
        "name": "command_1111",
    },
    1112: {

        "size": 0,
        "format": "<",
        "name": "command_1112",
    },
    1114: {

        "size": 0,
        "format": "<",
        "name": "command_1114",
    },
    1116: {

        "size": 0,
        "format": "<",
        "name": "command_1116",
    },
    2000: {

        "size": 0,
        "format": "<",
        "name": "RefreshMultihit",
    },
    2001: {

        "size": 0,
        "format": "<",
        "name": "command_2001",
    },
    2002: {

        "size": 0,
        "format": "<",
        "name": "StartMultihit",
    },
    2003: {

        "size": 4,
        "format": "<i",
        "name": "command_2003",
    },
    2004: {

        "size": 8,
        "format": "<ii",
        "name": "command_2004",
    },
    2005: {

        "size": 0,
        "format": "<",
        "name": "command_2005",
    },
    2006: {

        "size": 0,
        "format": "<",
        "name": "command_2006",
    },
    2007: {

        "size": 0,
        "format": "<",
        "name": "command_2007",
    },
    2008: {

        "size": 0,
        "format": "<",
        "name": "command_2008",
    },
    2009: {

        "size": 0,
        "format": "<",
        "name": "command_2009",
    },
    2010: {

        "size": 0,
        "format": "<",
        "name": "command_2010",
    },
    2011: {

        "size": 0,
        "format": "<",
        "name": "command_2011",
    },
    2012: {

        "size": 0,
        "format": "<",
        "name": "command_2012",
    },
    2013: {

        "size": 4,
        "format": "<i",
        "name": "command_2013",
    },
    2015: {

        "size": 4,
        "format": "<i",
        "name": "command_2015",
    },
    2016: {

        "size": 4,
        "format": "<i",
        "name": "command_2016",
    },
    2017: {

        "size": 4,
        "format": "<i",
        "name": "EnableCollision",
    },
    2018: {

        "size": 8,
        "format": "<ii",
        "name": "command_2018",
    },
    2019: {

        "size": 4,
        "format": "<i",
        "name": "command_2019",
    },
    2020: {

        "size": 4,
        "format": "<i",
        "name": "command_2020",
    },
    2021: {

        "size": 4,
        "format": "<i",
        "name": "command_2021",
    },
    2022: {

        "size": 0,
        "format": "<",
        "name": "command_2022",
    },
    2023: {

        "size": 8,
        "format": "<8s",
        "name": "command_2023",
    },
    2034: {

        "size": 4,
        "format": "<i",
        "name": "command_2034",
    },
    2035: {

        "size": 4,
        "format": "<i",
        "name": "command_2035",
    },
    2036: {

        "size": 12,
        "format": "<iii",
        "name": "command_2036",
    },
    2037: {

        "size": 4,
        "format": "<i",
        "name": "command_2037",
    },
    2038: {

        "size": 4,
        "format": "<i",
        "name": "command_2038",
    },
    2039: {

        "size": 4,
        "format": "<i",
        "name": "command_2039",
    },
    2040: {

        "size": 4,
        "format": "<i",
        "name": "command_2040",
    },
    2041: {

        "size": 4,
        "format": "<i",
        "name": "command_2041",
    },
    2042: {

        "size": 4,
        "format": "<i",
        "name": "command_2042",
    },
    2043: {

        "size": 4,
        "format": "<i",
        "name": "command_2043",
    },
    2044: {

        "size": 4,
        "format": "<i",
        "name": "command_2044",
    },
    2045: {

        "size": 4,
        "format": "<i",
        "name": "command_2045",
    },
    2046: {

        "size": 4,
        "format": "<i",
        "name": "command_2046",
    },
    2047: {

        "size": 4,
        "format": "<i",
        "name": "command_2047",
    },
    2048: {

        "size": 4,
        "format": "<i",
        "name": "command_2048",
    },
    2049: {

        "size": 4,
        "format": "<i",
        "name": "command_2049",
    },
    2050: {

        "size": 4,
        "format": "<i",
        "name": "command_2050",
    },
    2052: {

        "size": 4,
        "format": "<i",
        "name": "command_2052",
    },
    2053: {

        "size": 4,
        "format": "<i",
        "name": "command_2053",
    },
    2054: {

        "size": 4,
        "format": "<i",
        "name": "command_2054",
    },
    2055: {

        "size": 4,
        "format": "<i",
        "name": "command_2055",
    },
    2056: {

        "size": 4,
        "format": "<i",
        "name": "command_2056",
    },
    2057: {

        "size": 4,
        "format": "<i",
        "name": "command_2057",
    },
    2058: {

        "size": 4,
        "format": "<i",
        "name": "ConsumeSuperMeter",
    },
    2059: {

        "size": 4,
        "format": "<i",
        "name": "command_2059",
    },
    2060: {

        "size": 0,
        "format": "<",
        "name": "Recovery",
    },
    2061: {

        "size": 4,
        "format": "<i",
        "name": "command_2061",
    },
    2062: {

        "size": 0,
        "format": "<",
        "name": "command_2062",
    },
    2063: {

        "size": 0,
        "format": "<",
        "name": "command_2063",
    },
    2064: {

        "size": 4,
        "format": "<i",
        "name": "command_2064",
    },
    2065: {

        "size": 4,
        "format": "<i",
        "name": "command_2065",
    },
    2066: {

        "size": 4,
        "format": "<i",
        "name": "command_2066",
    },
    2067: {

        "size": 8,
        "format": "<ii",
        "name": "command_2067",
    },
    2068: {

        "size": 4,
        "format": "<i",
        "name": "command_2068",
    },
    2070: {

        "size": 16,
        "format": "<16s",
        "name": "command_2070",
    },
    2071: {

        "size": 20,
        "format": "<20s",
        "name": "command_2071",
    },
    2072: {

        "size": 20,
        "format": "<20s",
        "name": "command_2072",
    },
    2073: {

        "size": 4,
        "format": "<i",
        "name": "command_2073",
    },
    2074: {

        "size": 4,
        "format": "<i",
        "name": "command_2074",
    },
    2075: {

        "size": 4,
        "format": "<i",
        "name": "command_2075",
    },
    3000: {

        "size": 4,
        "format": "<i",
        "name": "command_3000",
    },
    3001: {

        "size": 4,
        "format": "<i",
        "name": "command_3001",
    },
    3002: {

        "size": 4,
        "format": "<i",
        "name": "command_3002",
    },
    3003: {

        "size": 4,
        "format": "<i",
        "name": "command_3003",
    },
    3004: {

        "size": 4,
        "format": "<i",
        "name": "command_3004",
    },
    3005: {

        "size": 4,
        "format": "<i",
        "name": "command_3005",
    },
    3006: {

        "size": 4,
        "format": "<i",
        "name": "command_3006",
    },
    3007: {

        "size": 4,
        "format": "<i",
        "name": "command_3007",
    },
    3008: {

        "size": 4,
        "format": "<i",
        "name": "command_3008",
    },
    3009: {

        "size": 4,
        "format": "<i",
        "name": "command_3009",
    },
    3010: {

        "size": 4,
        "format": "<i",
        "name": "command_3010",
    },
    3011: {

        "size": 4,
        "format": "<i",
        "name": "command_3011",
    },
    3012: {

        "size": 4,
        "format": "<i",
        "name": "command_3012",
    },
    3013: {

        "size": 4,
        "format": "<i",
        "name": "command_3013",
    },
    3014: {

        "size": 4,
        "format": "<i",
        "name": "command_3014",
    },
    3015: {

        "size": 4,
        "format": "<i",
        "name": "command_3015",
    },
    3016: {

        "size": 4,
        "format": "<i",
        "name": "command_3016",
    },
    3017: {

        "size": 4,
        "format": "<i",
        "name": "command_3017",
    },
    3018: {

        "size": 4,
        "format": "<i",
        "name": "command_3018",
    },
    3019: {

        "size": 4,
        "format": "<i",
        "name": "command_3019",
    },
    3020: {

        "size": 4,
        "format": "<i",
        "name": "command_3020",
    },
    3021: {

        "size": 4,
        "format": "<i",
        "name": "command_3021",
    },
    3022: {

        "size": 4,
        "format": "<i",
        "name": "command_3022",
    },
    3023: {

        "size": 4,
        "format": "<i",
        "name": "command_3023",
    },
    3024: {

        "size": 4,
        "format": "<i",
        "name": "command_3024",
    },
    3025: {

        "size": 8,
        "format": "<ii",
        "name": "command_3025",
    },
    3026: {

        "size": 4,
        "format": "<i",
        "name": "command_3026",
    },
    3027: {

        "size": 4,
        "format": "<i",
        "name": "command_3027",
    },
    3028: {

        "size": 8,
        "format": "<ii",
        "name": "ScreenShake",
    },
    3029: {

        "size": 4,
        "format": "<i",
        "name": "command_3029",
    },
    3030: {

        "size": 4,
        "format": "<i",
        "name": "command_3030",
    },
    3031: {

        "size": 0,
        "format": "<",
        "name": "command_3031",
    },
    3032: {

        "size": 0,
        "format": "<",
        "name": "command_3032",
    },
    3033: {

        "size": 0,
        "format": "<",
        "name": "command_3033",
    },
    3034: {

        "size": 0,
        "format": "<",
        "name": "command_3034",
    },
    3035: {

        "size": 0,
        "format": "<",
        "name": "command_3035",
    },
    3038: {

        "size": 4,
        "format": "<i",
        "name": "command_3038",
    },
    3040: {

        "size": 4,
        "format": "<i",
        "name": "command_3040",
    },
    3041: {

        "size": 4,
        "format": "<i",
        "name": "command_3041",
    },
    3042: {

        "size": 4,
        "format": "<i",
        "name": "command_3042",
    },
    3043: {

        "size": 4,
        "format": "<i",
        "name": "command_3043",
    },
    3044: {

        "size": 4,
        "format": "<i",
        "name": "command_3044",
    },
    3045: {

        "size": 4,
        "format": "<i",
        "name": "command_3045",
    },
    3046: {

        "size": 4,
        "format": "<i",
        "name": "command_3046",
    },
    3047: {

        "size": 4,
        "format": "<i",
        "name": "command_3047",
    },
    3048: {

        "size": 4,
        "format": "<i",
        "name": "command_3048",
    },
    3053: {

        "size": 4,
        "format": "<i",
        "name": "command_3053",
    },
    3054: {

        "size": 8,
        "format": "<ii",
        "name": "command_3054",
    },
    3055: {

        "size": 8,
        "format": "<ii",
        "name": "command_3055",
    },
    3056: {

        "size": 8,
        "format": "<ii",
        "name": "command_3056",
    },
    3057: {

        "size": 4,
        "format": "<i",
        "name": "command_3057",
    },
    3058: {

        "size": 4,
        "format": "<i",
        "name": "command_3058",
    },
    3059: {

        "size": 4,
        "format": "<i",
        "name": "command_3059",
    },
    3060: {

        "size": 36,
        "format": "<36s",
        "name": "command_3060",
    },
    3061: {

        "size": 8,
        "format": "<ii",
        "name": "command_3061",
    },
    3062: {

        "size": 8,
        "format": "<ii",
        "name": "command_3062",
    },
    3063: {

        "size": 8,
        "format": "<ii",
        "name": "command_3063",
    },
    3064: {

        "size": 8,
        "format": "<ii",
        "name": "command_3064",
    },
    3065: {

        "size": 8,
        "format": "<ii",
        "name": "command_3065",
    },
    3066: {

        "size": 8,
        "format": "<ii",
        "name": "command_3066",
    },
    3067: {

        "size": 8,
        "format": "<ii",
        "name": "command_3067",
    },
    3068: {

        "size": 20,
        "format": "<20s",
        "name": "command_3068",
    },
    3069: {

        "size": 4,
        "format": "<i",
        "name": "command_3069",
    },
    3070: {

        "size": 4,
        "format": "<i",
        "name": "command_3070",
    },
    3071: {

        "size": 4,
        "format": "<i",
        "name": "command_3071",
    },
    3072: {

        "size": 16,
        "format": "<16s",
        "name": "command_3072",
    },
    3073: {

        "size": 16,
        "format": "<16s",
        "name": "command_3073",
    },
    3074: {

        "size": 16,
        "format": "<16s",
        "name": "command_3074",
    },
    3075: {

        "size": 16,
        "format": "<16s",
        "name": "command_3075",
    },
    3076: {

        "size": 4,
        "format": "<i",
        "name": "command_3076",
    },
    3077: {

        "size": 4,
        "format": "<i",
        "name": "command_3077",
    },
    3078: {

        "size": 4,
        "format": "<i",
        "name": "command_3078",
    },
    3079: {

        "size": 4,
        "format": "<i",
        "name": "command_3079",
    },
    4000: {

        "size": 36,
        "format": "<36s",
        "name": "GFX_0",
    },
    4001: {

        "size": 36,
        "format": "<36s",
        "name": "GFX_1",
    },
    4002: {

        "size": 32,
        "format": "<32s",
        "name": "GFX_2",
    },
    4003: {

        "size": 64,
        "format": "<64s",
        "name": "command_4003",
    },
    4004: {

        "size": 36,
        "format": "<36s",
        "name": "command_4004",
    },
    4006: {

        "size": 4,
        "format": "<i",
        "name": "command_4006",
    },
    4007: {

        "size": 4,
        "format": "<i",
        "name": "command_4007",
    },
    4008: {

        "size": 4,
        "format": "<i",
        "name": "command_4008",
    },
    4009: {

        "size": 4,
        "format": "<i",
        "name": "command_4009",
    },
    4010: {

        "size": 4,
        "format": "<i",
        "name": "command_4010",
    },
    4011: {

        "size": 4,
        "format": "<i",
        "name": "command_4011",
    },
    4012: {

        "size": 4,
        "format": "<i",
        "name": "command_4012",
    },
    4013: {

        "size": 4,
        "format": "<i",
        "name": "command_4013",
    },
    4014: {

        "size": 32,
        "format": "<32s",
        "name": "command_4014",
    },
    4015: {

        "size": 0,
        "format": "<",
        "name": "command_4015",
    },
    4016: {

        "size": 36,
        "format": "<36s",
        "name": "command_4016",
    },
    4017: {

        "size": 8,
        "format": "<ii",
        "name": "command_4017",
    },
    4018: {

        "size": 48,
        "format": "<48s",
        "name": "command_4018",
    },
    4019: {

        "size": 4,
        "format": "<i",
        "name": "command_4019",
    },
    4020: {

        "size": 4,
        "format": "<i",
        "name": "command_4020",
    },
    4021: {

        "size": 36,
        "format": "<36s",
        "name": "command_4021",
    },
    4022: {

        "size": 4,
        "format": "<i",
        "name": "command_4022",
    },
    4023: {

        "size": 4,
        "format": "<i",
        "name": "command_4023",
    },
    4024: {

        "size": 4,
        "format": "<i",
        "name": "command_4024",
    },
    4025: {

        "size": 4,
        "format": "<i",
        "name": "command_4025",
    },
    4026: {

        "size": 4,
        "format": "<i",
        "name": "command_4026",
    },
    4045: {

        "size": 36,
        "format": "<36s",
        "name": "command_4045",
    },
    4046: {

        "size": 12,
        "format": "<iii",
        "name": "command_4046",
    },
    4047: {

        "size": 12,
        "format": "<iii",
        "name": "command_4047",
    },
    4048: {

        "size": 4,
        "format": "<i",
        "name": "command_4048",
    },
    4049: {

        "size": 4,
        "format": "<i",
        "name": "command_4049",
    },
    4050: {

        "size": 4,
        "format": "<i",
        "name": "command_4050",
    },
    4051: {

        "size": 4,
        "format": "<i",
        "name": "command_4051",
    },
    4052: {

        "size": 0,
        "format": "<",
        "name": "command_4052",
    },
    4053: {

        "size": 8,
        "format": "<ii",
        "name": "command_4053",
    },
    4054: {

        "size": 4,
        "format": "<i",
        "name": "command_4054",
    },
    4055: {

        "size": 4,
        "format": "<i",
        "name": "command_4055",
    },
    4061: {

        "size": 4,
        "format": "<i",
        "name": "command_4061",
    },
    5000: {

        "size": 8,
        "format": "<ii",
        "name": "command_5000",
    },
    5001: {

        "size": 20,
        "format": "<20s",
        "name": "command_5001",
    },
    5003: {

        "size": 4,
        "format": "<i",
        "name": "command_5003",
    },
    5004: {

        "size": 0,
        "format": "<",
        "name": "command_5004",
    },
    5005: {

        "size": 4,
        "format": "<i",
        "name": "command_5005",
    },
    6001: {

        "size": 4,
        "format": "<i",
        "name": "command_6001",
    },
    7000: {

        "size": 32,
        "format": "<32s",
        "name": "SFX_0",
    },
    7001: {

        "size": 16,
        "format": "<16s",
        "name": "SFX_1",
    },
    7002: {

        "size": 32,
        "format": "<32s",
        "name": "SFX_2",
    },
    7003: {

        "size": 32,
        "format": "<32s",
        "name": "SFX_3",
    },
    7004: {

        "size": 16,
        "format": "<16s",
        "name": "SFX_4",
    },
    7005: {

        "size": 68,
        "format": "<i16s16s16s16s",
        "name": "tag_voice",
    },
    7006: {

        "size": 80,
        "format": "<16s4i4i4i4i",
        "name": "command_7006",
    },
    7007: {

        "size": 80,
        "format": "<80s",
        "name": "command_7007",
    },
    7008: {

        "size": 8,
        "format": "<ii",
        "name": "command_7008",
    },
    7009: {

        "size": 4,
        "format": "<i",
        "name": "command_7009",
    },
    7010: {

        "size": 20,
        "format": "<i16s",
        "name": "command_7010",
    },
    7011: {

        "size": 4,
        "format": "<i",
        "name": "command_7011",
    },
    7012: {

        "size": 4,
        "format": "<i",
        "name": "command_7012",
    },
    7013: {

        "size": 8,
        "format": "<ii",
        "name": "command_7013",
    },
    7014: {

        "size": 32,
        "format": "<32s",
        "name": "command_7014",
    },
    7015: {

        "size": 0,
        "format": "<",
        "name": "command_7015",
    },
    7500: {

        "size": 4,
        "format": "<i",
        "name": "command_7500",
    },
    8000: {

        "size": 12,
        "format": "<iii",
        "name": "command_8000",
    },
    8001: {

        "size": 8,
        "format": "<ii",
        "name": "command_8001",
    },
    8002: {

        "size": 0,
        "format": "<",
        "name": "command_8002",
    },
    8003: {

        "size": 12,
        "format": "<iii",
        "name": "command_8003",
    },
    8004: {

        "size": 12,
        "format": "<iii",
        "name": "command_8004",
    },
    8005: {

        "size": 12,
        "format": "<iii",
        "name": "command_8005",
    },
    8006: {

        "size": 12,
        "format": "<iii",
        "name": "command_8006",
    },
    8007: {

        "size": 12,
        "format": "<iii",
        "name": "command_8007",
    },
    8008: {

        "size": 12,
        "format": "<iii",
        "name": "command_8008",
    },
    8009: {

        "size": 4,
        "format": "<i",
        "name": "command_8009",
    },
    8010: {

        "size": 12,
        "format": "<iii",
        "name": "command_8010",
    },
    8011: {

        "size": 12,
        "format": "<iii",
        "name": "SFX_FOOTSTEP_",
    },
    9000: {

        "size": 0,
        "format": "<",
        "name": "command_9000",
    },
    9001: {

        "size": 4,
        "format": "<i",
        "name": "command_9001",
    },
    9002: {

        "size": 4,
        "format": "<i",
        "name": "AttackLevel_",
    },
    9003: {

        "size": 4,
        "format": "<i",
        "name": "Damage",
    },
    9004: {

        "size": 0,
        "format": "<",
        "name": "command_9004",
    },
    9007: {

        "size": 20,
        "format": "<20s",
        "name": "command_9007",
    },
    9008: {

        "size": 20,
        "format": "<20s",
        "name": "command_9008",
    },
    9009: {

        "size": 84,
        "format": "<84s",
        "name": "command_9009",
    },
    9010: {

        "size": 84,
        "format": "<84s",
        "name": "command_9010",
    },
    9011: {

        "size": 40,
        "format": "<40s",
        "name": "command_9011",
    },
    9012: {

        "size": 28,
        "format": "<28s",
        "name": "command_9012",
    },
    9013: {

        "size": 20,
        "format": "<20s",
        "name": "command_9013",
    },
    9015: {

        "size": 4,
        "format": "<i",
        "name": "command_9015",
    },
    9016: {

        "size": 4,
        "format": "<i",
        "name": "command_9016",
    },
    9017: {

        "size": 4,
        "format": "<i",
        "name": "command_9017",
    },
    9018: {

        "size": 4,
        "format": "<i",
        "name": "command_9018",
    },
    9019: {

        "size": 4,
        "format": "<i",
        "name": "command_9019",
    },
    9020: {

        "size": 4,
        "format": "<i",
        "name": "command_9020",
    },
    9021: {

        "size": 4,
        "format": "<i",
        "name": "command_9021",
    },
    9070: {

        "size": 4,
        "format": "<i",
        "name": "AirPushbackX",
    },
    9071: {

        "size": 0,
        "format": "<",
        "name": "command_9071",
    },
    9072: {

        "size": 4,
        "format": "<i",
        "name": "command_9072",
    },
    9073: {

        "size": 0,
        "format": "<",
        "name": "command_9073",
    },
    9082: {

        "size": 4,
        "format": "<i",
        "name": "AirPushbackY",
    },
    9083: {

        "size": 0,
        "format": "<",
        "name": "command_9083",
    },
    9084: {

        "size": 4,
        "format": "<i",
        "name": "CounterHitAirPushbackY",
    },
    9085: {

        "size": 0,
        "format": "<",
        "name": "command_9085",
    },
    9094: {

        "size": 4,
        "format": "<i",
        "name": "YImpluseBeforeWallbounce",
    },
    9095: {

        "size": 0,
        "format": "<",
        "name": "command_9095",
    },
    9096: {

        "size": 4,
        "format": "<i",
        "name": "command_9096",
    },
    9097: {

        "size": 0,
        "format": "<",
        "name": "command_9097",
    },
    9106: {

        "size": 4,
        "format": "<i",
        "name": "WallbounceReboundTime",
    },
    9107: {

        "size": 0,
        "format": "<",
        "name": "command_9107",
    },
    9108: {

        "size": 4,
        "format": "<i",
        "name": "command_9108",
    },
    9109: {

        "size": 0,
        "format": "<",
        "name": "command_9109",
    },
    9118: {

        "size": 4,
        "format": "<i",
        "name": "command_9118",
    },
    9119: {

        "size": 0,
        "format": "<",
        "name": "command_9119",
    },
    9120: {

        "size": 4,
        "format": "<i",
        "name": "command_9120",
    },
    9121: {

        "size": 0,
        "format": "<",
        "name": "command_9121",
    },
    9130: {

        "size": 4,
        "format": "<i",
        "name": "command_9130",
    },
    9131: {

        "size": 0,
        "format": "<",
        "name": "command_9131",
    },
    9132: {

        "size": 4,
        "format": "<i",
        "name": "command_9132",
    },
    9133: {

        "size": 0,
        "format": "<",
        "name": "command_9133",
    },
    9142: {

        "size": 4,
        "format": "<i",
        "name": "command_9142",
    },
    9143: {

        "size": 0,
        "format": "<",
        "name": "command_9143",
    },
    9144: {

        "size": 4,
        "format": "<i",
        "name": "command_9144",
    },
    9145: {

        "size": 0,
        "format": "<",
        "name": "command_9145",
    },
    9154: {

        "size": 4,
        "format": "<i",
        "name": "hitstun",
    },
    9155: {

        "size": 0,
        "format": "<",
        "name": "command_9155",
    },
    9156: {

        "size": 4,
        "format": "<i",
        "name": "command_9156",
    },
    9157: {

        "size": 0,
        "format": "<",
        "name": "command_9157",
    },
    9166: {

        "size": 4,
        "format": "<i",
        "name": "AirUntechableTime",
    },
    9167: {

        "size": 0,
        "format": "<",
        "name": "command_9167",
    },
    9168: {

        "size": 4,
        "format": "<i",
        "name": "command_9168",
    },
    9169: {

        "size": 0,
        "format": "<",
        "name": "command_9169",
    },
    9170: {

        "size": 4,
        "format": "<i",
        "name": "command_9170",
    },
    9178: {

        "size": 4,
        "format": "<i",
        "name": "command_9178",
    },
    9179: {

        "size": 0,
        "format": "<",
        "name": "command_9179",
    },
    9180: {

        "size": 4,
        "format": "<i",
        "name": "command_9180",
    },
    9181: {

        "size": 0,
        "format": "<",
        "name": "command_9181",
    },
    9190: {

        "size": 4,
        "format": "<i",
        "name": "command_9190",
    },
    9191: {

        "size": 0,
        "format": "<",
        "name": "command_9191",
    },
    9192: {

        "size": 4,
        "format": "<i",
        "name": "command_9192",
    },
    9193: {

        "size": 0,
        "format": "<",
        "name": "command_9193",
    },
    9202: {

        "size": 4,
        "format": "<i",
        "name": "command_9202",
    },
    9203: {

        "size": 0,
        "format": "<",
        "name": "command_9203",
    },
    9204: {

        "size": 4,
        "format": "<i",
        "name": "command_9204",
    },
    9205: {

        "size": 0,
        "format": "<",
        "name": "command_9205",
    },
    9214: {

        "size": 4,
        "format": "<i",
        "name": "PushbackX",
    },
    9215: {

        "size": 0,
        "format": "<",
        "name": "command_9215",
    },
    9216: {

        "size": 4,
        "format": "<i",
        "name": "command_9216",
    },
    9217: {

        "size": 0,
        "format": "<",
        "name": "command_9217",
    },
    9218: {

        "size": 4,
        "format": "<i",
        "name": "command_9218",
    },
    9219: {

        "size": 4,
        "format": "<i",
        "name": "command_9219",
    },
    9238: {

        "size": 4,
        "format": "<i",
        "name": "command_9238",
    },
    9239: {

        "size": 0,
        "format": "<",
        "name": "command_9239",
    },
    9240: {

        "size": 4,
        "format": "<i",
        "name": "command_9240",
    },
    9241: {

        "size": 0,
        "format": "<",
        "name": "command_9241",
    },
    9250: {

        "size": 4,
        "format": "<i",
        "name": "FreezeCount",
    },
    9251: {

        "size": 0,
        "format": "<",
        "name": "command_9251",
    },
    9252: {

        "size": 4,
        "format": "<i",
        "name": "command_9252",
    },
    9253: {

        "size": 0,
        "format": "<",
        "name": "command_9253",
    },
    9262: {

        "size": 4,
        "format": "<i",
        "name": "FreezeDuration",
    },
    9263: {

        "size": 0,
        "format": "<",
        "name": "command_9263",
    },
    9264: {

        "size": 4,
        "format": "<i",
        "name": "command_9264",
    },
    9265: {

        "size": 0,
        "format": "<",
        "name": "command_9265",
    },
    9266: {

        "size": 4,
        "format": "<i",
        "name": "command_9266",
    },
    9274: {

        "size": 4,
        "format": "<i",
        "name": "AttackP1",
    },
    9275: {

        "size": 0,
        "format": "<",
        "name": "command_9275",
    },
    9276: {

        "size": 4,
        "format": "<i",
        "name": "command_9276",
    },
    9277: {

        "size": 0,
        "format": "<",
        "name": "command_9277",
    },
    9286: {

        "size": 4,
        "format": "<i",
        "name": "AttackP2",
    },
    9287: {

        "size": 0,
        "format": "<",
        "name": "command_9287",
    },
    9288: {

        "size": 4,
        "format": "<i",
        "name": "command_9288",
    },
    9289: {

        "size": 0,
        "format": "<",
        "name": "command_9289",
    },
    9310: {

        "size": 4,
        "format": "<i",
        "name": "command_9310",
    },
    9311: {

        "size": 0,
        "format": "<",
        "name": "command_9311",
    },
    9312: {

        "size": 4,
        "format": "<i",
        "name": "command_9312",
    },
    9313: {

        "size": 0,
        "format": "<",
        "name": "command_9313",
    },
    9322: {

        "size": 4,
        "format": "<i",
        "name": "GroundedHitstunAnimation",
    },
    9323: {

        "size": 0,
        "format": "<",
        "name": "command_9323",
    },
    9324: {

        "size": 4,
        "format": "<i",
        "name": "command_9324",
    },
    9325: {

        "size": 0,
        "format": "<",
        "name": "command_9325",
    },
    9334: {

        "size": 4,
        "format": "<i",
        "name": "AirHitstunAnimation",
    },
    9335: {

        "size": 0,
        "format": "<",
        "name": "command_9335",
    },
    9336: {

        "size": 4,
        "format": "<i",
        "name": "command_9336",
    },
    9337: {

        "size": 0,
        "format": "<",
        "name": "command_9337",
    },
    9346: {

        "size": 4,
        "format": "<i",
        "name": "command_9346",
    },
    9347: {

        "size": 0,
        "format": "<",
        "name": "command_9347",
    },
    9348: {

        "size": 4,
        "format": "<i",
        "name": "command_9348",
    },
    9349: {

        "size": 0,
        "format": "<",
        "name": "command_9349",
    },
    9358: {

        "size": 4,
        "format": "<i",
        "name": "AirHitstunAfterWallbounce",
    },
    9359: {

        "size": 0,
        "format": "<",
        "name": "command_9359",
    },
    9360: {

        "size": 4,
        "format": "<i",
        "name": "command_9360",
    },
    9361: {

        "size": 0,
        "format": "<",
        "name": "command_9361",
    },
    9362: {

        "size": 4,
        "format": "<i",
        "name": "command_9362",
    },
    9363: {

        "size": 4,
        "format": "<i",
        "name": "command_9363",
    },
    9364: {

        "size": 4,
        "format": "<i",
        "name": "command_9364",
    },
    9365: {

        "size": 4,
        "format": "<i",
        "name": "command_9365",
    },
    9366: {

        "size": 4,
        "format": "<i",
        "name": "command_9366",
    },
    10000: {

        "size": 4,
        "format": "<i",
        "name": "command_10000",
    },
    10001: {

        "size": 4,
        "format": "<i",
        "name": "command_10001",
    },
    11000: {

        "size": 4,
        "format": "<i",
        "name": "Hitstop",
    },
    11001: {

        "size": 12,
        "format": "<iii",
        "name": "command_11001",
    },
    11002: {

        "size": 4,
        "format": "<i",
        "name": "command_11002",
    },
    11023: {

        "size": 4,
        "format": "<i",
        "name": "command_11023",
    },
    11024: {

        "size": 4,
        "format": "<i",
        "name": "command_11024",
    },
    11025: {

        "size": 4,
        "format": "<i",
        "name": "command_11025",
    },
    11026: {

        "size": 4,
        "format": "<i",
        "name": "command_11026",
    },
    11028: {

        "size": 4,
        "format": "<i",
        "name": "blockstun",
    },
    11029: {

        "size": 4,
        "format": "<i",
        "name": "command_11029",
    },
    11030: {

        "size": 4,
        "format": "<i",
        "name": "command_11030",
    },
    11031: {

        "size": 4,
        "format": "<i",
        "name": "ChipDamagePct",
    },
    11032: {

        "size": 16,
        "format": "<16s",
        "name": "command_11032",
    },
    11033: {

        "size": 4,
        "format": "<i",
        "name": "ProjectileDurabilityLvl",
    },
    11034: {

        "size": 4,
        "format": "<i",
        "name": "command_11034",
    },
    11035: {

        "size": 4,
        "format": "<i",
        "name": "HitLow",
    },
    11036: {

        "size": 4,
        "format": "<i",
        "name": "HitOverhead",
    },
    11037: {

        "size": 4,
        "format": "<i",
        "name": "HitAirUnblockable",
    },
    11038: {

        "size": 4,
        "format": "<i",
        "name": "command_11038",
    },
    11039: {

        "size": 4,
        "format": "<i",
        "name": "command_11039",
    },
    11040: {

        "size": 4,
        "format": "<i",
        "name": "command_11040",
    },
    11042: {

        "size": 4,
        "format": "<i",
        "name": "command_11042",
    },
    11043: {

        "size": 4,
        "format": "<i",
        "name": "command_11043",
    },
    11044: {

        "size": 4,
        "format": "<i",
        "name": "command_11044",
    },
    11045: {

        "size": 4,
        "format": "<i",
        "name": "command_11045",
    },
    11046: {

        "size": 4,
        "format": "<i",
        "name": "command_11046",
    },
    11047: {

        "size": 32,
        "format": "<32s",
        "name": "command_11047",
    },
    11048: {

        "size": 4,
        "format": "<i",
        "name": "command_11048",
    },
    11049: {

        "size": 4,
        "format": "<i",
        "name": "command_11049",
    },
    11050: {

        "size": 36,
        "format": "<36s",
        "name": "command_11050",
    },
    11051: {

        "size": 36,
        "format": "<36s",
        "name": "command_11051",
    },
    11052: {

        "size": 4,
        "format": "<i",
        "name": "command_11052",
    },
    11053: {

        "size": 4,
        "format": "<i",
        "name": "command_11053",
    },
    11054: {

        "size": 4,
        "format": "<i",
        "name": "command_11054",
    },
    11055: {

        "size": 4,
        "format": "<i",
        "name": "command_11055",
    },
    11056: {

        "size": 4,
        "format": "<i",
        "name": "command_11056",
    },
    11057: {

        "size": 4,
        "format": "<i",
        "name": "command_11057",
    },
    11058: {

        "size": 20,
        "format": "<20s",
        "name": "command_11058",
    },
    11059: {

        "size": 4,
        "format": "<i",
        "name": "command_11059",
    },
    11060: {

        "size": 4,
        "format": "<i",
        "name": "command_11060",
    },
    11061: {

        "size": 4,
        "format": "<i",
        "name": "command_11061",
    },
    11062: {

        "size": 4,
        "format": "<i",
        "name": "command_11062",
    },
    11063: {

        "size": 4,
        "format": "<i",
        "name": "command_11063",
    },
    11064: {

        "size": 4,
        "format": "<i",
        "name": "command_11064",
    },
    11065: {

        "size": 4,
        "format": "<i",
        "name": "command_11065",
    },
    11066: {

        "size": 4,
        "format": "<i",
        "name": "command_11066",
    },
    11067: {

        "size": 4,
        "format": "<i",
        "name": "command_11067",
    },
    11068: {

        "size": 4,
        "format": "<i",
        "name": "command_11068",
    },
    11069: {

        "size": 32,
        "format": "<32s",
        "name": "command_11069",
    },
    11070: {

        "size": 4,
        "format": "<i",
        "name": "command_11070",
    },
    11071: {

        "size": 4,
        "format": "<i",
        "name": "command_11071",
    },
    11072: {

        "size": 12,
        "format": "<iii",
        "name": "command_11072",
    },
    11073: {

        "size": 4,
        "format": "<i",
        "name": "command_11073",
    },
    11074: {

        "size": 28,
        "format": "<28s",
        "name": "command_11074",
    },
    11075: {

        "size": 8,
        "format": "<ii",
        "name": "command_11075",
    },
    11076: {

        "size": 4,
        "format": "<i",
        "name": "command_11076",
    },
    11077: {

        "size": 4,
        "format": "<i",
        "name": "command_11077",
    },
    11078: {

        "size": 4,
        "format": "<i",
        "name": "command_11078",
    },
    11079: {

        "size": 4,
        "format": "<i",
        "name": "command_11079",
    },
    11080: {

        "size": 4,
        "format": "<i",
        "name": "command_11080",
    },
    11081: {

        "size": 4,
        "format": "<i",
        "name": "command_11081",
    },
    11082: {

        "size": 4,
        "format": "<i",
        "name": "command_11082",
    },
    11083: {

        "size": 4,
        "format": "<i",
        "name": "command_11083",
    },
    11084: {

        "size": 4,
        "format": "<i",
        "name": "command_11084",
    },
    11085: {

        "size": 4,
        "format": "<i",
        "name": "command_11085",
    },
    11086: {

        "size": 4,
        "format": "<i",
        "name": "command_11086",
    },
    11087: {

        "size": 8,
        "format": "<ii",
        "name": "command_11087",
    },
    11088: {

        "size": 4,
        "format": "<i",
        "name": "FatalCounter",
    },
    11089: {

        "size": 4,
        "format": "<i",
        "name": "command_11089",
    },
    11090: {

        "size": 4,
        "format": "<i",
        "name": "BonusProrationPct",
    },
    11091: {

        "size": 4,
        "format": "<i",
        "name": "MinimumDamagePct",
    },
    11092: {

        "size": 4,
        "format": "<i",
        "name": "command_11092",
    },
    11093: {

        "size": 4,
        "format": "<i",
        "name": "command_11093",
    },
    11094: {

        "size": 4,
        "format": "<i",
        "name": "command_11094",
    },
    11095: {

        "size": 4,
        "format": "<i",
        "name": "command_11095",
    },
    11096: {

        "size": 8,
        "format": "<ii",
        "name": "command_11096",
    },
    11097: {

        "size": 8,
        "format": "<ii",
        "name": "command_11097",
    },
    11098: {

        "size": 8,
        "format": "<ii",
        "name": "command_11098",
    },
    11099: {

        "size": 4,
        "format": "<i",
        "name": "command_11099",
    },
    11100: {

        "size": 4,
        "format": "<i",
        "name": "command_11100",
    },
    11101: {

        "size": 4,
        "format": "<i",
        "name": "command_11101",
    },
    11102: {

        "size": 4,
        "format": "<i",
        "name": "command_11102",
    },
    11103: {

        "size": 32,
        "format": "<32s",
        "name": "command_11103",
    },
    11104: {

        "size": 4,
        "format": "<i",
        "name": "command_11104",
    },
    11105: {

        "size": 4,
        "format": "<i",
        "name": "command_11105",
    },
    11106: {

        "size": 4,
        "format": "<i",
        "name": "command_11106",
    },
    11107: {

        "size": 4,
        "format": "<i",
        "name": "command_11107",
    },
    11108: {

        "size": 4,
        "format": "<4s",
        "name": "command_11108",
    },
    11109: {

        "size": 4,
        "format": "<4s",
        "name": "command_11109",
    },
    11110: {

        "size": 4,
        "format": "<i",
        "name": "command_11110",
    },
    12000: {

        "size": 4,
        "format": "<i",
        "name": "WalkFSpeed",
    },
    12001: {

        "size": 4,
        "format": "<i",
        "name": "WalkBSpeed",
    },
    12002: {

        "size": 4,
        "format": "<i",
        "name": "DashFInitialVelocity",
    },
    12003: {

        "size": 4,
        "format": "<i",
        "name": "DashFAccel",
    },
    12004: {

        "size": 4,
        "format": "<i",
        "name": "DashFMaxVelocity",
    },
    12005: {

        "size": 4,
        "format": "<i",
        "name": "JumpYVelocity",
    },
    12006: {

        "size": 4,
        "format": "<i",
        "name": "SuperJumpYVelocity",
    },
    12007: {

        "size": 4,
        "format": "<i",
        "name": "command_12007",
    },
    12008: {

        "size": 4,
        "format": "<i",
        "name": "command_12008",
    },
    12009: {

        "size": 4,
        "format": "<i",
        "name": "command_12009",
    },
    12010: {

        "size": 4,
        "format": "<i",
        "name": "command_12010",
    },
    12011: {

        "size": 4,
        "format": "<i",
        "name": "command_12011",
    },
    12012: {

        "size": 4,
        "format": "<i",
        "name": "DoubleJumpCount",
    },
    12013: {

        "size": 4,
        "format": "<i",
        "name": "AirDashCount",
    },
    12014: {

        "size": 4,
        "format": "<i",
        "name": "command_12014",
    },
    12015: {

        "size": 4,
        "format": "<i",
        "name": "Health",
    },
    12016: {

        "size": 8,
        "format": "<ii",
        "name": "command_12016",
    },
    12017: {

        "size": 4,
        "format": "<i",
        "name": "ComboRate",
    },
    12018: {

        "size": 36,
        "format": "<i32s",
        "name": "command_12018",
    },
    12019: {

        "size": 16,
        "format": "<16s",
        "name": "command_12019",
    },
    12020: {

        "size": 0,
        "format": "<",
        "name": "command_12020",
    },
    12021: {

        "size": 4,
        "format": "<i",
        "name": "command_12021",
    },
    12022: {

        "size": 4,
        "format": "<i",
        "name": "command_12022",
    },
    12023: {

        "size": 4,
        "format": "<i",
        "name": "command_12023",
    },
    12024: {

        "size": 4,
        "format": "<i",
        "name": "command_12024",
    },
    12025: {

        "size": 4,
        "format": "<i",
        "name": "command_12025",
    },
    12026: {

        "size": 4,
        "format": "<i",
        "name": "command_12026",
    },
    12027: {

        "size": 4,
        "format": "<i",
        "name": "command_12027",
    },
    12028: {

        "size": 4,
        "format": "<i",
        "name": "command_12028",
    },
    12029: {

        "size": 4,
        "format": "<i",
        "name": "command_12029",
    },
    12030: {

        "size": 4,
        "format": "<i",
        "name": "command_12030",
    },
    12031: {

        "size": 4,
        "format": "<i",
        "name": "JumpStartup",
    },
    12032: {

        "size": 24,
        "format": "<24s",
        "name": "command_12032",
    },
    12033: {

        "size": 4,
        "format": "<i",
        "name": "command_12033",
    },
    12034: {

        "size": 4,
        "format": "<i",
        "name": "command_12034",
    },
    12035: {

        "size": 4,
        "format": "<i",
        "name": "AirBDashDuration",
    },
    12036: {

        "size": 4,
        "format": "<i",
        "name": "SuperFreezeDuration",
    },
    12037: {

        "size": 4,
        "format": "<i",
        "name": "command_12037",
    },
    12038: {

        "size": 4,
        "format": "<i",
        "name": "command_12038",
    },
    12039: {

        "size": 4,
        "format": "<i",
        "name": "AirDashBSpeed",
    },
    12040: {

        "size": 4,
        "format": "<i",
        "name": "command_12040",
    },
    12041: {

        "size": 24,
        "format": "<24s",
        "name": "command_12041",
    },
    12042: {

        "size": 4,
        "format": "<i",
        "name": "command_12042",
    },
    12043: {

        "size": 4,
        "format": "<i",
        "name": "command_12043",
    },
    12044: {

        "size": 4,
        "format": "<i",
        "name": "command_12044",
    },
    12045: {

        "size": 64,
        "format": "<16i",
        "name": "command_12045",
    },
    12046: {

        "size": 4,
        "format": "<i",
        "name": "command_12046",
    },
    12047: {

        "size": 4,
        "format": "<i",
        "name": "command_12047",
    },
    12048: {

        "size": 4,
        "format": "<i",
        "name": "command_12048",
    },
    12049: {

        "size": 4,
        "format": "<i",
        "name": "command_12049",
    },
    12050: {

        "size": 4,
        "format": "<i",
        "name": "command_12050",
    },
    12051: {

        "size": 4,
        "format": "<i",
        "name": "StarterRating",
    },
    12052: {

        "size": 4,
        "format": "<i",
        "name": "command_12052",
    },
    12053: {

        "size": 40,
        "format": "<10i",
        "name": "OverdriveDuration",
    },
    12054: {

        "size": 8,
        "format": "<ii",
        "name": "command_12054",
    },
    12055: {

        "size": 4,
        "format": "<i",
        "name": "command_12055",
    },
    12056: {

        "size": 0,
        "format": "<",
        "name": "command_12056",
    },
    12057: {

        "size": 4,
        "format": "<i",
        "name": "command_12057",
    },
    12058: {

        "size": 4,
        "format": "<i",
        "name": "command_12058",
    },
    12059: {

        "size": 36,
        "format": "<36s",
        "name": "command_12059",
    },
    12060: {

        "size": 4,
        "format": "<i",
        "name": "command_12060",
    },
    13000: {

        "size": 4,
        "format": "<i",
        "name": "command_13000",
    },
    13001: {

        "size": 4,
        "format": "<i",
        "name": "command_13001",
    },
    13002: {

        "size": 4,
        "format": "<i",
        "name": "command_13002",
    },
    13003: {

        "size": 4,
        "format": "<i",
        "name": "command_13003",
    },
    13004: {

        "size": 4,
        "format": "<i",
        "name": "command_13004",
    },
    13005: {

        "size": 4,
        "format": "<i",
        "name": "command_13005",
    },
    13006: {

        "size": 4,
        "format": "<i",
        "name": "command_13006",
    },
    13007: {

        "size": 4,
        "format": "<i",
        "name": "command_13007",
    },
    13008: {

        "size": 4,
        "format": "<i",
        "name": "command_13008",
    },
    13009: {

        "size": 4,
        "format": "<i",
        "name": "command_13009",
    },
    13010: {

        "size": 4,
        "format": "<i",
        "name": "command_13010",
    },
    13011: {

        "size": 4,
        "format": "<i",
        "name": "command_13011",
    },
    13012: {

        "size": 4,
        "format": "<i",
        "name": "command_13012",
    },
    13013: {

        "size": 4,
        "format": "<i",
        "name": "command_13013",
    },
    13014: {

        "size": 4,
        "format": "<i",
        "name": "command_13014",
    },
    13015: {

        "size": 4,
        "format": "<i",
        "name": "command_13015",
    },
    13016: {

        "size": 4,
        "format": "<i",
        "name": "command_13016",
    },
    13017: {

        "size": 4,
        "format": "<i",
        "name": "command_13017",
    },
    13018: {

        "size": 4,
        "format": "<i",
        "name": "command_13018",
    },
    13019: {

        "size": 4,
        "format": "<i",
        "name": "command_13019",
    },
    13021: {

        "size": 4,
        "format": "<i",
        "name": "command_13021",
    },
    13022: {

        "size": 4,
        "format": "<i",
        "name": "command_13022",
    },
    13024: {

        "size": 4,
        "format": "<i",
        "name": "command_13024",
    },
    13026: {

        "size": 4,
        "format": "<i",
        "name": "command_13026",
    },
    13027: {

        "size": 4,
        "format": "<i",
        "name": "command_13027",
    },
    13028: {

        "size": 4,
        "format": "<i",
        "name": "command_13028",
    },
    13029: {

        "size": 4,
        "format": "<i",
        "name": "command_13029",
    },
    13030: {

        "size": 4,
        "format": "<i",
        "name": "command_13030",
    },
    13031: {

        "size": 4,
        "format": "<i",
        "name": "command_13031",
    },
    13032: {

        "size": 4,
        "format": "<i",
        "name": "command_13032",
    },
    13033: {

        "size": 4,
        "format": "<i",
        "name": "command_13033",
    },
    13034: {

        "size": 4,
        "format": "<i",
        "name": "command_13034",
    },
    13035: {

        "size": 4,
        "format": "<i",
        "name": "command_13035",
    },
    13036: {

        "size": 4,
        "format": "<i",
        "name": "command_13036",
    },
    13037: {

        "size": 4,
        "format": "<i",
        "name": "command_13037",
    },
    13038: {

        "size": 4,
        "format": "<i",
        "name": "command_13038",
    },
    13039: {

        "size": 4,
        "format": "<i",
        "name": "command_13039",
    },
    13040: {

        "size": 64,
        "format": "<64s",
        "name": "command_13040",
    },
    13041: {

        "size": 8,
        "format": "<ii",
        "name": "command_13041",
    },
    13042: {

        "size": 0,
        "format": "<",
        "name": "command_13042",
    },
    13043: {

        "size": 4,
        "format": "<i",
        "name": "command_13043",
    },
    13044: {

        "size": 4,
        "format": "<i",
        "name": "command_13044",
    },
    13045: {

        "size": 4,
        "format": "<i",
        "name": "command_13045",
    },
    13054: {

        "size": 4,
        "format": "<i",
        "name": "command_13054",
    },
    14000: {

        "size": 0,
        "format": "<",
        "name": "command_14000",
    },
    14001: {

        "size": 36,
        "format": "<32si",
        "name": "Move_Register",
    },
    14002: {

        "size": 0,
        "format": "<",
        "name": "Move_EndRegister",
    },
    14003: {

        "size": 4,
        "format": "<i",
        "name": "Move_AirGround_",
    },
    14004: {

        "size": 4,
        "format": "<i",
        "name": "command_14004",
    },
    14005: {

        "size": 4,
        "format": "<i",
        "name": "command_14005",
    },
    14006: {

        "size": 4,
        "format": "<i",
        "name": "command_14006",
    },
    14007: {

        "size": 4,
        "format": "<i",
        "name": "command_14007",
    },
    14008: {

        "size": 4,
        "format": "<i",
        "name": "command_14008",
    },
    14009: {

        "size": 4,
        "format": "<i",
        "name": "command_14009",
    },
    14010: {

        "size": 4,
        "format": "<i",
        "name": "command_14010",
    },
    14011: {

        "size": 4,
        "format": "<i",
        "name": "command_14011",
    },
    14012: {

        "size": 4,
        "format": "<i",
        "name": "Move_Input_",
    },
    14013: {

        "size": 32,
        "format": "<32s",
        "name": "command_14013",
    },
    14014: {

        "size": 4,
        "format": "<i",
        "name": "command_14014",
    },
    14015: {

        "size": 24,
        "format": "<iiiiii",
        "name": "command_14015",
    },
    14017: {

        "size": 16,
        "format": "<16s",
        "name": "command_14017",
    },
    14018: {

        "size": 12,
        "format": "<iii",
        "name": "command_14018",
    },
    14019: {

        "size": 32,
        "format": "<32s",
        "name": "command_14019",
    },
    14020: {

        "size": 4,
        "format": "<i",
        "name": "command_14020",
    },
    14021: {

        "size": 4,
        "format": "<i",
        "name": "command_14021",
    },
    14022: {

        "size": 4,
        "format": "<i",
        "name": "MoveMaxChainRepeat",
    },
    14023: {

        "size": 4,
        "format": "<i",
        "name": "command_14023",
    },
    14024: {

        "size": 32,
        "format": "<32s",
        "name": "command_14024",
    },
    14025: {

        "size": 4,
        "format": "<i",
        "name": "command_14025",
    },
    14026: {

        "size": 4,
        "format": "<i",
        "name": "command_14026",
    },
    14027: {

        "size": 32,
        "format": "<32s",
        "name": "command_14027",
    },
    14029: {

        "size": 4,
        "format": "<i",
        "name": "command_14029",
    },
    14030: {

        "size": 4,
        "format": "<i",
        "name": "command_14030",
    },
    14033: {

        "size": 4,
        "format": "<i",
        "name": "command_14033",
    },
    14035: {

        "size": 36,
        "format": "<36s",
        "name": "command_14035",
    },
    14043: {

        "size": 0,
        "format": "<",
        "name": "command_14043",
    },
    14044: {

        "size": 40,
        "format": "<40s",
        "name": "command_14044",
    },
    14045: {

        "size": 8,
        "format": "<ii",
        "name": "command_14045",
    },
    14046: {

        "size": 4,
        "format": "<i",
        "name": "command_14046",
    },
    14047: {

        "size": 0,
        "format": "<",
        "name": "command_14047",
    },
    14048: {

        "size": 40,
        "format": "<32sii",
        "name": "command_14048",
    },
    14049: {

        "size": 72,
        "format": "<32s32sii",
        "name": "command_14049",
    },
    14067: {

        "size": 4,
        "format": "<i",
        "name": "command_14067",
    },
    14068: {

        "size": 32,
        "format": "<32s",
        "name": "WhiffCancel",
    },
    14069: {

        "size": 32,
        "format": "<32s",
        "name": "HitOrBlockCancel",
    },
    14070: {

        "size": 32,
        "format": "<32s",
        "name": "command_14070",
    },
    14071: {

        "size": 32,
        "format": "<32s",
        "name": "command_14071",
    },
    14072: {

        "size": 32,
        "format": "<32s",
        "name": "command_14072",
    },
    14073: {

        "size": 32,
        "format": "<32s",
        "name": "command_14073",
    },
    14074: {

        "size": 32,
        "format": "<32s",
        "name": "command_14074",
    },
    14075: {

        "size": 4,
        "format": "<i",
        "name": "command_14075",
    },
    14076: {

        "size": 4,
        "format": "<i",
        "name": "WhiffCancelEnable",
    },
    14077: {

        "size": 4,
        "format": "<i",
        "name": "command_14077",
    },
    14078: {

        "size": 4,
        "format": "<i",
        "name": "HitOrBlockJumpCancel",
    },
    14079: {

        "size": 4,
        "format": "<i",
        "name": "JumpCancel_",
    },
    14080: {

        "size": 32,
        "format": "<32s",
        "name": "HitCancel",
    },
    14081: {

        "size": 4,
        "format": "<i",
        "name": "HitJumpCancel",
    },
    14082: {

        "size": 4,
        "format": "<i",
        "name": "command_14082",
    },
    14083: {

        # Reference says this should be size 4 but that does not work for us??
        "size": 32,
        "format": "<32s",
        "name": "command_14083",
    },
    14084: {

        "size": 32,
        "format": "<32s",
        "name": "command_14084",
    },
    14085: {

        "size": 32,
        "format": "<32s",
        "name": "command_14085",
    },
    14086: {

        "size": 32,
        "format": "<32s",
        "name": "command_14086",
    },
    14087: {

        "size": 4,
        "format": "<i",
        "name": "command_14087",
    },
    14088: {

        "size": 4,
        "format": "<i",
        "name": "command_14088",
    },
    14090: {

        "size": 0,
        "format": "<",
        "name": "command_14090",
    },
    14091: {

        "size": 0,
        "format": "<",
        "name": "command_14091",
    },
    14092: {

        "size": 0,
        "format": "<",
        "name": "command_14092",
    },
    14093: {

        "size": 0,
        "format": "<",
        "name": "command_14093",
    },
    14094: {

        "size": 0,
        "format": "<",
        "name": "command_14094",
    },
    15000: {

        "size": 4,
        "format": "<i",
        "name": "command_15000",
    },
    15001: {

        "size": 12,
        "format": "<iii",
        "name": "command_15001",
    },
    15003: {

        "size": 4,
        "format": "<i",
        "name": "command_15003",
    },
    15004: {

        "size": 4,
        "format": "<i",
        "name": "command_15004",
    },
    15005: {

        "size": 4,
        "format": "<i",
        "name": "command_15005",
    },
    15006: {

        "size": 4,
        "format": "<i",
        "name": "command_15006",
    },
    15007: {

        "size": 4,
        "format": "<i",
        "name": "command_15007",
    },
    15008: {

        "size": 0,
        "format": "<",
        "name": "command_15008",
    },
    15009: {

        "size": 0,
        "format": "<",
        "name": "command_15009",
    },
    15010: {

        "size": 0,
        "format": "<",
        "name": "command_15010",
    },
    15011: {

        "size": 4,
        "format": "<i",
        "name": "command_15011",
    },
    15012: {

        "size": 4,
        "format": "<i",
        "name": "command_15012",
    },
    15013: {

        "size": 4,
        "format": "<i",
        "name": "command_15013",
    },
    15014: {

        "size": 4,
        "format": "<i",
        "name": "command_15014",
    },
    15015: {

        "size": 8,
        "format": "<ii",
        "name": "command_15015",
    },
    15016: {

        "size": 12,
        "format": "<iii",
        "name": "command_15016",
    },
    15017: {

        "size": 8,
        "format": "<ii",
        "name": "command_15017",
    },
    15018: {

        "size": 4,
        "format": "<i",
        "name": "command_15018",
    },
    15019: {

        "size": 4,
        "format": "<i",
        "name": "command_15019",
    },
    15020: {

        "size": 16,
        "format": "<4i",
        "name": "command_15020",
    },
    15021: {

        "size": 4,
        "format": "<i",
        "name": "command_15021",
    },
    15022: {

        "size": 16,
        "format": "<16s",
        "name": "command_15022",
    },
    15023: {

        "size": 4,
        "format": "<i",
        "name": "command_15023",
    },
    15024: {

        "size": 68,
        "format": "<32s32si",
        "name": "command_15024",
    },
    15025: {

        "size": 20,
        "format": "<20s",
        "name": "command_15025",
    },
    15026: {

        "size": 12,
        "format": "<iii",
        "name": "command_15026",
    },
    15027: {

        "size": 4,
        "format": "<i",
        "name": "command_15027",
    },
    16000: {

        "size": 40,
        "format": "<40s",
        "name": "command_16000",
    },
    16001: {

        "size": 40,
        "format": "<40s",
        "name": "command_16001",
    },
    17000: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_StandingNormal",
    },
    17001: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_AirNormal",
    },
    17002: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_StandingSpecial",
    },
    17003: {

        "size": 0,
        "format": "<",
        "name": "command_17003",
    },
    17004: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_StandingDD",
    },
    17005: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_AirDD",
    },
    17006: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_CrouchingNormal",
    },
    17007: {

        "size": 0,
        "format": "<",
        "name": "command_17007",
    },
    17008: {

        "size": 0,
        "format": "<",
        "name": "command_17008",
    },
    17009: {

        "size": 0,
        "format": "<",
        "name": "command_17009",
    },
    17010: {

        "size": 0,
        "format": "<",
        "name": "command_17010",
    },
    17011: {

        "size": 44,
        "format": "<32siii",
        "name": "command_17011",
    },
    17012: {

        "size": 12,
        "format": "<iii",
        "name": "command_17012",
    },
    17013: {

        "size": 0,
        "format": "<",
        "name": "command_17013",
    },
    17014: {

        "size": 0,
        "format": "<",
        "name": "command_17014",
    },
    17015: {

        "size": 0,
        "format": "<",
        "name": "command_17015",
    },
    17016: {

        "size": 0,
        "format": "<",
        "name": "command_17016",
    },
    17017: {

        "size": 0,
        "format": "<",
        "name": "AttackDefaults_Astral",
    },
    17018: {

        "size": 0,
        "format": "<",
        "name": "command_17018",
    },
    17019: {

        "size": 0,
        "format": "<",
        "name": "ScriptEndGroundBOunce_",
    },
    17020: {

        "size": 0,
        "format": "<",
        "name": "ScriptSameAttackComboNoSpecialCancel",
    },
    17021: {

        "size": 0,
        "format": "<",
        "name": "command_17021",
    },
    17022: {

        "size": 0,
        "format": "<",
        "name": "command_17022",
    },
    17023: {

        "size": 0,
        "format": "<",
        "name": "command_17023",
    },
    17024: {

        "size": 0,
        "format": "<",
        "name": "command_17024",
    },
    17025: {

        "size": 0,
        "format": "<",
        "name": "command_17025",
    },
    18001: {

        "size": 0,
        "format": "<",
        "name": "command_18001",
    },
    18003: {

        "size": 128,
        "format": "<128s",
        "name": "command_18003",
    },
    18004: {

        "size": 8,
        "format": "<ii",
        "name": "command_18004",
    },
    18005: {

        "size": 8,
        "format": "<ii",
        "name": "command_18005",
    },
    18006: {

        "size": 8,
        "format": "<ii",
        "name": "command_18006",
    },
    18007: {

        "size": 12,
        "format": "<iii",
        "name": "command_18007",
    },
    18008: {

        "size": 0,
        "format": "<",
        "name": "command_18008",
    },
    18009: {

        "size": 4,
        "format": "<i",
        "name": "command_18009",
    },
    18010: {

        "size": 0,
        "format": "<",
        "name": "command_18010",
    },
    18011: {

        "size": 144,
        "format": "<16s64h",
        "name": "command_18011",
    },
    19000: {

        "size": 4,
        "format": "<i",
        "name": "command_19000",
    },
    19001: {

        "size": 4,
        "format": "<i",
        "name": "command_19001",
    },
    19002: {

        "size": 0,
        "format": "<",
        "name": "command_19002",
    },
    19003: {

        "size": 0,
        "format": "<",
        "name": "command_19003",
    },
    19004: {

        "size": 8,
        "format": "<ii",
        "name": "command_19004",
    },
    19005: {

        "size": 4,
        "format": "<i",
        "name": "command_19005",
    },
    19006: {

        "size": 4,
        "format": "<i",
        "name": "command_19006",
    },
    19007: {

        "size": 0,
        "format": "<",
        "name": "command_19007",
    },
    19008: {

        "size": 0,
        "format": "<",
        "name": "command_19008",
    },
    19009: {

        "size": 4,
        "format": "<i",
        "name": "command_19009",
    },
    19010: {

        "size": 8,
        "format": "<ii",
        "name": "command_19010",
    },
    19011: {

        "size": 4,
        "format": "<i",
        "name": "command_19011",
    },
    19012: {

        "size": 4,
        "format": "<i",
        "name": "command_19012",
    },
    19013: {

        "size": 0,
        "format": "<",
        "name": "command_19013",
    },
    19014: {

        "size": 0,
        "format": "<",
        "name": "command_19014",
    },
    19015: {

        "size": 4,
        "format": "<i",
        "name": "command_19015",
    },
    19016: {

        "size": 8,
        "format": "<ii",
        "name": "command_19016",
    },
    20000: {

        "size": 4,
        "format": "<i",
        "name": "command_20000",
    },
    20001: {

        "size": 4,
        "format": "<i",
        "name": "command_20001",
    },
    20002: {

        "size": 4,
        "format": "<i",
        "name": "command_20002",
    },
    20003: {

        "size": 4,
        "format": "<i",
        "name": "command_20003",
    },
    20004: {

        "size": 4,
        "format": "<i",
        "name": "command_20004",
    },
    20005: {

        "size": 8,
        "format": "<ii",
        "name": "command_20005",
    },
    20006: {

        "size": 4,
        "format": "<i",
        "name": "command_20006",
    },
    20007: {

        "size": 4,
        "format": "<i",
        "name": "command_20007",
    },
    20008: {

        "size": 4,
        "format": "<i",
        "name": "command_20008",
    },
    20009: {

        "size": 4,
        "format": "<i",
        "name": "command_20009",
    },
    20010: {

        "size": 12,
        "format": "<iii",
        "name": "command_20010",
    },
    20011: {

        "size": 8,
        "format": "<8s",
        "name": "command_20011",
    },
    21000: {

        "size": 4,
        "format": "<i",
        "name": "command_21000",
    },
    21001: {

        "size": 4,
        "format": "<i",
        "name": "command_21001",
    },
    21002: {

        "size": 4,
        "format": "<i",
        "name": "command_21002",
    },
    21003: {

        "size": 8,
        "format": "<ii",
        "name": "command_21003",
    },
    21004: {

        "size": 4,
        "format": "<i",
        "name": "command_21004",
    },
    21005: {

        "size": 4,
        "format": "<i",
        "name": "command_21005",
    },
    21006: {

        "size": 8,
        "format": "<ii",
        "name": "command_21006",
    },
    21007: {

        "size": 8,
        "format": "<ii",
        "name": "command_21007",
    },
    21008: {

        "size": 4,
        "format": "<i",
        "name": "command_21008",
    },
    21009: {

        "size": 24,
        "format": "<24s",
        "name": "command_21009",
    },
    21010: {

        "size": 4,
        "format": "<i",
        "name": "command_21010",
    },
    21011: {

        "size": 4,
        "format": "<i",
        "name": "command_21011",
    },
    21012: {

        "size": 36,
        "format": "<36s",
        "name": "command_21012",
    },
    21013: {

        "size": 36,
        "format": "<36s",
        "name": "command_21013",
    },
    21014: {

        "size": 4,
        "format": "<i",
        "name": "command_21014",
    },
    21015: {

        "size": 40,
        "format": "<40s",
        "name": "command_21015",
    },
    22000: {

        "size": 0,
        "format": "<",
        "name": "command_22000",
    },
    22001: {

        "size": 4,
        "format": "<i",
        "name": "command_22001",
    },
    22002: {

        "size": 0,
        "format": "<",
        "name": "command_22002",
    },
    22003: {

        "size": 4,
        "format": "<i",
        "name": "command_22003",
    },
    22004: {

        "size": 8,
        "format": "<ii",
        "name": "command_22004",
    },
    22005: {

        "size": 32,
        "format": "<32s",
        "name": "command_22005",
    },
    22006: {

        "size": 4,
        "format": "<i",
        "name": "command_22006",
    },
    22007: {

        "size": 4,
        "format": "<i",
        "name": "setInvincible",
    },
    22008: {

        "size": 4,
        "format": "<i",
        "name": "setInvincibleFor",
    },
    22009: {

        "size": 4,
        "format": "<i",
        "name": "command_22009",
    },
    22019: {

        "size": 20,
        "format": "<20s",
        "name": "command_22019",
    },
    22020: {

        "size": 4,
        "format": "<i",
        "name": "GuardPoint_",
    },
    22021: {

        "size": 4,
        "format": "<i",
        "name": "command_22021",
    },
    22022: {

        "size": 4,
        "format": "<i",
        "name": "command_22022",
    },
    22023: {

        "size": 4,
        "format": "<i",
        "name": "command_22023",
    },
    22024: {

        "size": 4,
        "format": "<i",
        "name": "command_22024",
    },
    22025: {

        "size": 12,
        "format": "<iii",
        "name": "command_22025",
    },
    22026: {

        "size": 4,
        "format": "<i",
        "name": "command_22026",
    },
    22027: {

        "size": 4,
        "format": "<i",
        "name": "command_22027",
    },
    22028: {

        "size": 4,
        "format": "<i",
        "name": "command_22028",
    },
    22029: {

        "size": 4,
        "format": "<i",
        "name": "command_22029",
    },
    22030: {

        "size": 4,
        "format": "<i",
        "name": "command_22030",
    },
    22031: {

        "size": 8,
        "format": "<ii",
        "name": "command_22031",
    },
    22032: {

        "size": 4,
        "format": "<i",
        "name": "command_22032",
    },
    22033: {

        "size": 4,
        "format": "<i",
        "name": "command_22033",
    },
    22034: {

        "size": 4,
        "format": "<i",
        "name": "command_22034",
    },
    22035: {

        "size": 4,
        "format": "<i",
        "name": "command_22035",
    },
    22036: {

        "size": 4,
        "format": "<i",
        "name": "command_22036",
    },
    22037: {

        "size": 4,
        "format": "<i",
        "name": "command_22037",
    },
    22038: {

        "size": 4,
        "format": "<i",
        "name": "command_22038",
    },
    22039: {

        "size": 4,
        "format": "<i",
        "name": "command_22039",
    },
    22500: {

        "size": 4,
        "format": "<i",
        "name": "command_22500",
    },
    23000: {

        "size": 12,
        "format": "<iii",
        "name": "command_23000",
    },
    23001: {

        "size": 8,
        "format": "<ii",
        "name": "command_23001",
    },
    23002: {

        "size": 0,
        "format": "<",
        "name": "command_23002",
    },
    23003: {

        "size": 32,
        "format": "<8i",
        "name": "command_23003",
    },
    23004: {

        "size": 8,
        "format": "<ii",
        "name": "command_23004",
    },
    23005: {

        "size": 8,
        "format": "<ii",
        "name": "command_23005",
    },
    23006: {

        "size": 8,
        "format": "<ii",
        "name": "command_23006",
    },
    23007: {

        "size": 8,
        "format": "<ii",
        "name": "command_23007",
    },
    23008: {

        "size": 8,
        "format": "<ii",
        "name": "command_23008",
    },
    23009: {

        "size": 8,
        "format": "<ii",
        "name": "command_23009",
    },
    23010: {

        "size": 8,
        "format": "<ii",
        "name": "command_23010",
    },
    23011: {

        "size": 4,
        "format": "<i",
        "name": "command_23011",
    },
    23012: {

        "size": 12,
        "format": "<iii",
        "name": "command_23012",
    },
    23013: {

        "size": 4,
        "format": "<i",
        "name": "command_23013",
    },
    23014: {

        "size": 0,
        "format": "<",
        "name": "command_23014",
    },
    23015: {

        "size": 4,
        "format": "<i",
        "name": "command_23015",
    },
    23016: {

        "size": 0,
        "format": "<",
        "name": "command_23016",
    },
    23017: {

        "size": 4,
        "format": "<i",
        "name": "command_23017",
    },
    23018: {

        "size": 4,
        "format": "<i",
        "name": "command_23018",
    },
    23019: {

        "size": 4,
        "format": "<i",
        "name": "command_23019",
    },
    23020: {

        "size": 4,
        "format": "<i",
        "name": "command_23020",
    },
    23021: {

        "size": 4,
        "format": "<i",
        "name": "command_23021",
    },
    23022: {

        "size": 4,
        "format": "<i",
        "name": "command_23022",
    },
    23023: {

        "size": 0,
        "format": "<",
        "name": "command_23023",
    },
    23024: {

        "size": 4,
        "format": "<i",
        "name": "command_23024",
    },
    23025: {

        "size": 4,
        "format": "<i",
        "name": "command_23025",
    },
    23026: {

        "size": 4,
        "format": "<i",
        "name": "command_23026",
    },
    23027: {

        "size": 0,
        "format": "<",
        "name": "DisableAttackRestOfMove",
    },
    23028: {

        "size": 8,
        "format": "<ii",
        "name": "command_23028",
    },
    23029: {

        "size": 12,
        "format": "<iii",
        "name": "command_23029",
    },
    23030: {

        "size": 64,
        "format": "<64s",
        "name": "command_23030",
    },
    23031: {

        "size": 4,
        "format": "<i",
        "name": "command_23031",
    },
    23032: {

        "size": 4,
        "format": "<i",
        "name": "command_23032",
    },
    23033: {

        "size": 4,
        "format": "<i",
        "name": "command_23033",
    },
    23034: {

        "size": 4,
        "format": "<i",
        "name": "command_23034",
    },
    23035: {

        "size": 4,
        "format": "<i",
        "name": "command_23035",
    },
    23036: {

        "size": 0,
        "format": "<",
        "name": "command_23036",
    },
    23037: {

        "size": 0,
        "format": "<",
        "name": "command_23037",
    },
    23038: {

        "size": 8,
        "format": "<ii",
        "name": "command_23038",
    },
    23039: {

        "size": 8,
        "format": "<ii",
        "name": "command_23039",
    },
    23040: {

        "size": 8,
        "format": "<ii",
        "name": "command_23040",
    },
    23041: {

        "size": 8,
        "format": "<ii",
        "name": "command_23041",
    },
    23042: {

        "size": 0,
        "format": "<",
        "name": "command_23042",
    },
    23043: {

        "size": 12,
        "format": "<iii",
        "name": "PhysicsPull",
    },
    23044: {

        "size": 8,
        "format": "<ii",
        "name": "command_23044",
    },
    23045: {

        "size": 4,
        "format": "<4s",
        "name": "command_23045",
    },
    23046: {

        "size": 4,
        "format": "<4s",
        "name": "command_23046",
    },
    23047: {

        "size": 8,
        "format": "<8s",
        "name": "command_23047",
    },
    23048: {

        "size": 4,
        "format": "<4s",
        "name": "command_23048",
    },
    23049: {

        "size": 8,
        "format": "<8s",
        "name": "command_23049",
    },
    23050: {

        "size": 8,
        "format": "<8s",
        "name": "command_23050",
    },
    23051: {

        "size": 64,
        "format": "<64s",
        "name": "command_23051",
    },
    23052: {

        "size": 4,
        "format": "<4s",
        "name": "command_23052",
    },
    23053: {

        "size": 8,
        "format": "<8s",
        "name": "command_23053",
    },
    23054: {

        "size": 36,
        "format": "<36s",
        "name": "command_23054",
    },
    23055: {

        "size": 0,
        "format": "<",
        "name": "command_23055",
    },
    23056: {

        "size": 0,
        "format": "<",
        "name": "command_23056",
    },
    23057: {

        "size": 4,
        "format": "<i",
        "name": "command_23057",
    },
    23058: {

        "size": 4,
        "format": "<i",
        "name": "command_23058",
    },
    23059: {

        "size": 4,
        "format": "<i",
        "name": "command_23059",
    },
    23060: {

        "size": 4,
        "format": "<i",
        "name": "command_23060",
    },
    23066: {

        "size": 4,
        "format": "<i",
        "name": "command_23066",
    },
    23067: {

        "size": 32,
        "format": "<32s",
        "name": "command_23067",
    },
    23068: {

        "size": 4,
        "format": "<i",
        "name": "command_23068",
    },
    23069: {

        "size": 4,
        "format": "<i",
        "name": "command_23069",
    },
    23070: {

        "size": 4,
        "format": "<i",
        "name": "command_23070",
    },
    23071: {

        "size": 4,
        "format": "<i",
        "name": "command_23071",
    },
    23072: {

        "size": 0,
        "format": "<",
        "name": "command_23072",
    },
    23073: {

        "size": 0,
        "format": "<",
        "name": "command_23073",
    },
    23074: {

        "size": 0,
        "format": "<",
        "name": "command_23074",
    },
    23075: {

        "size": 0,
        "format": "<",
        "name": "command_23075",
    },
    23076: {

        "size": 0,
        "format": "<",
        "name": "command_23076",
    },
    23077: {

        "size": 4,
        "format": "<i",
        "name": "command_23077",
    },
    23078: {

        "size": 4,
        "format": "<i",
        "name": "command_23078",
    },
    23079: {

        "size": 4,
        "format": "<i",
        "name": "command_23079",
    },
    23080: {

        "size": 12,
        "format": "<iii",
        "name": "command_23080",
    },
    23081: {

        "size": 4,
        "format": "<i",
        "name": "command_23081",
    },
    23082: {

        "size": 16,
        "format": "<16s",
        "name": "command_23082",
    },
    23083: {

        "size": 4,
        "format": "<i",
        "name": "command_23083",
    },
    23084: {

        "size": 4,
        "format": "<i",
        "name": "command_23084",
    },
    23085: {

        "size": 4,
        "format": "<i",
        "name": "command_23085",
    },
    23086: {

        "size": 4,
        "format": "<i",
        "name": "command_23086",
    },
    23087: {

        "size": 4,
        "format": "<i",
        "name": "command_23087",
    },
    23088: {

        "size": 8,
        "format": "<ii",
        "name": "command_23088",
    },
    23089: {

        "size": 32,
        "format": "<32s",
        "name": "command_23089",
    },
    23090: {

        "size": 4,
        "format": "<i",
        "name": "command_23090",
    },
    23091: {

        "size": 4,
        "format": "<i",
        "name": "command_23091",
    },
    23093: {

        "size": 4,
        "format": "<i",
        "name": "command_23093",
    },
    23094: {

        "size": 4,
        "format": "<i",
        "name": "command_23094",
    },
    23095: {

        "size": 4,
        "format": "<i",
        "name": "command_23095",
    },
    23096: {

        "size": 4,
        "format": "<i",
        "name": "command_23096",
    },
    23097: {

        "size": 4,
        "format": "<i",
        "name": "command_23097",
    },
    23098: {

        "size": 4,
        "format": "<i",
        "name": "command_23098",
    },
    23099: {

        "size": 4,
        "format": "<i",
        "name": "command_23099",
    },
    23100: {

        "size": 4,
        "format": "<i",
        "name": "command_23100",
    },
    23101: {

        "size": 4,
        "format": "<i",
        "name": "command_23101",
    },
    23102: {

        "size": 4,
        "format": "<i",
        "name": "command_23102",
    },
    23103: {

        "size": 4,
        "format": "<i",
        "name": "command_23103",
    },
    23104: {

        "size": 4,
        "format": "<i",
        "name": "command_23104",
    },
    23105: {

        "size": 4,
        "format": "<i",
        "name": "command_23105",
    },
    23106: {

        "size": 4,
        "format": "<i",
        "name": "command_23106",
    },
    23107: {

        "size": 4,
        "format": "<i",
        "name": "command_23107",
    },
    23108: {

        "size": 4,
        "format": "<i",
        "name": "command_23108",
    },
    23109: {

        "size": 4,
        "format": "<i",
        "name": "command_23109",
    },
    23110: {

        "size": 4,
        "format": "<i",
        "name": "command_23110",
    },
    23111: {

        "size": 4,
        "format": "<i",
        "name": "command_23111",
    },
    23112: {

        "size": 4,
        "format": "<i",
        "name": "command_23112",
    },
    23113: {

        "size": 4,
        "format": "<i",
        "name": "command_23113",
    },
    23114: {

        "size": 4,
        "format": "<i",
        "name": "command_23114",
    },
    23115: {

        "size": 4,
        "format": "<i",
        "name": "command_23115",
    },
    23116: {

        "size": 4,
        "format": "<i",
        "name": "command_23116",
    },
    23117: {

        "size": 8,
        "format": "<ii",
        "name": "command_23117",
    },
    23118: {

        "size": 4,
        "format": "<i",
        "name": "command_23118",
    },
    23119: {

        "size": 12,
        "format": "<iii",
        "name": "command_23119",
    },
    23120: {

        "size": 0,
        "format": "<",
        "name": "command_23120",
    },
    23121: {

        "size": 4,
        "format": "<i",
        "name": "command_23121",
    },
    23122: {

        "size": 4,
        "format": "<i",
        "name": "command_23122",
    },
    23123: {

        "size": 8,
        "format": "<ii",
        "name": "command_23123",
    },
    23124: {

        "size": 4,
        "format": "<i",
        "name": "command_23124",
    },
    23125: {

        "size": 0,
        "format": "<",
        "name": "command_23125",
    },
    23126: {

        "size": 4,
        "format": "<i",
        "name": "command_23126",
    },
    23130: {

        "size": 12,
        "format": "<iii",
        "name": "command_23130",
    },
    23131: {

        "size": 0,
        "format": "<",
        "name": "command_23131",
    },
    23132: {

        "size": 4,
        "format": "<i",
        "name": "command_23132",
    },
    23141: {

        "size": 4,
        "format": "<i",
        "name": "command_23141",
    },
    23142: {

        "size": 4,
        "format": "<i",
        "name": "command_23142",
    },
    23143: {

        "size": 12,
        "format": "<iii",
        "name": "command_23143",
    },
    23144: {

        "size": 44,
        "format": "<44s",
        "name": "command_23144",
    },
    23145: {

        "size": 32,
        "format": "<32s",
        "name": "command_23145",
    },
    23146: {

        "size": 36,
        "format": "<36s",
        "name": "command_23146",
    },
    23147: {

        "size": 0,
        "format": "<",
        "name": "command_23147",
    },
    23148: {

        "size": 32,
        "format": "<32s",
        "name": "command_23148",
    },
    23149: {

        "size": 4,
        "format": "<i",
        "name": "command_23149",
    },
    23150: {

        "size": 4,
        "format": "<i",
        "name": "command_23150",
    },
    23151: {

        "size": 8,
        "format": "<ii",
        "name": "command_23151",
    },
    23152: {

        "size": 4,
        "format": "<i",
        "name": "command_23152",
    },
    23153: {

        "size": 4,
        "format": "<i",
        "name": "command_23153",
    },
    23154: {

        "size": 4,
        "format": "<i",
        "name": "command_23154",
    },
    23155: {

        "size": 40,
        "format": "<40s",
        "name": "command_23155",
    },
    23156: {

        "size": 32,
        "format": "<32s",
        "name": "command_23156",
    },
    23157: {

        "size": 4,
        "format": "<i",
        "name": "command_23157",
    },
    23158: {

        # Reference says this should be size 8 but that does not work for us??
        "size": 12,
        "format": "<12s",
        "name": "command_23158",
    },
    23159: {

        "size": 32,
        "format": "<32s",
        "name": "command_23159",
    },
    23160: {

        "size": 4,
        "format": "<i",
        "name": "command_23160",
    },
    23161: {

        "size": 4,
        "format": "<i",
        "name": "command_23161",
    },
    23162: {

        "size": 4,
        "format": "<i",
        "name": "command_23162",
    },
    23163: {

        "size": 4,
        "format": "<i",
        "name": "command_23163",
    },
    23164: {

        "size": 4,
        "format": "<i",
        "name": "command_23164",
    },
    23165: {

        "size": 0,
        "format": "<",
        "name": "command_23165",
    },
    23166: {

        "size": 32,
        "format": "<32s",
        "name": "command_23166",
    },
    23167: {

        "size": 0,
        "format": "<",
        "name": "command_23167",
    },
    23168: {

        "size": 4,
        "format": "<i",
        "name": "command_23168",
    },
    23169: {

        "size": 4,
        "format": "<i",
        "name": "command_23169",
    },
    23170: {

        "size": 32,
        "format": "<32s",
        "name": "command_23170",
    },
    23177: {

        "size": 0,
        "format": "<",
        "name": "command_23177",
    },
    23178: {

        "size": 4,
        "format": "<i",
        "name": "command_23178",
    },
    23179: {

        "size": 4,
        "format": "<i",
        "name": "command_23179",
    },
    23180: {

        "size": 4,
        "format": "<i",
        "name": "command_23180",
    },
    23181: {

        "size": 4,
        "format": "<i",
        "name": "command_23181",
    },
    23182: {

        "size": 4,
        "format": "<i",
        "name": "command_23182",
    },
    23183: {

        "size": 44,
        "format": "<44s",
        "name": "command_23183",
    },
    23184: {

        "size": 32,
        "format": "<32s",
        "name": "command_23184",
    },
    23185: {

        "size": 36,
        "format": "<36s",
        "name": "command_23185",
    },
    30000: {

        "size": 0,
        "format": "<",
        "name": "command_30000",
    },
    30001: {

        "size": 36,
        "format": "<36s",
        "name": "command_30001",
    },
    30002: {

        "size": 12,
        "format": "<iii",
        "name": "command_30002",
    },
    30003: {

        "size": 4,
        "format": "<i",
        "name": "command_30003",
    },
    30004: {

        "size": 12,
        "format": "<12s",
        "name": "command_30004",
    },
    30005: {

        "size": 4,
        "format": "<i",
        "name": "command_30005",
    },
    30006: {

        "size": 12,
        "format": "<iii",
        "name": "command_30006",
    },
    30007: {

        "size": 4,
        "format": "<4s",
        "name": "command_30007",
    },
    30008: {

        "size": 8,
        "format": "<8s",
        "name": "command_30008",
    },
    30009: {

        "size": 4,
        "format": "<4s",
        "name": "command_30009",
    },
    30010: {

        "size": 4,
        "format": "<4s",
        "name": "command_30010",
    },
    30011: {

        "size": 0,
        "format": "<",
        "name": "command_30011",
    },
    30012: {

        "size": 4,
        "format": "<4s",
        "name": "command_30012",
    },
    30013: {

        "size": 0,
        "format": "<",
        "name": "command_30013",
    },
    30014: {

        "size": 0,
        "format": "<",
        "name": "command_30014",
    },
    30015: {

        "size": 0,
        "format": "<",
        "name": "command_30015",
    },
    30016: {

        "size": 4,
        "format": "<4s",
        "name": "command_30016",
    },
    30017: {

        "size": 4,
        "format": "<4s",
        "name": "command_30017",
    },
    30018: {

        "size": 0,
        "format": "<",
        "name": "command_30018",
    },
    30019: {

        "size": 8,
        "format": "<8s",
        "name": "command_30019",
    },
    30020: {

        "size": 0,
        "format": "<",
        "name": "command_30020",
    },
    30021: {

        "size": 0,
        "format": "<",
        "name": "command_30021",
    },
    30026: {

        "size": 0,
        "format": "<",
        "name": "command_30026",
    },
    30027: {

        "size": 0,
        "format": "<",
        "name": "command_30027",
    },
    30028: {

        "size": 4,
        "format": "<i",
        "name": "selfDamage",
    },
    30029: {

        "size": 4,
        "format": "<i",
        "name": "command_30029",
    },
    30030: {

        "size": 4,
        "format": "<i",
        "name": "command_30030",
    },
    30031: {

        "size": 4,
        "format": "<i",
        "name": "command_30031",
    },
    30032: {

        "size": 4,
        "format": "<i",
        "name": "command_30032",
    },
    30033: {

        "size": 4,
        "format": "<i",
        "name": "command_30033",
    },
    30034: {

        "size": 0,
        "format": "<",
        "name": "command_30034",
    },
    30035: {

        "size": 4,
        "format": "<i",
        "name": "command_30035",
    },
    30036: {

        "size": 36,
        "format": "<36s",
        "name": "command_30036",
    },
    30037: {

        "size": 0,
        "format": "<",
        "name": "command_30037",
    },
    30038: {

        "size": 4,
        "format": "<i",
        "name": "command_30038",
    },
    30039: {

        "size": 4,
        "format": "<i",
        "name": "command_30039",
    },
    30040: {

        "size": 4,
        "format": "<i",
        "name": "command_30040",
    },
    30041: {

        "size": 0,
        "format": "<",
        "name": "command_30041",
    },
    30042: {

        "size": 4,
        "format": "<i",
        "name": "command_30042",
    },
    30043: {

        "size": 4,
        "format": "<i",
        "name": "command_30043",
    },
    30044: {

        "size": 0,
        "format": "<",
        "name": "command_30044",
    },
    30045: {

        "size": 4,
        "format": "<i",
        "name": "command_30045",
    },
    30046: {

        "size": 4,
        "format": "<i",
        "name": "command_30046",
    },
    30047: {

        "size": 4,
        "format": "<i",
        "name": "command_30047",
    },
    30048: {

        "size": 4,
        "format": "<i",
        "name": "command_30048",
    },
    30049: {

        "size": 24,
        "format": "<24s",
        "name": "command_30049",
    },
    30050: {

        "size": 24,
        "format": "<24s",
        "name": "command_30050",
    },
    30051: {

        "size": 4,
        "format": "<i",
        "name": "command_30051",
    },
    30052: {

        "size": 4,
        "format": "<i",
        "name": "command_30052",
    },
    30053: {

        "size": 4,
        "format": "<i",
        "name": "command_30053",
    },
    30054: {

        "size": 4,
        "format": "<i",
        "name": "command_30054",
    },
    30055: {

        "size": 12,
        "format": "<12s",
        "name": "command_30055",
    },
    30056: {

        "size": 12,
        "format": "<12s",
        "name": "command_30056",
    },
    30057: {

        "size": 0,
        "format": "<",
        "name": "command_30057",
    },
    30058: {

        "size": 0,
        "format": "<",
        "name": "command_30058",
    },
    30059: {

        "size": 0,
        "format": "<",
        "name": "command_30059",
    },
    30060: {

        "size": 8,
        "format": "<8s",
        "name": "command_30060",
    },
    30061: {

        "size": 4,
        "format": "<i",
        "name": "command_30061",
    },
    30062: {

        "size": 4,
        "format": "<i",
        "name": "command_30062",
    },
    30063: {

        "size": 4,
        "format": "<i",
        "name": "command_30063",
    },
    30064: {

        "size": 4,
        "format": "<i",
        "name": "command_30064",
    },
    30065: {

        "size": 4,
        "format": "<i",
        "name": "command_30065",
    },
    30066: {

        "size": 4,
        "format": "<i",
        "name": "command_30066",
    },
    30067: {

        "size": 4,
        "format": "<i",
        "name": "command_30067",
    },
    30068: {

        "size": 4,
        "format": "<i",
        "name": "command_30068",
    },
    30069: {

        "size": 4,
        "format": "<i",
        "name": "command_30069",
    },
    30070: {

        "size": 32,
        "format": "<32s",
        "name": "command_30070",
    },
    30071: {

        "size": 0,
        "format": "<",
        "name": "command_30071",
    },
    30072: {

        "size": 0,
        "format": "<",
        "name": "command_30072",
    },
    30073: {

        "size": 4,
        "format": "<i",
        "name": "command_30073",
    },
    30074: {

        "size": 4,
        "format": "<i",
        "name": "command_30074",
    },
    30075: {

        "size": 4,
        "format": "<i",
        "name": "command_30075",
    },
    30076: {

        "size": 4,
        "format": "<i",
        "name": "command_30076",
    },
    30077: {

        "size": 8,
        "format": "<8s",
        "name": "command_30077",
    },
    30078: {

        "size": 4,
        "format": "<i",
        "name": "command_30078",
    },
    30079: {

        "size": 4,
        "format": "<i",
        "name": "command_30079",
    },
    30080: {

        "size": 0,
        "format": "<",
        "name": "command_30080",
    },
    30081: {

        "size": 0,
        "format": "<",
        "name": "command_30081",
    },
    30082: {

        "size": 4,
        "format": "<i",
        "name": "command_30082",
    },
    30083: {

        "size": 16,
        "format": "<16s",
        "name": "command_30083",
    },
    30084: {

        "size": 4,
        "format": "<i",
        "name": "command_30084",
    },
    30085: {

        "size": 4,
        "format": "<i",
        "name": "command_30085",
    },
    30086: {

        "size": 4,
        "format": "<i",
        "name": "command_30086",
    },
    30087: {

        "size": 4,
        "format": "<i",
        "name": "command_30087",
    },
    30088: {

        "size": 4,
        "format": "<i",
        "name": "command_30088",
    },
    30089: {

        "size": 4,
        "format": "<i",
        "name": "command_30089",
    },
    30090: {

        "size": 32,
        "format": "<16s16s",
        "name": "command_30090",
    },
    30092: {

        "size": 32,
        "format": "<16s16s",
        "name": "command_30092",
    },
    30093: {

        "size": 20,
        "format": "<iiiii",
        "name": "command_30093",
    },
}


def get_command(scr_data):
    """
    Get the next command from the script.
    We return the command ID, information from the command map,
    the arguments passed to the command, and remaining script data.
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
