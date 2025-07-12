def validornot(ta, num, pos):
    """
    Checks whether placing 'num' at position 'pos' in the Sudoku board is valid.

    Parameters:
    ta (list of list): 2D list representing the Sudoku board
    num (int): The number to be placed
    pos (tuple): Position as (row, column)

    Returns:
    bool: True if valid, False otherwise
    """

    # Check the row
    for i in range(len(ta[0])):
        if num == ta[pos[0]][i]:
            return False

    # Check the column
    for i in range(len(ta)):
        if num == ta[i][pos[1]]:
            return False

    # Check the 3x3 subgrid
    x = pos[0] // 3  # Row block index (0, 1, 2)
    y = pos[1] // 3  # Column block index (0, 1, 2)

    for i in range(x * 3, x * 3 + 3):
        for j in range(y * 3, y * 3 + 3):
            # Check if the number already exists in the subgrid
            if ta[i][j] == num and (i, j) != pos:
                return False

    return True

             
           