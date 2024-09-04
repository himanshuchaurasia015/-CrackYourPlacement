# Ninja is planing this ‘N’ days-long training schedule. 
# Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves).
#  Each activity has some merit points on each day.
#  As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days.
#  Can you help Ninja find out the maximum merit points Ninja can earn?

# You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity.
#  Your task is to calculate the maximum number of merit points that Ninja can earn.

# For Example
# If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= N <= 100000.
# 1 <= values of POINTS arrays <= 100 .

# Time limit: 1 sec
# Sample Input 1:
# 2
# 3
# 1 2 5 
# 3 1 1
# 3 3 3
# 3
# 10 40 70
# 20 50 80
# 30 60 90
# Sample Output 1:
# 11
# 210
# Explanation of sample input 1:
# For the first test case,
# One of the answers can be:
# On the first day, Ninja will learn new moves and earn 5 merit points. 
# On the second day, Ninja will do running and earn 3 merit points. 
# On the third day, Ninja will do fighting and earn 3 merit points. 
# The total merit point is 11 which is the maximum. 
# Hence, the answer is 11.

# For the second test case:
# One of the answers can be:
# On the first day, Ninja will learn new moves and earn 70 merit points. 
# On the second day, Ninja will do fighting and earn 50 merit points. 
# On the third day, Ninja will learn new moves and earn 90 merit points. 
# The total merit point is 210 which is the maximum. 
# Hence, the answer is 210.
# Sample Input 2:
# 2
# 3
# 18 11 19
# 4 13 7
# 1 8 13
# 2
# 10 50 1
# 5 100 11
# Sample Output 2:
# 45
# 110

def ninjaTraining(n: int, points) -> int:

    # Write your code here.
    # memoization
    def solve(i,points,d,dp):
        if dp[i][d] !=-1:
            return dp[i][d]
        if i==0:
            m=0
            for j in range(3):
                if j!=d:
                    m=max(m,points[i][j])
            return m
        mcurr=0
        a=0
        for j in range(3):
            if j !=d:
                a=points[i][j]+solve(i-1,points,j,dp)
                mcurr=max(a,mcurr)
        dp[i][d]= mcurr
        return mcurr
    
    dp=[[-1]*3 for i in range(len(points))]
    return solve(len(points)-1,points,-1,dp)


# -----------------------------Tabulation-----------------------------------------------

    dp=[[0]*4 for i in range(len(points))]
    dp[0][0]=max(points[0][1],points[0][2])
    dp[0][1]=max(points[0][0],points[0][2])
    dp[0][2]=max(points[0][1],points[0][0])
    dp[0][3]=max(points[0][0],max(points[0][1],points[0][2]))

    for d in range(1,len(points)):
        for l in range(4):
            c=0
            for t in range(3):
                if t!=l:
                    a=points[d][t]+dp[d-1][t]
                    c=max(c,a)
                    dp[d][l]=c
                    print(dp,d,l,t)
            
    return dp[-1][-1]


# -----------------------------------optimized-----------------------------


    dp=[0]*4
    dp[0]=max(points[0][1],points[0][2])
    dp[1]=max(points[0][0],points[0][2])
    dp[2]=max(points[0][1],points[0][0])
    dp[3]=max(points[0][0],max(points[0][1],points[0][2]))

    for d in range(1,len(points)):
        arr=[0]*4
        for l in range(4):
            arr[l]=0
            for t in range(3):
                if t!=l:
                    a=points[d][t]+dp[t]
                    arr[l]=max(arr[l],a)
        dp=arr.copy()
    return dp[-1]


# ------------------------------Recursion----------------------------------

    def solve(i,points,d):
        if i==0:
            m=0
            for j in range(3):
                if j!=d:
                    m=max(m,points[i][j])
            return m
        mcurr=0
        a=0
        for j in range(3):
            if j !=d:
                a=points[i][j]+solve(i-1,points,j)
                mcurr=max(a,mcurr)
        return mcurr
    
    dp=[[-1]*3 for i in range(len(points))]
    return solve(len(points)-1,points,-1,dp)

print(ninjaTraining(3,[
    [1, 2, 5] ,
    [3, 1, 1],
    [3, 3, 3]]))