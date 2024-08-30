class Solution:
    def intToRoman(self, num: int) -> str:
        def solve(minc,mid,maxc,val):
            res=""
            if val<=3:
                for i in range(val):
                    res+=minc
            elif val==4:
                res+=minc
                res+=mid
            elif val==5:
                res+=mid
            elif val<=8:
                res+=mid
                for i in range(val-5):
                    res+=minc
            elif val==9:
                res+=minc
                res+=maxc
            return res
        
        res=""
        res=solve("M","q","q",(num//1000))
        num=num%1000
        res+=solve("C","D","M",(num//100))
        num=num%100
        res+=solve("X","L","C",(num//10))
        num=num%10
        res+=solve("I","V","X",num)
        return res