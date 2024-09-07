# Problem statement
# You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

# Note:
# You have an infinite number of elements of each type.
# For example
# If N=3 and X=7 and array elements are [1,2,3]. 
# Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
# Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
# Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
# Hence the output is 3.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 10
# 1 <= N <= 15
# 1 <= nums[i] <= (2^31) - 1
# 1 <= X <= 10000

# All the elements of the “nums” array will be unique.
# Time limit: 1 sec
# Sample Input 1 :
# 2
# 3 7
# 1 2 3
# 1 0
# 1
# Sample output 1 :
#  3
#  0
# Explanation For Sample Output 1:
# For the first test case,
# Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
# Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
# Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
# Hence the output is 3.

# For the second test case,
# Way 1 - You can take 3 elements  [1, 1, 1] as 1 + 1 + 1  = 3.
# Way 2 - You can take 2 elements  [2, 1] as 2 + 1 = 3.
# Here, you can see in Way 2 we have used 2 coins to reach the target sum of 7.
# Hence the output is 2.
# Sample Input 2 :
# 2
# 3 4
# 12 1 3
# 2 11
# 2 1
# Sample output 2 :
# 2
# 6 

# -----------------------------------memoization-----------------------------
def minimumElementsUtil(arr, ind, T, dp):
    # Base case: If we have reached the first element in the array.
    if ind == 0:
        # If the target T is divisible by the first element, return the quotient as the minimum number of coins.
        if T % arr[0] == 0:
            return T // arr[0]
        else:
            # If not, it's not possible to achieve the target sum, so return a very large value.
            return int(1e9)

    # If the result for this state is already calculated, return it.
    if dp[ind][T] != -1:
        return dp[ind][T]

    # Initialize variables for cases when we don't take the current element.
    notTaken = 0 + minimumElementsUtil(arr, ind - 1, T, dp)

    # Initialize a variable for the case when we take the current element.
    taken = int(1e9)

    # Check if the current element can be used to reduce the target sum.
    if arr[ind] <= T:
        taken = 1 + minimumElementsUtil(arr, ind, T - arr[ind], dp)

    # Store the minimum of the two cases in the DP table.
    dp[ind][T] = min(notTaken, taken)
    return dp[ind][T]

# -----------------------------tabulation------------------------

def minimumElements(arr, T):
    n = len(arr)
    # Initialize a DP table with 0 values for bottom-up dynamic programming.
    dp = [[0 for _ in range(T + 1)] for _ in range(n)]

    # Fill in the DP table for the first element in the array (base case).
    for i in range(T + 1):
        if i % arr[0] == 0:
            dp[0][i] = i // arr[0]
        else:
            # Set an initial large value to indicate that it's not possible to achieve the target sum.
            dp[0][i] = int(1e9)

    # Iterate over the array elements and target values to fill in the DP table.
    for ind in range(1, n):
        for target in range(T + 1):
            # Calculate the minimum number of elements needed to achieve the current target.
            notTake = dp[ind - 1][target]  # Option: Don't take the current element.
            take = int(1e9)  # Initialize as a large value.
            if arr[ind] <= target:
                # Option: Take the current element, reduce the target, and add 1 to the count.
                take = 1 + dp[ind][target - arr[ind]]
            # Store the minimum of the two options in the DP table.
            dp[ind][target] = min(notTake, take)

    # The result is stored in the last cell of the DP table.
    ans = dp[n - 1][T]
    # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
    if ans >= int(1e9):
        return -1
    return ans



def minimumElements(arr, T):
    n = len(arr)
    # Initialize a DP table with -1 values.
    dp = [[-1 for j in range(T + 1)] for i in range(n)]
    # Calculate the minimum number of coins required using the helper function.
    ans = minimumElementsUtil(arr, n - 1, T, dp)

    # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
    if ans >= int(1e9):
        return -1
    return ans

# -----------------------------------------------space optimized----------------------------------
def minimumElements(arr, T):
    n = len(arr)
    
    # Initialize two lists: 'prev' and 'cur' for dynamic programming.
    prev = [0] * (T + 1)  # To store results for the previous element.
    cur = [0] * (T + 1)   # To store results for the current element.

    # Fill in the DP table for the first element in the array (base case).
    for i in range(0, 1 + T):
        if i % arr[0] == 0:
            prev[i] = i // arr[0]
        else:
            # Set an initial large value to indicate that it's not possible to achieve the target sum.
            prev[i] = int(1e9)

    # Iterate over the array elements and target values to fill in the DP table.
    for ind in range(1, n):
        for target in range(T + 1):
            # Calculate the minimum number of elements needed to achieve the current target.
            not_take = prev[target]  # Option: Don't take the current element.
            take = int(1e9)          # Initialize as a large value.
            
            if arr[ind] <= target:
                # Option: Take the current element, reduce the target, and add 1 to the count.
                take = 1 + cur[target - arr[ind]]
                
            cur[target] = min(not_take, take)  # Store the minimum of the two options in the 'cur' list.

        prev = cur  # Update the 'prev' list with the values from the 'cur' list for the next iteration.

    # The result is stored in the 'prev' list for the target T.
    ans = prev[T]
    
    # If the result is still equal to a very large value, it means it's not possible to achieve the target sum.
    if ans >= int(1e9):
        return -1
    return ans

def main():
    arr = [1, 2, 3]
    T = 7
    print("The minimum number of coins required to form the target sum is", minimumElements(arr, T))

if __name__ == '__main__':
    main()