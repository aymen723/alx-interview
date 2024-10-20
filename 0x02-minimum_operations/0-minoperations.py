#!/usr/bin/python3
'''minum op challenge'''

def minOperations(target):
    # Initialize current_chars to 1 (starting with 1 character on the notepad)
    # buffer to 0 (no characters copied yet)
    # operations_count to 0 (to count the number of operations performed)
    current_chars = 1
    buffer = 0
    operations_count = 0  

    # Loop until the number of current_chars equals or exceeds the target
    while current_chars < target:

        # If the buffer is empty, copy the current number of characters
        if buffer == 0:
            buffer = current_chars
            operations_count += 1  # Increment operation count for the copy action

        # If only 1 character is pasted, paste the content from the buffer
        if current_chars == 1:
            current_chars += buffer
            operations_count += 1  # Increment operation count for the paste action
            continue  # Skip the rest of the loop and start the next iteration

        # Calculate the remaining characters needed to reach the target
        remaining_chars = target - current_chars
     
        # If the remaining characters are less than the buffer's content, return 0 (invalid case)
        if remaining_chars < buffer:
            return 0

        # If the remaining characters are not a multiple of current_chars,
        # paste the buffer content
        if remaining_chars % current_chars != 0:
            current_chars += buffer
            operations_count += 1  # Increment operation count for the paste action
        else:
            # Otherwise, copy the current characters and then paste them
            buffer = current_chars
            current_chars += buffer
            operations_count += 2  # Increment operation count for both copy and paste actions

    # If the number of characters matches the target, return the total number of operations
    if current_chars == target:
        return operations_count
    else:
        return 0  # If something went wrong and the target wasn't reached, return 0
