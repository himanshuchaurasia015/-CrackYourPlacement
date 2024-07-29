class Solution:
    def merge(self, nums1, m: int, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j+=1
        nums1.sort()