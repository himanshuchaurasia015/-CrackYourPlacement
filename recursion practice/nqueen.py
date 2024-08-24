class Solution:
    def solveNQueens(self, n: int):
        def isSafe(r,c,board):
            if c==0:
                return True
            i=r
            j=c
            while(i>=0 and j>=0):
                if board[i][j]=="Q": return False
                i-=1
                j-=1
            i=r
            j=c
            while(j>=0):
                if board[i][j]=="Q": return False
                j-=1
            i=r
            j=c
            while(i<n and j<n):
                if board[i][j]=="Q": return False
                i+=1
                j-=1
            return True


        def solve(j,board,res,n):
            if j==n:
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                if isSafe(i,j,board):
                    board[i][j]="Q"
                    solve(j+1,board,res,n)
                    board[i][j]="."
                
        arr=["."]*n
        board=[arr.copy() for i in range(n)]
        res=[]
        solve(0,board,res,n)
        return res



        