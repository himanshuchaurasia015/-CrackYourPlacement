class Solution:
    def fourSum(self, nums, target):
        n= len(nums)
        nums.sort()
        res=[]
        for i,v in enumerate(nums):
            for j in range(i+1,n):
                t=nums[j]
                l=j+1
                r=n-1
                while(l<r):
                    fsum=v+t+nums[l]+nums[r]
                    if fsum>target:
                        r-=1
                    elif fsum<target:
                        l+=1
                    else:
                        if [v,t,nums[l],nums[r]] not in res: res.append([v,t,nums[l],nums[r]])
                        l+=1
                        
        return res

