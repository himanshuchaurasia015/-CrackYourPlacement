# Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
# A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing. Return the maximum length of bitonic subsequence.
 
# Note : A strictly increasing or a strictly decreasing sequence should not be considered as a bitonic sequence

# Examples :

# Input: n = 5, nums[] = [1, 2, 5, 3, 2]
# Output: 5
# Explanation: The sequence {1, 2, 5} is increasing and the sequence {3, 2} is decreasing so merging both we will get length 5.
# Input: n = 8, nums[] = [1, 11, 2, 10, 4, 5, 2, 1]
# Output: 6
# Explanation: The bitonic sequence {1, 2, 10, 4, 2, 1} has length 6.

# Input: n = 5, nums[] = [10, 20, 30]
# Output: 0
# Explanation: The decreasing or increasing part cannot be empty

# Input: n = 5, nums[] = [10, 10, 10]
# Output: 0
# Explanation: The subsequences must be strictly increasing or decreasing
# Expected Time Complexity: O(n2)
# Expected Auxiliary Space : O(n)
 

# Constraints:
# 1 ≤ length of array ≤ 103
# 1 ≤ arr[i] ≤ 104



def longest_bitonic_sequence(arr):
    n = len(arr)

    # Initialize two dynamic programming lists for increasing and decreasing subsequences
    dp1 = [1] * n
    dp2 = [1] * n

    # Calculate the length of the longest increasing subsequence
    for i in range(n):
        for prev_index in range(i):
            if arr[prev_index] < arr[i]:
                dp1[i] = max(dp1[i], 1 + dp1[prev_index])

    # Reverse the direction of nested loops to calculate the length of the longest decreasing subsequence
    for i in range(n - 1, -1, -1):
        for prev_index in range(n - 1, i, -1):
            if arr[prev_index] < arr[i]:
                dp2[i] = max(dp2[i], 1 + dp2[prev_index])

    maxi = 0

    # Find the maximum length of bitonic subsequence by combining increasing and decreasing lengths
    for i in range(n):
        if dp1[i]!=1 and dp2[i]!=1: #add this if you subsequence first increase then decrease otherwise remove this line
            maxi = max(maxi, dp1[i] + dp2[i] - 1)

    return maxi


if __name__ == "__main__":
    arr = [5,7,9]
    n = len(arr)

    print("The length of the longest bitonic subsequence is", longest_bitonic_sequence(arr))