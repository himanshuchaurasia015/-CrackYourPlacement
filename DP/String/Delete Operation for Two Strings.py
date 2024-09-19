# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

 

# Example 1:

# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Example 2:

# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
 

# Constraints:

# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.


class Solution:
    def minDistance(self, s1: str, s: str) -> int:
        dp=[[-1]*(len(s1)+1) for i in range(len(s)+1)]
        def solve(i,j,s,s1,dp):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s1[j]:
                dp[i][j]= solve(i-1,j-1,s,s1,dp)+1
            else:
                dp[i][j]= max(solve(i-1,j,s,s1,dp),solve(i,j-1,s,s1,dp))
            return dp[i][j]
        ans=solve(len(s)-1,len(s1)-1,s,s1,dp)
        return len(s1)+len(s)-2*ans
