class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(nums,i,res,sub=[]):
            res.append(sub.copy())
            for j in range(i,len(nums)):
                if j!=i and nums[j]==nums[j-1]:
                    continue
                sub.append(nums[j])
                solve(nums,j+1,res,sub)
                sub.pop()
        res=[]
        nums.sort()
        solve(nums,0,res)
        return res