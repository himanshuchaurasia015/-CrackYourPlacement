# Problem statement
# A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= N <= 10^2
# 1<= wi <= 50
# 1 <= vi <= 10^2
# 1 <= W <= 10^3

# Time Limit: 1 second
# Sample Input:
# 1 
# 4
# 1 2 4 5
# 5 4 8 6
# 5
# Sample Output:
# 13

# ------------------------------memoization.py-----------------------------------
def solve(i,W,wi,v,dp):
    if W<=0:
        return 0
    if i<0:
        return 0
    if dp[i][W]!=-1:
        return dp[i][W]
    take=0
    if wi[i]<=W: take=solve(i-1,W-wi[i],wi,v,dp)+v[i]
    nttake=solve(i-1,W,wi,v,dp)
    dp[i][W]= max(take,nttake)
    return dp[i][W]

# -----------------------------tabulation------------------------

def solve(i,W,wi,v,dp):
    dp=[[0]*(W+1) for i in range(n)]
    for w in range(wi[0],W+1): dp[0][w]=v[0]
    for i in range(1,n):
        for j in range(W+1): 
            take=0
            if wi[i]<=j:
                take=dp[i-1][j-wi[i]]+v[i]
            nttake=0+dp[i-1][j]
            dp[i][j]= max(take,nttake)
    return dp[n-1][W]


t=int(input())
while(t):
    n=int(input())
    wi=list(map(int,input().split()))
    v=list(map(int,input().split()))
    W=int(input())
    dp=[[-1]*(W+1) for i in range(n)]
    print(solve(n-1,W,wi,v,dp))
    t-=1
