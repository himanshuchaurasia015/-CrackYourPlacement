class Solution:
    def longestCommonPrefix(self, strs):
        s=sorted(strs)       
        f=s[0]
        l=s[-1]
        res=""
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                return res
            res+=f[i]
        return res