#!/usr/bin/python3
"""
    a script that reads stdin line by line and computes metrics
"""
import sys


def print_msg(scodes, file_size):
    print("File size: {}".format(file_size))
    for key, value in sorted(scodes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
code = 0
count_lines = 0
scodes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in scodes.keys()):
                    scodes[code] += 1

            if (count_lines == 10):
                print_msg(scodes, file_size)
                count_lines = 0

finally:
    print_msg(scodes, file_size)
