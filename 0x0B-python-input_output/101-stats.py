#!/usr/bin/python3
"""
Module documentation goes here
"""


import sys


def print_metrics(total_size, status_counts):
    """
    Function documentation goes here

    Args:
        total_size (int): The total file size.
        status_counts (dict): Dictionary containing counts
        for each status code.

    Returns:
        None

    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def process_lines():
    """
    Function documentation goes here

    Returns:
        None

    """
    total_size = 0
    status_counts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 9:
                total_size += int(parts[8])
                status_code = parts[7]
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
