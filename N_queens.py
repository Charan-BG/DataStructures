"""
Coding Exercise: N Queen
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""
# TC=O(n!) SC=O(n^2)
def N_Queen(n):
    res=[]
    board=[['.']*n for _ in range(n)]

    def jointherow(board):
        return [''.join(row) for row in board]

    def is_vaild(row, col, board):
        
        #col check
        for x in range(row):
            if board[x][col]=='Q': 
                return False
            
        #top left diagonal check
        for r,c in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[r][c]=='Q':
                return False

        #top right diagonal check
        for r,c in zip(range(row, -1, -1), range(col, n)):
            if board[r][c]=='Q':
                return False
            
        return True


    def main(board, row):

        if row==n:
            res.append(jointherow(board))
            return
        
        for col in range(n):
            if is_vaild(row, col, board):
                board[row][col]='Q'
                main(board, row+1)
                board[row][col]="."
        

    main(board, 0)
    return res

print(N_Queen(6))