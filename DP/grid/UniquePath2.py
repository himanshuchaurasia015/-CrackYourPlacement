# Given a ‘N’ * ’M’ maze with obstacles, count and
#  return the number of unique paths to reach the right-bottom cell from the top-left cell.
#  A cell in the given maze has a value '-1' if it is a blockage or dead-end, else 0.
#  From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.
#  Since the answer can be large, print it modulo 10^9 + 7.

# For Example :
# Consider the maze below :
# 0 0 0 
# 0 -1 0 
# 0 0 0

# There are two ways to reach the bottom left corner - 

# (1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
# (1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)

# Hence the answer for the above test case is 2.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= N,M <= 200

# Note: It is guaranteed that the top-left cell does not have an obstacle.

# Time Limit: 1 sec
# Sample Input 1 :
# 2    
# 2 2
# 0 0
# 0 0
# 3 3
# 0 0 0 
# 0 -1 0 
# 0 0 0
# Sample Output 1 :
# 2
# 2
# Explanation For Sample Output 1 :
# For the first test case, there are two possible paths to reach (2, 2) from (1, 1) : 
#     (1, 1) -> (1, 2) -> (2, 2)
#     (1, 1) -> (2, 1) -> (2, 2)

# For the second test case, there are two ways to reach the bottom left corner - 
# (1, 1) -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 3)
# (1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (3, 3)
# Sample Input 2 :
# 1
# 2 2
# 0 -1
# -1  0
# Sample Output 2 :
# 0




def mazeObstacles(n, m, mat):
    # Write your code here.
    def solve(i,j,mat,dp,):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==0 and j==0:
            return 1
        if i<0 or j<0:
            return 0
        if mat[i][j]==-1:
            return 0

        l,u=0,0
        if j>0  :
            l=solve(i,j-1,mat,dp,)
        if i>0 :
            u=solve(i-1,j,mat,dp,)
        dp[i][j]=l+u
        return dp[i][j]
    dp= [[-1]*m for i in range(n)]
    return (solve(n-1,m-1,mat,dp,))%(10**9+7)
# --------------------------------Tabulation======================
    for i in range(n):
        for j in range(m):
            if mat[i][j]==-1:
                dp[i][j]=0
            elif i==0 and j==0:
                dp[i][j]=1
            else:
                l,u=0,0
                if i>0: l=dp[i-1][j]
                if j>0: u=dp[i][j-1]
                dp[i][j]=u+l
    return dp[n-1][m-1]%(10**9+7)
# -----------------------------------space optimized---------------------------
    dp=[0]*m
    for i in range(n):
        temp=[0]*m
        for j in range(m):
            if mat[i][j]==-1:
                temp[j]=0
            elif i==0 and j==0:
                temp[j]=1
            else:
                l,u=0,0
                if i>0: u=dp[j]
                if j>0: l=temp[j-1]
                temp[j]=u+l
        dp=temp
    return dp[-1]%(10**9+7)




