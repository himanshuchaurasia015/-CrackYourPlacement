class Solution:
    def findDuplicates(self, nums):
        d={}
        temp=[]
        for i in nums:
            if i in d:
                temp.append(i)
            else:
                d[i]=1
        return temp
        
        