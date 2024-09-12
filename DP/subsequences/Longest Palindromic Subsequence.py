# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str2=list(s)
        str2.reverse()
        str2="".join(str2)
        dp=[[0]*(len(str2)+1) for i in range(len(s)+1)]
        maxx=0
        for i in range(1,len(s)+1):
            for j in range(1,len(str2)+1):
                if s[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(s)][len(str2)]