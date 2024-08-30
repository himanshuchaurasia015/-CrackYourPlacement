# Smallest window in a string containing all the characters of another string
# Difficulty: HardAccuracy: 30.19%Submissions: 140K+Points: 8
# Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
# Note : All characters are in Lowercase alphabets. 

# Example 1:

# Input:
# S = "timetopractice"
# P = "toc"
# Output: 
# toprac
# Explanation: "toprac" is the smallest
# substring in which "toc" can be found.
# Example 2:

# Input:
# S = "zoomlazapzo"
# P = "oza"
# Output: 
# apzo
# Explanation: "apzo" is the smallest 
# substring in which "oza" can be found.
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index. 

# Expected Time Complexity: O(|S|)
# Expected Auxiliary Space: O(n) n = len(p)

 

# Constraints: 
# 1 ≤ |S|, |P| ≤ 105




# bruteforce
from collections import defaultdict

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        st=0
        minlen=float("inf")
        for i in range(len(s)):
            d=defaultdict(int)
            count=0
            for k in p:
                d[k]+=1
            for j in range(i,len(s)):
                if d[s[j]]>0: count+=1
                d[s[j]]-=1
                if count==len(p):
                    if j-i+1<minlen:
                        minlen=j-i+1
                        st=i
                        break
        return s[st:minlen+st]
    
# -------------------------------------optimal----------------------------------------



    def smallestWindow(self, s, p):
        #code here
        l=0
        r=0
        count=0
        d=defaultdict(int)
        for i in p:
            d[i]+=1
        st=-1
        minlen=float("inf")
        while(r<len(s)):
            if d[s[r]]>0: count+=1
            d[s[r]]-=1
            while l <= r and count==len(p):
                if r-l+1<minlen or (r-l+1==minlen and l<st ):
                    minlen=r-l+1
                    st=l
                d[s[l]]+=1
                if d[s[l]]>0: count-=1
                l+=1
            r+=1
            
        return s[st:minlen+st] if st!=-1 else -1