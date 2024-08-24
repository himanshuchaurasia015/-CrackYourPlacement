class Solution:
    def permute(self, nums):
        def solve(nums,i,res,m={},sub=[]):
            if len(sub)==len(nums):
                res.append(sub.copy())
                return
            for j in range(len(nums)):
                if (j not in m) or (m[j]==0):
                    sub.append(nums[j])
                    m[j]=1
                    solve(nums,j+1,res,m,sub)
                    m[j]=0
                    sub.pop()
        res=[]
        solve(nums,0,res)
        return res

class Solution:
    def permute(self, nums):
        def solve(nums,i,res):
            if i==len((nums)):
                res.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                solve(nums,i+1,res)
                nums[j],nums[i]=nums[i],nums[j]
        res=[]
        solve(nums,0,res)
        return res

a=Solution()
a.permute([1,2,3])