# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0
 

# Constraints:

# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(i,buy,prices,dp):
            if i>=len(prices): return 0
            if dp[buy][i]!=-1:
                return dp[buy][i]
            if buy==0:
                a=-prices[i]+solve(i+1,1,prices,dp)
                b=0+solve(i+1,0,prices,dp)
                dp[buy][i]= max(a,b)
            else:
                a=prices[i]+solve(i+2,0,prices,dp)
                b=0+solve(i+1,1,prices,dp)
                dp[buy][i]= max(a,b)
            return dp[buy][i]
        dp = [[-1] * len(prices) for _ in range(2)]
        return solve(0,0,prices,dp)