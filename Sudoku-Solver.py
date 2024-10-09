def SudokuSolver():
    """Uses recursive backtracking to solve a 2d array that resembles a Sudoku board and solves it accordingly. """
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0 ,9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def solve(board):
        find = find_empty(board)
        if not find:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i
                if solve(board):
                    return True
                board[row][col] = 0
        return False

    def valid(board, num ,pos):
        # need to check the row, column and inner square .
        #1. Check Row
        for i in range(len(board[0])):
            if board[pos[0]][i] == num and pos[1] != i: # looking in row for the number but ignoring the current position
                return False
        #2. Check col
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i: # looking down col for number and ignoring current position
                return False
        # Chech inner square
        box_x = pos[1] // 3 # determines the horizontal box
        box_y = pos[0] // 3 # determines the vertical box
        for i in range(box_y*3, box_y*3 + 3): # multiplying allows for the correct indices to be selected
            for j in range(box_x*3, box_x*3 + 3): # ibid.
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True # means it's a valid position

    def print_board(board):
        for row in range(len(board)):
            if row % 3 == 0 and row!=0: #mulitiple of 3 valid but not 0
                print("- - - - - - - - - - - - -")
            for col in range(len(board[0])):
                if col % 3 == 0 and col!=0: #multiple of 3 valid but not 0
                    print(" | ", end="")
                if col == 8: # end of row
                    print(board[row][col])
                else: # middle of row
                    print(str(board[row][col]) + " ", end="")

    def find_empty(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return (i, j) # row, column
        return None
    print_board(board)
    solve(board)
    print("-" * len(board[0])* 3)
    print_board(board)
SudokuSolver()