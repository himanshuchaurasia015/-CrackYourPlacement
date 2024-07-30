class Solution:
    def subarraysDivByK(self, nums, k):
        summ=0
        count=0
        d={}
        for i in nums:
            summ+=i
            if summ%k==0:
                count+=1
            if summ%k in d:
                count+=d[summ%k]
                d[summ%k]+=1
            else:
                d[summ%k]=1
        return count




        