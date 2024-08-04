class Solution:
    def spiralOrder(self, matrix):
        l=0
        r=len(matrix[0])
        t=0
        b=len(matrix)
        res=[]
        while(l<r and t<b):
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            for j in range(t,b):
                res.append(matrix[j][r-1])
            r-=1
            if not(l<r and t<b):
                break 
            for k in range(r-1,l-1,-1):
                res.append(matrix[b-1][k])
            b-=1
            for x in range(b-1,t-1,-1):
                res.append(matrix[x][l])
            l+=1
        return res



        