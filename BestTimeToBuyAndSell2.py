class Solution:
    def maxProfit(self, prices):
        curr=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if curr<prices[i]:
                profit+=prices[i]-curr
                curr=prices[i]
            else:
                curr=prices[i]
        return profit