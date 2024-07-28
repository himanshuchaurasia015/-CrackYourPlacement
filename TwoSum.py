class Solution:
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in d:
                return [i,d[val]]
            d[nums[i]]=i