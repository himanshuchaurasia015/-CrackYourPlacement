class Solution:
    def exist(self, board, s):
        def check(i,j):
            return (0<=i<len(board)) and (0<=j<len(board[0]))
        def iterate(i,j,index):
            if index==len(s):
                return True
            if (not check(i,j)) or board[i][j]!=s[index]:
                return False
            temp=board[i][j]
            board[i][j]=""
            if iterate(i-1,j,index+1) or iterate(i,j+1,index+1) or iterate(i,j-1,index+1) or iterate(i+1,j,index+1):
                return True
            board[i][j]=temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==s[0] and iterate(i,j,0):
                    return True
        return False
                


        