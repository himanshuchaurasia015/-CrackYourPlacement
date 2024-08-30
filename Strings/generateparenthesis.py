class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(o,c,n,res,curr=[]):
            if o==n and c==n:
                a="".join(curr)
                res.append(a)
                return
            if o!=n+1:
                curr.append("(")
                solve(o+1,c,n,res,curr)
                curr.pop()
            if o>c and c!=n+1:
                curr.append(")")
                solve(o,c+1,n,res,curr)
                curr.pop()
        res=[]
        solve(0,0,n,res)
        return res


                

        