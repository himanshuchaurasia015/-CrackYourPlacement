# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

# Given n and k, return the kth permutation sequence.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

# Example 3:
# Input: n = 3, k = 1
# Output: "123"


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        f=1
        for i in range(1,n):
            nums.append(i)
            f*=i
        nums.append(n)
        ans=""
        k-=1
        while(True):
            index=(k)//f
            ans+=str(nums[index])
            del nums[index]
            if len(nums)==0:
                break
            k=(k)%f
            f=f//len(nums)
        return ans
    



# def solve(n,k):
#     nums=[]
#     factorial=1
#     for i in range(1,n):
#         nums.append(i)
#         factorial*=i
#     nums.append(n)
#     ans=""
#     k-=1
#     while(True):
#         ans+=str(nums[k//factorial])
#         del nums[k//factorial]
#         if not nums:
#             break
#         k=k%factorial
#         factorial=factorial//len(nums)
#     return ans
# print(solve(3,6))
