# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

# Constraints:

# 1 <= s.length <= 500
# s consists of lowercase English letters.



class Solution:
    def minInsertions(self, s: str) -> int:
        s1=list(s)
        s1.reverse()
        s1="".join(s1)
        dp=[[-1]*(len(s)+1) for i in range(len(s)+1)]
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
        return len(s)-solve((len(s))-1,(len(s))-1,s,s1,dp)