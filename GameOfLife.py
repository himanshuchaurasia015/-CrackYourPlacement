class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        res=[]
        for i in board:
            arr=[]
            for j in i:
                arr.append(j)
            res.append(arr)
        def check(a,b):
            if 0<=a<m and 0<=b<n:
                return True
            else:
                return False

        for i in range(m):
            for j in range(n):
                count=0
                a,b=i-1,j
                if check(a,b) and res[a][b]: count+=1
                a,b=i+1,j
                if check(a,b) and res[a][b]: count+=1   
                a,b=i-1,j-1
                if check(a,b) and res[a][b]: count+=1 
                a,b=i+1,j+1
                if check(a,b) and res[a][b]: count+=1 
                a,b=i,j+1
                if check(a,b) and res[a][b]: count+=1  
                a,b=i,j-1
                if check(a,b) and res[a][b]: count+=1  
                a,b=i+1,j-1
                if check(a,b) and res[a][b]: count+=1  
                a,b=i-1,j+1
                if check(a,b) and res[a][b]: count+=1  
                if count<2 or  count>3:
                    board[i][j]=0
                if count==3:
                    board[i][j]=1
                