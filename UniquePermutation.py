#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        # # code here 
        # res=[]
        # def permute(index,nums):
        #     if nums in res:
        #         return
        #     if index>=n:
        #         if (nums not in res):
        #             res.append(nums[:])
        #         return
        #     for i in range(index,n):
        #         nums[index],nums[i]=nums[i],nums[index]
        #         permute(index+1,nums)
        #         nums[i],nums[index]=nums[index],nums[i]
        # arr.sort()
        # permute(0,arr)
        # # res.sort()
        # return res
        res = []
        visited = [False] * n
        
        def permute(visited, index, ans, nums):
            if index == n:
                res.append(ans[:])
                return
            
            for j in range(n):
                if not visited[j]:
                    # Ensure no duplicate permutations
                    if j > 0 and nums[j] == nums[j-1] and not visited[j-1]:
                        continue
                    
                    visited[j] = True
                    ans.append(nums[j])
                    permute(visited, index + 1, ans, nums)
                    visited[j] = False
                    ans.pop()
        
        arr.sort()  # Sorting to handle duplicates
        permute(visited, 0, [], arr)
        return res