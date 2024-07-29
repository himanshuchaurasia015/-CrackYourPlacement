class Solution:
    def subarraySum(self, nums, k):
        n=len(nums)
        count=0
        summ=0
        d={0:1}
        for i in range(n):
            summ+=nums[i]
            if summ-k in d:
                count+= d[summ-k]
            if summ not in d:
                d[summ]=1
            else:
                d[summ]+=1
        return count