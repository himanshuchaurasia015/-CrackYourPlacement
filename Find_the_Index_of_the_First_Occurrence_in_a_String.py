class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index=-1
        if len(needle)>len(haystack):
            return -1
        i=0
        j=len(needle)-1
        while j<len(haystack):
            if needle == haystack[i:j+1]:
                index =i
                break
            i+=1
            j+=1
        return index

        