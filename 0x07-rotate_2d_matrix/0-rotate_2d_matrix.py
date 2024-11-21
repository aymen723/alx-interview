#!/usr/bin/python3
'''Rotate a 2D matrix 90 degrees clockwise'''

def rotate_matrix_90_clockwise(matrix):
    '''Rotates a 2D matrix 90° clockwise in place.
    
    Args:
        matrix (list of list): The 2D matrix to rotate.
        
    Returns:
        None: The matrix is modified in place.
    '''
    start_col, end_col = 0, len(matrix) - 1  # Define the initial and final column indices.

    while start_col < end_col:
        for offset in range(end_col - start_col):
            top_row, bottom_row = start_col, end_col
            
            # Save the top-left value.
            top_left = matrix[top_row][start_col + offset]
            
            # Move the bottom-left value to the top-left position.
            matrix[top_row][start_col + offset] = matrix[bottom_row - offset][start_col]
            
            # Move the bottom-right value to the bottom-left position.
            matrix[bottom_row - offset][start_col] = matrix[bottom_row][end_col - offset]
            
            # Move the top-right value to the bottom-right position.
            matrix[bottom_row][end_col - offset] = matrix[top_row + offset][end_col]
            
            # Move the saved top-left value to the top-right position.
            matrix[top_row + offset][end_col] = top_left
        
        # Move to the inner layer of the matrix.
        end_col -= 1
        start_col += 1
