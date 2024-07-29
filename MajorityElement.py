class Solution:
    def majorityElement(self, nums):
        s=set(nums)
        d={}
        for i in s:
            d[i]=nums.count(i)
        ele=0
        maxx=0
        for a,b in d.items():
            if b>maxx:
                maxx=b
                ele=a
        return ele