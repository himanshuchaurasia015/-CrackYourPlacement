class Solution:
    def maxScore(self, points, k):
        n=len(points)
        l=0
        r=n-k
        res=sum(points[r:])
        maxsum=sum(points[r:])
        print(maxsum)
        while(r<n):
            maxsum+=points[l]
            maxsum-=points[r]
            res=max(res,maxsum)
            l+=1
            r+=1
        return res




            

            

            
            
            
        