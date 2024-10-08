# Problem statement
# Ninjaland is a country in the shape of a 2-Dimensional grid 'GRID', with 'N' rows and 'M' columns. Each point in the grid has some cost associated with it.



# Find a path from top left i.e. (0, 0) to the bottom right i.e. ('N' - 1, 'M' - 1) which minimizes the sum of the cost of all the numbers along the path. You need to tell the minimum sum of that path.



# Note:
# You can only move down or right at any point in time.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 100   
# 1 <= N, M <= 10^2
# 1 <= GRID[i][j] <= 10^5

# Where 'GRID[i][j]' denotes the value of the cell in the matrix.

# Time limit: 1 sec
# Sample Input 1:
# 2
# 2 3
# 5 9 6
# 11 5 2
# 1 1
# 5
# Sample Output 1:
# 21
# 5
# Explanation For Sample Output 1:
# In test case 1, Consider a grid of 2*3:

# For this the grid the path with minimum value is (0,0) -> (0,1) -> (1,1) -> (1,2). And the sum along this path is 5 + 9 +5 + 2 = 21. So the ans is 21.

# In test case 2, The given grid is:

# For this the grid the path with minimum value is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2).The sum along this path is 1 + 2 + 3 + 4 + 9 = 19.
# Sample Input 2:
# 2
# 2 2
# 5 6
# 1 2
# 3 3
# 1 2 3
# 4 5 4
# 7 5 9
# Sample Output 2:
# 8
# 19
# Explanation For Sample Output 2:
# In test case 1, For this the grid the path with minimum value is (0,0) -> (1,0) -> (1,1). The sum along this path is 5 + 1 + 2 = 8.

# In test case 2, The given grid is:

# For this the grid the path with minimum value is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2).The sum along this path is 1 + 2 + 3 + 4 + 9 = 19.

# ----------------------memoization-------------------------------------------

def minSumPath(grid,n,m):
    # Write your code here.
    def solve(i,j, grid, dp):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i==0 and j==0:
            return grid[0][0]
        cost=0
        l,u=0,0
        if j>0: l=solve(i,j-1,grid,dp)
        if i>0: u=solve(i-1,j,grid,dp)
        if l and u:
            cost=min(l,u)
        else:
            cost=max(l,u)
        dp[i][j]= grid[i][j]+cost
        return dp[i][j]
    dp=[[-1]*m for i in range(n)]
    return solve(n-1,m-1, grid, dp)

# ------------------------------Tabulation----------------------------

    dp=[[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j]=grid[i][j]
            else:
                l,u=0,0
                if j>0: l=dp[i][j-1]
                if i>0: u=dp[i-1][j]
                if l and u:
                    cost=min(l,u)
                else:
                    cost=max(l,u)
                dp[i][j]= grid[i][j]+cost
    return dp[n-1][m-1]

# ----------------------------------------Space Optimized--------------------------------------

