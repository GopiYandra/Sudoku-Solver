
def printboard(ta):
    """
    Function to print the Sudoku board in a formatted 9x9 grid.
    
    Parameters:
    ta (list of list): 2D list representing the Sudoku board.
    """
    for i in range(len(ta)):
        # Print a horizontal separator after every 3 rows (except the first)
        if i % 3 == 0 and i != 0:
            print("---" * len(ta))  # Separator line between boxes

        for j in range(len(ta[0])):
            # Print vertical separator after every 3 columns (except the first)
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            # Print each cell value with a space
            print(ta[i][j], end=" ")

        # Move to the next line after each row
        print()
                       