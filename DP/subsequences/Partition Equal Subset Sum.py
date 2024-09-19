
# Problem statement
# You are given an array 'ARR' of 'N' positive integers. 
# Your task is to find if we can partition the given array into two subsets such that the sum of elements in both subsets is equal.

# For example, let’s say the given array is [2, 3, 3, 3, 4, 5], then the array can be partitioned as [2, 3, 5], and [3, 3, 4] with equal sum 10.

# Follow Up:

# Can you solve this using not more than O(S) extra space, where S is the sum of all elements of the given array?
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= 'T' <= 10
# 1 <= 'N' <= 100 
# 1 <= 'ARR'[i] <= 100

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 6
# 3 1 1 2 2 1
# 5
# 5 6 5 11 6
# Sample Output 1:
# true
# false    
# Explanation Of Sample Input 1:
# For the first test case, the array can be partitioned as ([2,1,1,1] and [3, 2]) or ([2,2,1], and [1,1,3]) with sum 5.

# For the second test case, the array can’t be partitioned.
# Sample Input 2:
# 2
# 9
# 2 2 1 1 1 1 1 3 3
# 6
# 8 7 6 12 4 5
# Sample Output 2:
# false
# true





def canPartition(arr, n):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    total=sum(arr)
    if sum(arr)%2!=0:
        return False
    total=total//2
    def solve(i,total,arr,dp):
        if total==0:
            return True
        if i==0:
            return arr[0]==total
        if dp[i][total]!=-1:
            return dp[i][total]
        tk=False
        if arr[i]<=total:
            tk=solve(i-1,total-arr[i],arr,dp)
        nt=solve(i-1,total,arr,dp)
        dp[i][total]= tk or nt
        return dp[i][total]
    dp=[[-1]*(total+1) for j in range((n))]
    return solve(n-1,total,arr,dp)

# ------------------------------------Tabulation---------------------------------------
    total=sum(arr)
    total=total//2
    if sum(arr)%2!=0:
        return False
    dp=[[False]*(total+1) for j in range((n))]
    # basecase
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=total:
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,total+1):
            tk=False
            if arr[i]<=j:
                tk=dp[i-1][j-arr[i]]
            nt=dp[i-1][j]
            dp[i][j]=nt or tk
    return dp[n-1][total]

# ---------------------------------------optimized-------------------------------------------


    # Initialize a boolean array 'prev' with size (total + 1).
    total=sum(arr)
    if sum(arr)%2!=0:
        return False
    total=total//2
    prev = [False] * (total + 1)
    
    # Set the first element of 'prev' to True since an empty subset can sum up to 0.
    prev[0] = True
    
    # Chectotal if the first element of 'arr' can directly contribute to the target sum 'total'.
    if arr[0] <= total:
        prev[arr[0]] = True

    # Loop through the elements of 'arr' and update 'prev' using dynamic programming.
    for ind in range(1, n):
        # Initialize a new boolean array 'cur' for the current element.
        cur = [False] * (total + 1)
        
        # An empty subset can always sum up to 0.
        cur[0] = True
        
        for target in range(1, total + 1):
            not_tatotalen = prev[target]  # Previous result without including the current element.
            tatotalen = False
            
            # Chectotal if including the current element is possible without exceeding the target.
            if arr[ind] <= target:
                tatotalen = prev[target - arr[ind]]
            
            # Update 'cur' with the result for the current 'target'.
            cur[target] = not_tatotalen or tatotalen
        
        # Update 'prev' with the results for the current element 'ind'.
        prev = cur

    # The final result is stored in 'prev[total]'.
    return prev[total]

