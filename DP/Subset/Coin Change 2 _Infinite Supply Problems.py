# Problem statement
# You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}. You need to figure out the total number of ways W, in which you can make a change for value V using coins of denominations from D. Print 0, if a change isn't possible.

# Detailed explanation ( Input/output format, Notes, Images )

# Sample Input 1 :
# 3
# 1 2 3
# 4
# Sample Output 1:
# 4
# Explanation for Sample Output 1:
# We can make a change for the value V = 4 in four ways.
# 1. (1,1,1,1), 
# 2. (1,1, 2), [One thing to note here is, (1, 1, 2) is same as that of (2, 1, 1) and (1, 2, 1)]
# 3. (1, 3), and 
# 4. (2, 2)
# Sample Input 2 :
# 3
# 5 3 2
# 1
# Sample Output 2:
# 0


# ---------------------------------memoization---------------------------
def countWaysToMakeChange(denominations, value) :
    
	# Your code goes here
    def solve(i,value,arr,dp):
        if i==0:
            if value%arr[0]==0:
                return 1
            return 0
        if dp[i][value]!=-1:
            return dp[i][value]
        take=0
        if arr[i]<=value:
            take=solve(i,value-arr[i],arr,dp)
        nottk=solve(i-1,value,arr,dp)
        dp[i][value]=take+nottk
        return dp[i][value]
    dp=[[-1]*(value+1) for i in range(len(denominations))]
    return solve(len(denominations)-1,value,denominations,dp)

# --------------------------------------tabulation--------------------------------

    dp=[[0]*(value+1) for i in range(len(arr))]
    for i in range(value+1):
        if i%arr[0]==0:
            dp[0][i]=1
    for i in range(1,len(arr)):
        for j in range(value+1):
            take=0
            if arr[i]<=j:
                take=dp[i][j-arr[i]]
            nottk=dp[i-1][j]
            dp[i][j]=take+nottk
    return dp[len(arr)-1][value]


# -------------------space optimized----------------------

    dp=[0]*(value+1)
    curr=[0]*(value+1)
    for i in range(value+1):
        if i%arr[0]==0:
            dp[i]=1
    for i in range(1,len(arr)):
        for j in range(value+1):
            take=0
            if arr[i]<=j:
                take=curr[j-arr[i]]
            nottk=dp[j]
            curr[j]=take+nottk
        dp=curr
    return dp[value]