#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Simulate HTTP request logs with randomized IPs, timestamps, status codes, and response sizes.
for log_index in range(10000):
    # Sleep for a random amount of time between requests to simulate varied response times
    sleep(random.random())
    
    # Generate a random IP address
    ip_address = "{}.{}.{}.{}".format(
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )
    
    # Current timestamp for log entry
    timestamp = datetime.datetime.now()
    
    # Randomly choose a status code for the request (e.g., 200 OK, 404 Not Found)
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    
    # Randomize response size in bytes
    response_size = random.randint(1, 1024)
    
    # Format and write log entry to standard output
    log_entry = "{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        ip_address,
        timestamp,
        status_code,
        response_size
    )
    
    # Output the log entry immediately
    sys.stdout.write(log_entry)
    sys.stdout.flush()
