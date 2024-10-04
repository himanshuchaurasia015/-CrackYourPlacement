# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0

    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(cnt0):
        arr[i] = 0

    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1

    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2