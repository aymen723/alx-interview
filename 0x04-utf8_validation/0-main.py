#!/usr/bin/python3
"""
Main file for testing UTF-8 Validation
"""

# Import the UTF-8 validation function
is_valid_utf8 = __import__('0-validate_utf8').is_valid_utf8

# Test case 1: Single valid ASCII character
byte_data = [65]  # ASCII for 'A'
print(is_valid_utf8(byte_data))  # Expected output: True

# Test case 2: Sequence of valid ASCII characters forming a sentence
byte_data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# Corresponds to: "Python is cool!"
print(is_valid_utf8(byte_data))  # Expected output: True

# Test case 3: Invalid UTF-8 byte sequence
byte_data = [229, 65, 127, 256]  # 256 is not a valid byte (out of range)
print(is_valid_utf8(byte_data))  # Expected output: False
