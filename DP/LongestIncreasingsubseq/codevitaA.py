# BestBubble
# Problem Description
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. The problem with bubble sort is its worst case scenario. When the smallest element is in the last position, then it takes more time to sort in ascending order, but takes less time to sort in descending order.

# An array is called beautiful if all the elements of the array are in either ascending or descending order. Given an array of numbers, find the minimum swap operations required to make the array beautiful.

# Constraints
# 0 < N < 1000

# 0 < Arr[i] < 1000

# Input
# First line contains of integer N denoting number of elements in the array.

# Second line consist of N integers separated by space denoting the elements of the array.

# Output
# Single integer denoting the least numbers of swap operations required to make the array beautiful.

# Time Limit (secs)
# 1

# Examples
# Example 1:

# Input:

# 5

# 4 5 3 2 1

# Output:

# 1

# Explanation:

# The number of swaps required to sort the elements in ascending order is 9.

# The number of swaps required to sort the elements in descending order is 1.

# The best way is to sort in descending order and swaps required is 1.

# Example 2:

# Input:

# 5

# 4 5 1 2 3

# Output 2:

# 4


# The number of swaps required to sort the elements in ascending order is 6.

# The number of swaps required to sort the elements in descending order is 4.

# The best way is to sort in descending order and swaps required is 4.


def merge(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1 # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
        
    return inv_count

def count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2

        inv_count += count(arr, temp_arr, left, mid)
        inv_count += count(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count

def swaps(nums, ascending=True):
    n = len(nums)
    temp_arr = [0]*n
    if ascending:
        return count(nums, temp_arr, 0, n - 1)
    else:
        nums = [-num for num in nums]  # Reverse the order by negating
        swaps = count(nums, temp_arr, 0, n - 1)
        nums = [-num for num in nums]  # Restore original values
        return swaps

n = int(input())
nums = list(map(int, input().split()))
a = swaps(nums.copy(), ascending=True)
b = swaps(nums.copy(), ascending=False)
print(min(a, b))