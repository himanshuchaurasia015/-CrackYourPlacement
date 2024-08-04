class Solution:
    def canJump(self, nums):
        n=len(nums)
        maxx=nums[0]
        for i in range(n):
            if maxx<0:
                return False
            elif maxx<nums[i]:
                maxx=nums[i]
            maxx-=1
        return True
            


            
            

        