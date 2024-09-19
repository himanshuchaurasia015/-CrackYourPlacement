
# You are given two strings str1 and str2. Your task is to find the length of the longest common substring among the given strings.

# Examples:

# Input: str1 = "ABCDGH", str2 = "ACDGHR"
# Output: 4
# Explanation: The longest common substring is "CDGH" which has length 4.
# Input: str1 = "ABC", str2 = "ACB"
# Output: 1
# Explanation: The longest common substrings are "A", "B", "C" all having length 1.
# Expected Time Complexity: O(n*m).
# Expected Auxiliary Space: O(n*m).

# Constraints:
# 1<= str1.size(), str2.size()<=1000
# Both strings may contain upper and lower case alphabets

class Solution:
    def longestCommonSubstr(self, str1, str2):

        dp=[[0]*(len(str2)+1) for i in range(len(str1)+1)]
        maxx=0
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=0
                maxx=max(dp[i][j],maxx)
        return maxx