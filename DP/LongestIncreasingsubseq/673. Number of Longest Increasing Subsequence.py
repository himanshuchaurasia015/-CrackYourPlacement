# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

# Constraints:

# 1 <= nums.length <= 2000
# -106 <= nums[i] <= 106
# The answer is guaranteed to fit inside a 32-bit integer.


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        index=-1
        cnt=[1]*n
        maxi=0
        for i in range(n):
            for prev in range(i):
                
                if nums[i]>nums[prev] and (dp[prev]+1>dp[i]):

                    dp[i]=1+dp[prev]
                    # inherit previous count of sequence
                    cnt[i]=cnt[prev]
                    # if len of seq are equal then add count of both seq
                elif nums[i]>nums[prev] and (dp[prev]+1==dp[i]):
                    # increase count
                    cnt[i]+=cnt[prev]

            if maxi<dp[i]:
                maxi=dp[i]
        num=0
        for i in range(n):
            if dp[i]==maxi:
                num+=cnt[i]
        return num
        