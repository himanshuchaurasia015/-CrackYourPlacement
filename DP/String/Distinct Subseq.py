# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

 

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
 

# Constraints:

# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.


class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        def solve(i,j,s,t,d={}):
            if j<0: return 1
            if i<0: return 0
            if (i,j) in d:
                return d[(i,j)]
            if s[i]==t[j]:
                d[(i,j)]=solve(i-1,j-1,s,t,d)+solve(i-1,j,s,t,d)
            else:
                d[(i,j)]=solve(i-1,j,s,t,d)
            return d[(i,j)]
        return solve(len(s)-1,len(t)-1,s,t)
 
    def numDistinct(self, s: str, t: str) -> int:
        def solve(i,j,s,t,dp):
            if j<0: return 1
            if i<0: return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]=solve(i-1,j-1,s,t,dp)+solve(i-1,j,s,t,dp)
            else:
                dp[i][j]=solve(i-1,j,s,t,dp)
            return dp[i][j]
        dp=[[-1]*len(t) for i in range(len(s))]
        return solve(len(s)-1,len(t)-1,s,t,dp)


# -------------------------tabulation-------------------------------
        dp=[[0]*(len(t)+1) for i in range(len(s)+1)]
        for i in range(len(s)):
            if s[i]==t[0]:
                dp[i][0]=1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]