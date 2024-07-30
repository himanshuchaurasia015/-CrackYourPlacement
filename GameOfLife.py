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
        def countnei(a,b):
            count=0
            for i in range(a-1,a+2):
                for j in range(b-1,b+2):
                    if (i==a and b==j) or i<0 or j<0 or (i==m or j==n):
                        continue
                    if res[i][j]:
                        count+=1
            return count
        for i in range(m):
            for j in range(n):
                count=countnei(i,j)
                if i==1 and j==0:
                    print(count, board[i][j])  
                if count<2 or  count>3:
                    board[i][j]=0
                if count==3:
                    board[i][j]=1

                