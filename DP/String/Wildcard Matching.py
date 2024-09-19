# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def solve(i,j,s,p,dp):
            # if both string will exhausted
            if i<0 and j<0:
                return True
            # if s is exhausted but p is not
            if i<0 and j>=0:
                # if p has characters other than "*" then it will return False otherwise False
                for i in range(j+1):
                    if p[i]!="*":
                        return False
                return True
            if i>=0 and j<0:
                return False
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==p[j]  or p[j]=="?":
                dp[i][j]= solve(i-1,j-1,s,p,dp)
            else:
                if p[j]=="*":
                    a=solve(i,j-1,s,p,dp)
                    b= solve(i-1,j,s,p,dp)
                    dp[i][j]= a or b
                else:
                    dp[i][j]= False
            return dp[i][j]
        dp=[[-1]*(len(p)+1) for i in range(len(s)+1)]
        return solve(len(s)-1,len(p)-1,s,p,dp)

        