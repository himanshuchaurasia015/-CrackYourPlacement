
# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

 

# Example 1:

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# Example 2:

# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# Example 3:

# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Helper function to check if w2 is a valid predecessor of w1
        def check(w1, w2):
            if len(w1) != len(w2) + 1: 
                return False
            x, y = 0, 0
            # Two-pointer comparison to check if w2 is a subsequence of w1
            while x < len(w1) and y < len(w2):
                if w1[x] == w2[y]:
                    y += 1
                x += 1
            # w2 is valid if we've matched all characters in w2
            return y == len(w2)
        
        n = len(words)
        dp = [1] * n  # Initialize dp array
        maxi = 0  # Track the maximum chain length
        
        # Sort words by length to ensure correct sequence of predecessors
        words.sort(key=len)
        
        # Iterate through each word
        for i in range(n):
            w1 = words[i]
            # Compare w1 with all previous words to check for valid predecessors
            for prev in range(i):
                w2 = words[prev]
                if check(w1, w2) and dp[prev] + 1 > dp[i]:
                    dp[i] = dp[prev] + 1
            # Update the maximum chain length
            maxi = max(maxi, dp[i])
        
        return maxi
