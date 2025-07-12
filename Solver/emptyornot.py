def emptyornot(ta):
    """
    Finds the first empty cell (value 0) in the Sudoku board.

    Parameters:
    ta (list of list): 2D list representing the Sudoku board

    Returns:
    tuple: Position (row, column) of the first empty cell
           If no empty cell is found, returns None implicitly
    """
    for i in range(len(ta)):
        for j in range(len(ta[0])):
            # Check for an empty cell
            if ta[i][j] == 0:
                # Return the position of the empty cell
                return i, j
