# You are given an array 'arr' containing 'n' non-negative integers.



# Your task is to partition this array into two subsets such that the absolute difference between subset sums is minimum.



# You just need to find the minimum absolute difference considering any valid division of the array elements.



# Note:

# 1. Each array element should belong to exactly one of the subsets.

# 2. Subsets need not always be contiguous.
# For example, for the array : [1, 2, 3], some of the possible divisions are 
#    a) {1,2} and {3}
#    b) {1,3} and {2}.

# 3. Subset-sum is the sum of all the elements in that subset. 
# Example:
# Input: 'n' = 5, 'arr' = [3, 1, 5, 2, 8].

# Ouput: 1

# Explanation: We can partition the given array into {3, 1, 5} and {2, 8}. 
# This will give us the minimum possible absolute difference i.e. (10 - 9 = 1).
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 4
# 1 2 3 4
# Sample Output 1:
# 0
# Explanation for sample input 1:
# We can partition the given array into {2,3} and {1,4}.
# This will give us the minimum possible absolute difference i.e. (5 - 5 = 0) in this case.
# Sample Input 2:
# 3
# 8 6 5
# Sample Output 2:
# 3
# Explanation for sample input 2:
# We can partition the given array into {8} and {6,5}. 
# This will give us the minimum possible absolute difference i.e. (11 - 8 = 3).
# Expected time complexity:
# The expected time complexity is O(n * 𝚺 'arr'[i]), where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.
# Constraints:
# 1 <= 'n' <= 10^3
# 0 <= 'arr'[i] <= 10^3
# 0 <= 𝚺 'arr'[i] <= 10^4, 

# where 𝚺 'arr'[i] denotes the sum of all elements in 'arr'.

# Time Limit: 1sec




def subsetSumUtil(ind, target, arr, dp):
    # Base case: If the target sum is 0, we have found a subset that sums to the target.
    if target == 0:
        return True

    # Base case: If we have reached the first element of the array, check if it equals the target.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursive cases:
    # 1. Try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    # 2. Try taking the current element if it is less than or equal to the target.
    taken = False
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Update the DP table and return the result.
    dp[ind][target] = notTaken or taken
    return dp[ind][target]

def minSubsetSumDifference(arr):
    n = len(arr)
    totSum = sum(arr)

    # Initialize a DP table to store the subset sum information.
    dp = [[-1 for i in range(totSum + 1)] for j in range(n)]

    # Calculate dummy values for all possible sums using subsetSumUtil.
    for i in range(totSum + 1):
        dummy = subsetSumUtil(n - 1, i, arr, dp)

    # Initialize a variable to track the minimum absolute difference.
    mini = int(1e9)

    # Iterate through all possible sums.
    for i in range(totSum + 1):
        if dp[n - 1][i] == True:
            # Calculate the difference between the current sum and the complement sum.
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)

    return mini


