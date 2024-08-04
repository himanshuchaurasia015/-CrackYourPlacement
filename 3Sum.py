
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res=[]
        n= len(nums)
        for i in range(n):
            target=nums[i]
            if i>0 and target==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                tsum=nums[l]+nums[r]+target
                if tsum<0:
                    l+=1
                elif tsum>0:
                    r-=1
                else:
                    res.append([target,nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
        return res


                    


            


                            

        
                   
                
                
                
            
                
            
        