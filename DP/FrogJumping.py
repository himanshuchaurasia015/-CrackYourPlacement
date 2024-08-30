
# Tabulation
def frogJump(n: int, heights: List[int]) -> int:
    dp=[-1]*n
    dp[0]=0
    ener=float('inf')
    for i in range(1,n):
        f=dp[i-1]+abs(heights[i]-heights[i-1])
        s=f
        if i>1:
            s=dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i]=min(f,s)
    return dp[-1]

# memoization

def frogJump(n: int, heights: List[int]) -> int:

    # Write your code here.
    def solve(i,n,heights,d={0:0}):
        if i in d:
            return d[i]
        a=solve(i-1,n,heights)+abs(heights[i-1]-heights[i])
        b=a
        if i>1:
            b=solve(i-2,n,heights)+abs(heights[i-2]-heights[i])
        d[i]= min(a,b)
        return d[i]
    return solve(n-1,n,heights)