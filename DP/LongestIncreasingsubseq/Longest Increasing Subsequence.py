# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

 

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
 

# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?



# ---------------------------MEMOIZATION==============================

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Helper recursive function to solve the problem
        def solve(i, prev_index, nums, dp):
            if i == len(nums):  # Base case: if index goes beyond the array length
                return 0
            if dp[i][prev_index + 1] != -1:  # Return memoized result if available
                return dp[i][prev_index + 1]
            
            # Option to include nums[i] if it's greater than the previous element
            include = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                include = 1 + solve(i + 1, i, nums, dp)
            
            # Option to skip nums[i]
            exclude = solve(i + 1, prev_index, nums, dp)
            
            # Store and return the best of the two options
            dp[i][prev_index + 1] = max(include, exclude)
            return dp[i][prev_index + 1]
        
        # Initialize the dp array with -1 (extra dimension to handle prev_index = -1)
        dp = [[-1 for _ in range(len(nums) + 1)] for _ in range(len(nums))]
        
        # Start solving from the first element with prev_index set to -1 (no previous element)
        # return solve(0, -1, nums, dp)
        n=len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev_index in range(i-1,-2,-1):
                include = 0
                if prev_index == -1 or nums[i] > nums[prev_index]:
                    include = 1 + dp[i + 1][i+1]
                
                # Option to skip nums[i]
                exclude = solve[i + 1][prev_index+1]
                
                # Store and return the best of the two options
                dp[i][prev_index + 1] = max(include, exclude)
        print(dp)
        return 0
# ------------------------------tabulation-----------------------------
        dp = [[0 for _ in range(len(nums) + 1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)-1,-1,-1):
            for prev_index in range(i-1,-2,-1):
                include = 0
                if prev_index == -1 or nums[i] > nums[prev_index]:
                    include = 1 + dp[i + 1][i+1]
                
                # Option to skip nums[i]
                exclude = dp[i + 1][prev_index+1]
                
                # Store and return the best of the two options
                dp[i][prev_index + 1] = max(include, exclude)      
        return dp[0][0]
    
# ----------------------optimized---------------------------------
        dp = [1 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            for prev in range(i):
                if nums[prev]<nums[i]:
                    dp[i]=max(1+dp[prev],dp[i])
        return max(dp)
    


# ---------------------------using binary search---------------------------------
import bisect
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        # code here
        ans=[a[0]]
        for i in range(1,n):
            if a[i]>ans[-1]:
                ans.append(a[i])
            else:
                # using binary search to find index where we can insert it a[i]
                x=bisect.bisect_left(ans,a[i])
                ans[x]=a[i]
        return len(ans)