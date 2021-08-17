import os
import argparse

from .scr import parse_script


def abs_path(value):
    value = os.path.abspath(value)

    if not os.path.exists(value):
        raise argparse.ArgumentError("Invalid file path! Does not exist!")

    return value


def main():
    parser = argparse.ArgumentParser("scr")
    subparsers = parser.add_subparsers(title="commands")

    tojson = subparsers.add_parser("tojson")
    tojson.add_argument(dest="scr_path", type=abs_path, help="Script bin file input path.")

    args, _ = parser.parse_known_args()

    scr_path = getattr(args, "scr_path", None)

    if scr_path is not None:
        parse_script(scr_path)


if __name__ == "__main__":
    main()
