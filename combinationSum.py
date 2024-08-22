
# Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 

# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def solve(arr,curr,index,n,res,sub=[]):
            if curr>target or index>=n :
                return
            elif sub in res:
                return
            elif curr==target :
                res.append(sub.copy())
                return

            for i in range(index,n):
                curr+=arr[i]
                sub.append(arr[i])
                solve(arr,curr,i,n,res,sub)
                curr-=sub.pop()
                if i+1>n and curr+arr[i+1]<=target:
                    solve(arr,curr,i+1,n,res,sub)
        curr=0
        res=[]
        solve(arr,curr,0,len(arr),res)
        return res
    
    # <--------------------------------------------------solution 2---------------------------------------------------->

class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        def solve(arr,curr,index,n,res,sub=[]):
            if index==n:
                if curr==0:
                    res.append(sub.copy())
                    return
                return
            if curr>0:
                curr-=arr[index]
                sub.append(arr[index])
                solve(arr,curr,index,n,res,sub)
                curr+=sub.pop()
            solve(arr,curr,index+1,n,res,sub)
        curr=0
        res=[]
        solve(arr,target,0,len(arr),res)
        return res
            
