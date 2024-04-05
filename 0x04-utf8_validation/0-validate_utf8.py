#!/usr/bin/python3
"""utf validation"""


def validUTF8(data):
    """
    a method that determines if a given data set represents a
    valid UTF-8 encoding
    """
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte >> 3 == 0b11110:  # 4 bytes
                num_bytes_to_follow = 3
            elif byte >> 4 == 0b1110:  # 3 bytes
                num_bytes_to_follow = 2
            elif byte >> 5 == 0b110:  # 2 bytes
                num_bytes_to_follow = 1
            elif byte >> 7 == 0b0:  # 1 byte
                continue
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
