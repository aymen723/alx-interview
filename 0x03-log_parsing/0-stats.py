#!/usr/bin/python3
"""A script that reads lines from standard input and calculates metrics for HTTP status codes and total file size."""

import sys

# Dictionary to keep track of the count of each HTTP status code
status_code_count = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

# Variables to store the total size of all file transfers and a line counter
total_file_size = 0
line_counter = 0

try:
    # Process each line from standard input
    for line in sys.stdin:
        line_parts = line.split(" ")
        
        # Ensure line has enough parts to contain a status code and file size
        if len(line_parts) > 4:
            # Extract the HTTP status code and the file size from the line
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])
            
            # Update status code count if it's in the predefined dictionary
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            
            # Add the file size to the total and increment the line counter
            total_file_size += file_size
            line_counter += 1

        # Every 10 lines, output the metrics
        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_file_size))
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print('{}: {}'.format(code, count))

except Exception as error:
    # Suppress any exceptions during processing
    pass

finally:
    # Output metrics one last time upon program termination
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print('{}: {}'.format(code, count))
