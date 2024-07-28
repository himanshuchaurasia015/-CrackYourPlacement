class Solution:
    def findMinDiff(self, A,N,M):
        A.sort()
        i=0
        j=M-1
        minn=float("inf")
        while(j<N):
            val=A[j]-A[i]
            if minn>val:
                minn=val
            i+=1
            j+=1
        return minn