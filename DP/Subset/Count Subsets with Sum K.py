# You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.



# Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.



# Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.



# Example:
# Input: 'arr' = [1, 1, 4, 5]

# Output: 3

# Explanation: The possible ways are:
# [1, 4]
# [1, 4]
# [5]
# Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 4 5
# 1 4 4 5


# Sample Output 1 :
#  3


# Explanation For Sample Output 1:
# The possible ways are:
# [1, 4]
# [1, 4]
# [5]
# Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.


# Sample Input 2 :
# 3 2
# 1 1 1


# Sample Output 2 :
# 3


# Explanation For Sample Output 1:
# There are three 1 present in the array. Answer is the number of ways to choose any two of them.


# Sample Input 3 :
# 3 40
# 2 34 5


# Sample Output 3 :
# 0


# Expected time complexity :
# The expected time complexity is O('n' * 'k').


# Constraints:
# 1 <= 'n' <= 100
# 0 <= 'arr[i]' <= 1000
# 1 <= 'k' <= 1000

# Time limit: 1 sec


from typing import List

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    MOD=10**9+7
    def solve(i,target,arr,dp):
        if dp[i][target]!=-1:
            return dp[i][target]
        if i==0:
            if arr[0] ==0 and target==0:
                return 2
            if target==0 or target ==arr[0]:
                return 1
            return 0
        r=solve(i-1,target,arr,dp)
        l=0
        if arr[i]<=target:
            l=solve(i-1,target-arr[i],arr,dp)
        t=l+r
        dp[i][target]= t%MOD
        return dp[i][target]
    dp=[[-1]*(k+1) for _ in range(len(arr))]
    return solve(len(arr)-1,k,arr,dp)

# --------------------------------tabulation----------------------------------------

def findWays(num, k):
    n = len(num)
    
    # Initialize a 2D DP array to store the count of subsets for different targets.
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: There is always one way to make a subset with a target sum of 0 (empty subset).
    for i in range(n):
        dp[i][0] = 1
    
    # Handle the base case for the first element in the array.
    if num[0] <= k:
        dp[0][num[0]] = 1

    # Iterate through the elements in the array.
    for ind in range(1, n):
        for target in range(1, k + 1):
            # If the current element is not taken, the count is the same as the previous row.
            notTaken = dp[ind - 1][target]
            
            # If the current element is taken, subtract its value from the target and check the previous row.
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            
            # Update the DP array with the total count of ways (taken + notTaken).
            dp[ind][target] = notTaken + taken

    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][k]