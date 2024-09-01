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
            # count denotes the no. of elements of p in current substring of s
            count=0
            # storing count of all elements of p
            for k in p:
                d[k]+=1
            for j in range(i,len(s)):
                # incrementing the value of count whenever s[j] in p or count of s[j] in d >0
                if d[s[j]]>0: count+=1
                # it will decrement the value of d[s[j]]
                d[s[j]]-=1
                # when the count is equal to length of p compare with prev substring length 
                # and store min length of string and strating index
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
        # count denotes the no. of elements of p in current substring of s
        count=0
        d=defaultdict(int)
            # storing count of all elements of p
        for i in p:
            d[i]+=1
        st=-1
        minlen=float("inf")
        while(r<len(s)):
                # incrementing the value of count whenever s[j] in p occurs or count of s[j] in d >0
            if d[s[r]]>0: count+=1
                # it will decrement the value of d[s[j]]
            d[s[r]]-=1
            # whenever we got a substring which contains all elements of p 
            # then starts finding smallest len by decreasing the l pointer 
            # till count of elements of p become<len(p)
            while l <= r and count==len(p):
                # when the count is equal to length of p compare with prev substring length 
                # and store min length of string and strating index
                if r-l+1<minlen or (r-l+1==minlen and l<st ):
                    minlen=r-l+1
                    st=l
                # As r pointer had decreased the value of all d[s[l]] 
                # so whever it find a elements of p in substring it will increment the d[s[l]]
                # 
                d[s[l]]+=1
                if d[s[l]]>0: count-=1
                l+=1
            r+=1
            
        return s[st:minlen+st] if st!=-1 else -1