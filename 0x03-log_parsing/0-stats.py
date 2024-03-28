#!/usr/bin/python3
"""stats"""
import sys


total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read Input Loop
    for line in sys.stdin:
        line = line.strip()
        print(line)
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip invalid lines
        ip_address, _, _, _, status_code, file_size = parts
        status_code = int(status_code)
        file_size = int(file_size)

        # Update Metrics
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        line_count += 1

        # Check for Print Trigger
        if line_count % 10 == 0:
            # Print Statistics
            print("Total file size:", total_file_size)
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print()

except (KeyboardInterrupt, EOFError):
    # Print final statistics if interrupted
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{code}: {count}")