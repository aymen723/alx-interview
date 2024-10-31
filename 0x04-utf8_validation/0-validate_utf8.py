#!/usr/bin/python3
"""
UTF-8 Encoding Validation
"""

def is_valid_utf8(byte_data):
    """
    byte_data: a list of integers representing bytes
    Returns: True if byte_data is a valid UTF-8 encoding,
             otherwise returns False
    """
    remaining_bytes = 0  # Number of remaining bytes in a multi-byte character

    for byte in byte_data:
        if remaining_bytes == 0:
            # Check how many bytes are in the current UTF-8 character
            if byte >> 5 == 0b110:  # 2-byte character
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                remaining_bytes = 3
            elif byte >> 7 == 0b1:  # Invalid single-byte character
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1  # Decrease the remaining bytes count

    # If there are no more expected continuation bytes, the encoding is valid
    return remaining_bytes == 0
