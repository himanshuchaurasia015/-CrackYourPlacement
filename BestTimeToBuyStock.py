class Solution:
    def maxProfit(self, prices):
        minp=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if minp<prices[i]:
                p=prices[i]-minp
                if p>profit:
                    profit=p
            else:
                minp=prices[i]
        return profit
            

        

        