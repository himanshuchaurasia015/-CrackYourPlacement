

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# Example 2:

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

# Constraints:

# 1 <= k <= 100
# 1 <= prices.length <= 1000
# 0 <= prices[i] <= 1000

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def solve(i,buy,prices,cap,dp):
            if cap==0:
                return 0
            if i==len(prices):
                return 0
            if dp[buy][cap][i]!=-1:
                return dp[buy][cap][i]
            if buy:
                a=-prices[i]+solve(i+1,0,prices,cap,dp)
                b=0+solve(i+1,1,prices,cap,dp)
                dp[buy][cap][i]= max(a,b)
            else:
                a=prices[i]+solve(i+1,1,prices,cap-1,dp)
                b=0+solve(i+1,0,prices,cap,dp)
                dp[buy][cap][i]= max(a,b)
            return dp[buy][cap][i]
        dp = [[[-1] * len(prices) for _ in range(k+1)] for _ in range(2)]
        return solve(0,1,prices,k,dp)

       