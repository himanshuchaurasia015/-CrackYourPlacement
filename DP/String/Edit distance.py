# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.



class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        def solve(i,j,w1,w2,dp):
            if j<0: 
                #IF W2 IS EXHAUSTED AND WE STILL HAVE CHARACTER
                # SO WE HAVE TO PERFORM REMOVE OPERATION i+1 TIMES
                return i+1
            if i<0:
                #IF W1 IS EXHAUSTED AND WE STILL want CHARACTERS TO CREATE W2
                # SO WE HAVE TO PERFORM INSERT OPERATION j+1 TIMES
                return j+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if w1[i]==w2[j]:
                dp[i][j]= solve(i-1,j-1,w1,w2,dp)
            else:
                a=solve(i-1,j,w1,w2,dp)+1   #DELETE
                b=solve(i-1,j-1,w1,w2,dp)+1 #REPLACE
                c=solve(i,j-1,w1,w2,dp)+1   #INSERT
                dp[i][j]= min(a,b,c)
            return dp[i][j]
        dp=[[-1]*(len(w2)+1) for i in range(len(w1)+1)]
        return solve(len(w1)-1,len(w2)-1,w1,w2,dp)
    
# ----------------------tabulation-------------------------

        dp=[[0]*(len(w2)+1) for i in range(len(w1)+1)]
        # return solve(len(w1)-1,len(w2)-1,w1,w2,dp)
        for i in range(len(w2)+1): dp[0][i]=i
        for i in range(len(w1)+1): dp[i][0]=i
        for i in range(1,len(w1)+1):
            for j in range(1,len(w2)+1):
                if w1[i-1]==w2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    a=dp[i-1][j]+1
                    b=dp[i-1][j-1]+1
                    c=dp[i][j-1]+1
                    dp[i][j]= min(a,b,c)
        return dp[len(w1)][len(w2)]