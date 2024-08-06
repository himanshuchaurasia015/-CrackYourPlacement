# Given an integer array nums, return the number of reverse pairs in the array.

# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

# Constraints:

# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1



class Solution:
    def reversePairs(self, nums):
        self.count=0
        def merge(low, mid,high):
            temp=[]
            left=low
            right=mid+1
            while(left<=mid and right<=high):
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            while(left<=mid):
                temp.append(nums[left])
                left+=1
            while(right<=high):
                temp.append(nums[right])
                right+=1
            for i in range(low,high+1):
                nums[i]=temp[i-low]


        def count_merge(low,mid,high):
            right=mid+1
            for i in range(low,mid+1):
                while right<=high and nums[i]>2*nums[right]:
                    right+=1
                self.count+=right-(mid+1)
            merge(low, mid, high)


        def mergesort(low,high):
            if low>=high:
                return
            mid=(low+high)//2
            mergesort(low,mid)
            mergesort(mid+1,high)
            count_merge(low, mid, high)

        mergesort(0,len(nums)-1)
        return self.count



        
        