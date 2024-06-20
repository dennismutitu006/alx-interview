#!/usr/bin/env python3
import sys
import signal

# Initialize the metrics
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

# Function to print the metrics
def print_metrics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        if status_codes_count[status_code] > 0:
            print(f"{status_code}: {status_codes_count[status_code]}")

# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Attach the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
line_count = 0
try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) != 9:
            continue

        ip_address = parts[0]
        date = parts[3][1:] + " " + parts[4][:-1]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[8]
        try:
            file_size = int(parts[9])
        except ValueError:
            continue

        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        total_file_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        if line_count % 10 == 0:
            print_metrics()
except Exception as e:
    sys.stderr.write(f"Error: {str(e)}\n")
    sys.exit(1)
finally:
    print_metrics()

