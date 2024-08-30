class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        s.reverse()
        res=[]
        for i in s:
            if i!="":
                res.append(i)
        res=" ".join(res)
        return res
            


            

        
        