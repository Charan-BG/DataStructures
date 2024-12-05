"""
Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.

Each of the digits 1-9 must occur exactly once in each column.

Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Constraints:

board.length == 9

board[i].length == 9

board[i][j] is a digit between 1 and 9 , inclusive or '.'.

It is guaranteed that the input board has only one solution.

Example: 

board = [

["5", "3", ".", ".", "7", ".", ".", ".", "."],

["6", ".", ".", "1", "9", "5", ".", ".", "."],

[".", "9", "8", ".", ".", ".", ".", "6", "."],

["8", ".", ".", ".", "6", ".", ".", ".", "3"],

["4", ".", ".", "8", ".", "3", ".", ".", "1"],

["7", ".", ".", ".", "2", ".", ".", ".", "6"],

[".", "6", ".", ".", ".", ".", "2", "8", "."],

[".", ".", ".", "4", "1", "9", ".", ".", "5"],

[".", ".", ".", ".", "8", ".", ".", "7", "9"]

]

Output : 


[

["5", "3", "4", "6", "7", "8", "9", "1", "2"],

["6", "7", "2", "1", "9", "5", "3", "4", "8"],

["1", "9", "8", "3", "4", "2", "5", "6", "7"],

["8", "5", "9", "7", "6", "1", "4", "2", "3"],

["4", "2", "6", "8", "5", "3", "7", "9", "1"],

["7", "1", "3", "9", "2", "4", "8", "5", "6"],

["9", "6", "1", "5", "3", "7", "2", "8", "4"],

["2", "8", "7", "4", "1", "9", "6", "3", "5"],

["3", "4", "5", "2", "8", "6", "1", "7", "9"]

]
"""
#TC=O(1) since its 9x9 board size is fixed it is solved in constant time
#SC=O(1) 
def sudoku(board):

    def is_valid(val, row, col, board):
        
        for x in range(9):
            #rowcheck
            if board[row][x]==val:
                return False
            #colcheck
            if board[x][col]==val:
                return False
            
            #boxcheck
            r=3*(row//3) + x // 3 #row 0,1,2
            c=3*(col//3) + x % 3  #col 3,4,5

            if board[r][c] == val:
                return False
        return True


    def main(board):

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    for val in '123456789':
                        if is_valid(val, row, col, board):
                            board[row][col]=val
                            if (main(board)): return True
                            board[row][col]="."
                    return False
        
        return True
    
    call=main(board)
    return call

board = [
["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# print(sudoku(board))









class SudokuSolver:
    def __init__(self, board):
        self.board = board

    def is_valid(self, val, row, col):
        """
        Check if placing the value `val` at position (row, col) is valid.
        """
        for x in range(9):
            # Row check
            if self.board[row][x] == val:
                return False
            # Column check
            if self.board[x][col] == val:
                return False
            # Box check
            r = 3 * (row // 3) + x // 3
            c = 3 * (col // 3) + x % 3
            if self.board[r][c] == val:
                return False
        return True

    def solve(self):
        """
        Solve the Sudoku board using backtracking.
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    for val in '123456789':
                        if self.is_valid(val, row, col):
                            self.board[row][col] = val
                            if self.solve():
                                return True
                            self.board[row][col] = "."
                    return False
        return True

    def get_board(self):
        """
        Return the solved Sudoku board.
        """
        return self.board


# Example usage
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# import time
# solver = SudokuSolver(board)
# if solver.solve():
#     solved_board = solver.get_board()
#     for row in solved_board:
#         time.sleep(10)
#         print(" ".join(row))
# else:
#     print("No solution exists.")


def sudoku(board):

    def isvalid(val, row, col, board):

        for x in range(9):

            if board[row][x]==val:
                return False
            
            if board[x][col]==val:
                return False
            
            r= 3*(row//3)+x//3
            c= 3*(col//3)+x%3
            if board[r][c]==val:
                return False
            
        return True
    
    def main(board):

        for row in range(9):
            for col in range(9):

                if board[row][col]==".":
                    for val in "123456789":
                        if isvalid(val, row, col, board):
                            board[row][col]=val
                            if (main(board)): return True
                            board[row][col]="."
                    
                    return False
                
        for row in board:
            print(" ".join(row))
        return True
    
    for row in board:
            print(" ".join(row))
    return main(board)

print(sudoku(board))


    