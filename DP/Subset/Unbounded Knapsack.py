# You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.



# You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.



# Example:
# Input: 
# 'n' = 3, 'w' = 10, 
# 'profit' = [5, 11, 13]
# 'weight' = [2, 4, 6]

# Output: 27

# Explanation:
# We can fill the knapsack as:

# 1 item of weight 6 and 1 item of weight 4.
# 1 item of weight 6 and 2 items of weight 2.
# 2 items of weight 4 and 1 item of weight 2.
# 5 items of weight 2.

# The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.


# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 3 15
# 7 2 4
# 5 10 20

# Expected Answer:
# 21


# Output on console:
# 21


# Explanation of Sample Input 1
# The given knapsack capacity is 15. We can fill the knapsack as [1, 1, 1] giving us profit 21 and as [1,2] giving us profit 9. Thus maximum profit will be 21.


# Sample Input 2
# 2 3
# 6 12
# 4 17


# Expected Answer:
# 0


# Output on console:
# 0


# Explanation of Sample Input 2:
# We can clearly see that no item has weight less than knapsack capacity. Therefore we can not fill knapsack with any item.


# Expected Time Complexity:
# Try to solve this in O(n*w).


# Constraints
# 1 <= n <= 10^3
# 1 <= w <= 10^3
# 1 <= profit[i] , weight[i] <= 10^8

# Time Limit: 1 sec

# ----------------------------------------Memoization-----------------------


from typing import List

def unboundedKnapsack(n: int, W: int, profit: List[int], weight: List[int]) -> int:
    # write your code here
    def solve(i,W,weight,profit,dp):
        if i==0:
            if (W%weight[0]==0):
                # suppose we have w=5 when i==0 and weight[0]==1 and profit[0]=5
                # then we can take that item 5 times therefor profit will be 5*profit[0]
                return (W//weight[0])*profit[0]
            return 0
        if dp[i][W]!=-1:
                return dp[i][W]
        plus,minus=0,0
        if weight[i]<=W:
            plus=solve(i,W-weight[i],weight,profit,dp)+profit[i]
        minus=solve(i-1,W,weight,profit,dp)
        dp[i][W]= max(plus,minus)
        return dp[i][W]
    dp=[[-1]*(W+1) for i in range(n)]
    return solve(len(weight)-1,W,weight,profit,dp)


# ----------------------------------------tabulation-----------------------------------
    dp=[[0]*(W+1) for i in range(n)]
    for i in range(weight[0],W+1):
        dp[0][i]=(i//weight[0])*profit[0]
    for i in range(1,n):
        for w in range(W+1):
            plus=0
            if weight[i]<=w:
                plus=dp[i][w-weight[i]]+profit[i]
            minus=dp[i-1][w]
            dp[i][w]= max(plus,minus)
    return dp[n-1][W]
# -------------------------------------------------optimized space----------------------

    dp=[0]*(W+1)
    curr=[0]*(W+1)

    for i in range(weight[0],W+1):
        dp[i]=(i//weight[0])*profit[0]

    for i in range(1,n):
        for w in range(W+1):
            plus=0
            if weight[i]<=w:
                plus=curr[w-weight[i]]+profit[i]
            minus=dp[w]
            curr[w]= max(plus,minus)
        dp=curr
    return dp[W]
