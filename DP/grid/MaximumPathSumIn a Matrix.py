# You have been given an N*M matrix filled with integer numbers, find the maximum sum that can be obtained from a path starting from any cell in the first row to any cell in the last row.

# From a cell in a row, you can move to another cell directly below that row, or diagonally below left or right. So from a particular cell (row, col), we can move in three directions i.e.

# Down: (row+1,col)
# Down left diagonal: (row+1,col-1)
# Down right diagonal: (row+1, col+1)
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 50
# 1 <= N <= 100
# 1 <= M <= 100
# -10^4 <= matrix[i][j] <= 10^4

# Where 'T' is the number of test cases.
# Where 'N' is the number of rows in the given matrix, and 'M' is the number of columns in the given matrix.
# And, matrix[i][j] denotes the value at (i,j) cell in the matrix.

# Time Limit: 1sec
# Input 1 :
# 2
# 4 4
# 1 2 10 4
# 100 3 2 1
# 1 1 20 2
# 1 2 2 1
# 3 3
# 10 2 3
# 3 7 2
# 8 1 5
# Output 1 :
# 105
# 25
# Explanation Of Input 1 :
# In the first test case for the given matrix,

# The maximum path sum will be 2->100->1->2, So the sum is 105(2+100+1+2).

# In the second test case for the given matrix, the maximum path sum will be 10->7->8, So the sum is 25(10+7+8).
# Input 2 :
# 2
# 3 3
# 1 2 3
# 9 8 7
# 4 5 6
# 4 6
# 10 10 2 -13 20 4
# 1 -9 -81 30 2 5
# 0 10 4 -79 2 -10
# 1 -5 2 20 -11 4
# Output 2 :
# 17
# 74
# Explanation Of Input 2 :
# In the first test case for the given matrix, the maximum path sum will be 3->8->6, So the sum is 17(3+8+6).

# In the second test case for the given matrix, the maximum path sum will be 20->30->4->20, So the sum is 74(20+30+4+20).


# ------------------------------------memoization-----------------------------------------------
def getMaxPathSum(matrix):

    #   Write your code here
    def solve(i,j,mat,n,m,dp):
        if j<0 or j>=m:
            return -float("inf")
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==0 :
            return mat[0][j]
        u=solve(i-1,j,mat,n,m,dp)+mat[i][j]
        ur=solve(i-1,j+1,mat,n,m,dp)+mat[i][j]
        ul=solve(i-1,j-1,mat,n,m,dp)+mat[i][j]
        cost=max(u,ul,ur)
        dp[i][j]=cost
        return cost
    cost=-float("inf")
    n=len(matrix)
    m=len(matrix[0])
    dp=[[-1 for _ in range(m)] for i in range(n)]
    for i in range(m):
        cost=max(cost,solve(n-1,i,matrix,len(matrix),m,dp))
    return cost

# -----------------------------------------tabulation------------------------------------------

    dp=[[0 for _ in range(m)] for i in range(n)]
    for i in range(m):
        dp[0][i]=matrix[0][i]
    for i in range(1,n):
        for j in range(m):
            u=dp[i-1][j]+matrix[i][j]
            ur=matrix[i][j]
            ul=matrix[i][j]
            if j+1<m:
                ur+=dp[i-1][j+1]
            else:
                ur+=-float("inf")
            if j>0:
                ul+=dp[i-1][j-1]
            else:
                ul+=-float("inf")
            dp[i][j]=max(u,ul,ur)
    maxx=-float("inf")
    for i in range(m):
        maxx=max(maxx,dp[n-1][i])
    return maxx

# ------------------------------------------optimized space---------------------------------

    dp=[0]*m
    for i in range(m):
        dp[i]=matrix[0][i]
    for i in range(1,n):
        temp=[0]*m
        for j in range(m):
            u=dp[j]+matrix[i][j]
            ur=matrix[i][j]
            ul=matrix[i][j]
            if j+1<m:
                ur+=dp[j+1]
            else:
                ur+=-float("inf")
            if j>0:
                ul+=dp[j-1]
            else:
                ul+=-float("inf")
            temp[j]=max(u,ul,ur)
        dp=temp
    return max(dp)