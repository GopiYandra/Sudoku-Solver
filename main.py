from Solver.validornot import validornot
from Solver.emptyornot import emptyornot
from Solver.printboard import printboard

def solve(ta):
    """
    Solves the Sudoku puzzle using recursion and backtracking.

    Parameters:
    ta (list of list): The Sudoku board

    Returns:
    bool: True if a solution is found, False otherwise
    """
    # Find the first empty cell
    pos = emptyornot(ta)
    
    # If no empty position, puzzle is solved
    if not pos:
        return True
    else:
        row, col = pos

    # Try numbers 1 to 9 in the empty position
    for i in range(1, 10):
        if validornot(ta, i, (row, col)):
            ta[row][col] = i  # Tentatively assign number

            # Recursively attempt to solve the rest
            if solve(ta):
                return True

            # Backtrack if not successful
            ta[row][col] = 0

    return False  # Trigger backtracking

# Initial Sudoku board (0 represents empty cells)
ta = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Display original board
printboard(ta)

# Solve and print result
a = solve(ta)
print(a)
print("solution")
printboard(ta)
