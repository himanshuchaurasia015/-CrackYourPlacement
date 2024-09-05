# Problem statement
# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. 
# Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

# For Example :
# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 5
# 1 <= N <= 10^3
# 0 <= ARR[i] <= 10^9
# 0 <= K <= 10^3

# Time Limit: 1 sec
# Sample Input 1:
# 2
# 4 5
# 4 3 2 1
# 5 4
# 2 5 1 6 7
# Sample Output 1:
# true
# false
# Explanation For Sample Input 1:
# In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
# In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
# Sample Input 2:
# 2
# 4 4
# 6 1 2 1
# 5 6
# 1 7 2 9 10
# Sample Output 2:
# true
# false
# Explanation For Sample Input 2:
# In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
# In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.


# Hints:
# 1. Can you find every possible subset of ‘ARR’ and check if its sum is equal to ‘K’?
# 2. Can you use dynamic programming and use the previously calculated result to calculate the new result?
# 3. Try to use a recursive approach followed by memoization by including both index and sum we can form. 



def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    def solve(i,k,arr,dp):
        if k==0:
            return True
        if i==0:
            return arr[0]==k
        if dp[i][k]!=-1:
            return dp[i][k]
        tk=False
        if arr[i]<=k:
            tk=solve(i-1,k-arr[i],arr,dp)
        nt=solve(i-1,k,arr,dp)
        dp[i][k]= tk or nt
        return dp[i][k]
    dp=[[-1]*(k+1) for j in range((n))]
    return solve(n-1,k,arr,dp)

# ------------------------------------Tabulation---------------------------------------

    dp=[[False]*(k+1) for j in range((n))]
    # basecase
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,k+1):
            tk=False
            if arr[i]<=j:
                tk=dp[i-1][j-arr[i]]
            nt=dp[i-1][j]
            dp[i][j]=nt or tk
    return dp[n-1][k]

# ---------------------------------------optimized-------------------------------------------


    # Initialize a boolean array 'prev' with size (k + 1).
    prev = [False] * (k + 1)
    
    # Set the first element of 'prev' to True since an empty subset can sum up to 0.
    prev[0] = True
    
    # Check if the first element of 'arr' can directly contribute to the target sum 'k'.
    if arr[0] <= k:
        prev[arr[0]] = True

    # Loop through the elements of 'arr' and update 'prev' using dynamic programming.
    for ind in range(1, n):
        # Initialize a new boolean array 'cur' for the current element.
        cur = [False] * (k + 1)
        
        # An empty subset can always sum up to 0.
        cur[0] = True
        
        for target in range(1, k + 1):
            not_taken = prev[target]  # Previous result without including the current element.
            taken = False
            
            # Check if including the current element is possible without exceeding the target.
            if arr[ind] <= target:
                taken = prev[target - arr[ind]]
            
            # Update 'cur' with the result for the current 'target'.
            cur[target] = not_taken or taken
        
        # Update 'prev' with the results for the current element 'ind'.
        prev = cur

    # The final result is stored in 'prev[k]'.
    return prev[k]

