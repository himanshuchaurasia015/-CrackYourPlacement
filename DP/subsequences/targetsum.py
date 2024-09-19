# Problem statement
# You are given an array ‘ARR’ of ‘N’ integers and a target number, ‘TARGET’. Your task is to build an expression out of an array by adding one of the symbols '+' and '-' before each integer in an array, and then by concatenating all the integers, you want to achieve a target. You have to return the number of ways the target can be achieved.

# For Example :
# You are given the array ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
# 1. -1 + 1 + 1 + 1 + 1 = 3
# 2. +1 - 1 + 1 + 1 + 1 = 3
# 3. +1 + 1 - 1 + 1 + 1 = 3
# 4. +1 + 1 + 1 - 1 + 1 = 3
# 5. +1 + 1 + 1 + 1 - 1 = 3
# These are the 5 ways to make. Hence the answer is 5.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 1 <= N <= 25
# -1000 <= TARGET <= 1000
# 0 <= ARR[i] <= 1000

# Time Limit: 1 sec
# Note :
# You do not need to print anything. It has already been taken care of. Just implement the given function.
# Sample input 1 :
# 2
# 5 3
# 1 1 1 1 1
# 4 3
# 1 2 3 1
# Sample Output 2 :
# 5
# 2
# Explanation For Sample Input 1 :
# For the first test case, ‘ARR’ = [1, 1, 1, 1, 1], ‘TARGET’ = 3. The number of ways this target can be achieved is:
# 1. -1 + 1 + 1 + 1 + 1 = 3
# 2. +1 - 1 + 1 + 1 + 1 = 3
# 3. +1 + 1 - 1 + 1 + 1 = 3
# 4. +1 + 1 + 1 - 1 + 1 = 3
# 5. +1 + 1 + 1 + 1 - 1 = 3
# These are the 5 ways to get the target. Hence the answer is 5.

# For the second test case, ‘ARR’ = [1, 2, 3, 1]. ‘TARGET’ = 3, The number of ways this target can be achieved is:
# 1. +1 - 2 + 1 + 3 = 3
# 2. -1 + 2 - 1 + 3 = 3
# These are the 3 ways to get the target. Hence the answer is 2.
# Sample Input 2 :
# 2
# 3 2
# 1 2 3
# 2 0
# 1 1
# Sample Output 2 :
# 1
# 2

# same question as partition with given difference


from typing import List

def targetSum(arr: List[int], target: int) -> int:
    def solve(i,target,arr,dp):
        if i==0:
            if (target==arr[0]) or target==-arr[0]:
                if arr[0]==0:
                    return 2
                return 1
            return 0
        if (i,target) in dp:
                return dp[(i,target)]
        plus,minus=0,0
        plus=solve(i-1,target+arr[i],arr,dp)
        minus=solve(i-1,target-arr[i],arr,dp)
        dp[(i,target)]= plus+minus
        return dp[(i,target)]
    dp={}
    return solve(len(arr)-1,target,arr,dp)


# ---------------------------------tabulation---------------------------------

def findWays(num, tar):
    n = len(num)
    dp = [[0 for i in range(tar + 1)] for j in range(n)]

    if num[0] == 0:
        dp[0][0] = 2  # 2 cases - pick and not pick
    else:
        dp[0][0] = 1  # 1 case - not pick

    if num[0] != 0 and num[0] <= tar:
        dp[0][num[0]] = 1  # 1 case - pick

    for ind in range(1, n):
        for target in range(tar + 1):
            notTaken = dp[ind - 1][target]

            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]

            dp[ind][target] = (notTaken + taken)

    return dp[n - 1][tar]