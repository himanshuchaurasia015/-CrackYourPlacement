# Problem statement
# Ninja has a 'GRID' of size 'R' X 'C'. 
# Each cell of the grid contains some chocolates. Ninja has two friends Alice and Bob, 
# and he wants to collect as many chocolates as possible with the help of his friends.

# Initially, Alice is in the top-left position i.e. (0, 0), and Bob is in the top-right place i.e. (0, ‘C’ - 1) in the grid.
#  Each of them can move from their current cell to the cells just below them. 
# When anyone passes from any cell, he will pick all chocolates in it, and then the number of chocolates in that cell will become zero.
#  If both stay in the same cell, only one of them will pick the chocolates in it.

# If Alice or Bob is at (i, j) then they can move to (i + 1, j), (i + 1, j - 1) or (i + 1, j + 1).
#  They will always stay inside the ‘GRID’.

# Your task is to find the maximum number of chocolates Ninja can collect with the help of his friends by following the above rules.

# Example:
# Input: ‘R’ = 3, ‘C’ = 4
#        ‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
# Output: 21

# Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and will collect 2 + 4 + 6 = 12 chocolates.

# Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3) and will colllect 2 + 2 + 5 = 9 chocolates.

# Hence the total number of chocolates collected will be 12 + 9 = 21. 
# there is no other possible way to collect a greater number of chocolates than 21.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= ‘T’ <= 10
# 2 <= 'R', 'C' <= 50
# 0 <= 'GRID[i][j]'<= 10^2
# Time Limit: 1sec
# Sample Input 1 :
# 2
# 3 4
# 2 3 1 2
# 3 4 2 2
# 5 6 3 5
# 2 2
# 1 1
# 1 2
# Sample Output 1 :
# 21
# 5
# Explanation Of Sample Input 1 :
# For the first test case, Initially Alice is at the position (0, 0) he can follow the path (0, 0) -> (1, 1) -> (2, 1) and will collect 2 + 4 + 6 = 12 chocolates.

# Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1, 3) -> (2, 3) and will collect 2 + 2 + 5 = 9 chocolates.

# Hence the total number of chocolates collected will be 12 + 9 = 21.

# For the second test case, Alice will follow the path (0, 0) -> (1, 0) and Bob will follow the path (0, 1) -> (1, 1). 
# total number of chocolates collected will be 1 + 1 + 1 + 2 = 5
# Sample Input 2 :
# 2
# 2 2
# 3 7
# 7 6
# 3 2
# 4 5
# 3 7
# 4 2
# Sample Output 2 :
# 23
# 25








def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    def solve(i,j,l,grid,r,c,dp):
        if j<0 or j>=c or l<0 or l>=c:
            return 0
        if i==r-1:
            if j==l:
                return grid[r-1][j]
            return grid[r-1][j]+grid[r-1][l]
        if dp[i][j][l]!=-1:
            return dp[i][j][l]
        cost1=-10e9
        for x in range(-1,2):
            
            for y in range(-1,2):
                ux=-10e9
                if j+x==l+y:
                    ux=solve(i+1,j+x,l+y,grid,r,c,dp)+grid[i][j]
                else:
                    ux=solve(i+1,j+x,l+y,grid,r,c,dp)+grid[i][j]+grid[i][l]

                cost1=max(ux,cost1)
        dp[i][j][l]=cost1
        return cost1
    a=0
    dp=[[[-1 for h in range(c)] for k in range(c)] for i in range(r)]
    a=solve(0,0,c-1,grid,r,c,dp)
    return a

# -------------------------------------tabulation-----------------------------------------
    dp=[[[0 for h in range(c)] for k in range(c)] for i in range(r)]
    for j1 in range(c):
        for j2 in range(c):
            if j1==j2:
                dp[r-1][j1][j2]=grid[r-1][j2]
            else:
                dp[r-1][j1][j2]=grid[r-1][j2]+grid[r-1][j1]
    for i in range(r-2,-1,-1):
        for j in range(c):
            for l in range(c):
                cost1=-10e9
                for x in range(-1,2):
                    for y in range(-1,2):
                        ux=-10e9
                        if j==l:
                            ux=grid[i][j]
                        else:
                            ux=grid[i][j]+grid[i][l]
                        if 0<=j+x<c and 0<=l+y<c:
                            ux+=dp[i+1][j+x][l+y]
                        else:
                            ux=-float("inf")
                        cost1=max(ux,cost1)
                dp[i][j][l]=cost1
    return dp[0][0][-1]