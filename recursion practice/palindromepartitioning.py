class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(subs):
            return subs[::-1]==subs
            
        def solve(p,res,s,curr=[]):
            if p==len(s):
                print(curr)
                res.append(curr.copy())
                return
            for i in range(p,len(s)):
                sub=s[p:i+1]
                if check(sub):
                    curr.append(sub)
                    solve(i+1,res,s,curr)
                    curr.pop()

        res=[]
        solve(0,res,s)
        return res

            
       