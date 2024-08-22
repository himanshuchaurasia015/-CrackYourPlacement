class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def check(r,c,v,board):
            for k in range(9):
                if board[r][k]==v:
                    return False
                if board[k][c]==v:
                    return False
                if board[3*(r//3)+k//3][3*(c//3)+k%3]==v:
                    return False
            return True
            
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]==".":
                        for c in range(1,10):
                            if check(i,j,str(c),board):
                                board[i][j]=str(c)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j]="."
                        return False
            return True

        solve(board)


            
                    

        