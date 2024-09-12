# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(i,j,t1,t2,dp):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            res=0
            if t1[i]==t2[j]:
                res= solve(i-1,j-1,t1,t2,dp)+1
            else:
                a=solve(i-1,j,t1,t2,dp)
                b=solve(i,j-1,t1,t2,dp)
                res=max(a,b)
            dp[i][j]=res
            return res
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for i in range(n)]
        return solve(n-1,m-1,text1,text2,dp)