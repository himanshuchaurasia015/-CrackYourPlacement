# You are given an array/list of ‘N’ integers. 
# You are supposed to return the maximum sum of the subsequence 
# with the constraint that no two elements are adjacent in the given array/list.

# Note:
# A subsequence of an array/list is obtained by deleting some number of elements (can be zero) from the array/list,
#  leaving the remaining elements in their original order.
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= T <= 500
# 1 <= N <= 1000
# 0 <= ARR[i] <= 10^5

# Where 'ARR[i]' denotes the 'i-th' element in the array/list.

# Time Limit: 1 sec.
# Sample Input 1:
# 2
# 3
# 1 2 4
# 4
# 2 1 4 9
# Sample Output 1:
# 5
# 11
# Explanation to Sample Output 1:
# In test case 1, the sum of 'ARR[0]' & 'ARR[2]' is 5 which is greater than 'ARR[1]' which is 2 so the answer is 5.

# In test case 2, the sum of 'ARR[0]' and 'ARR[2]' is 6, the sum of 'ARR[1]' and 'ARR[3]' is 10, 
# and the sum of 'ARR[0]' and 'ARR[3]' is 11. 
# So if we take the sum of 'ARR[0]' and 'ARR[3]', 
# it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.
# Sample Input 2:
# 2
# 5
# 1 2 3 5 4
# 9
# 1 2 3 1 3 5 8 1 9
# Sample Output 2:
# 8
# 24
# Explanation to Sample Output 2:
# In test case 1, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]' and 'ARR[4]', i.e. 8, 
# it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.

# In test case 2, out of all the possibilities, if we take the sum of 'ARR[0]', 'ARR[2]', 'ARR[4]', 'ARR[6]' and 'ARR[8]', i.e. 24 
# so, it will give the maximum sum of sequence in which no elements are adjacent in the given array/list.


# memomoization
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    def solve(i,num,d={}):
        if i in d:
            return d[i]
        if i == 0:
            return num[i]
        if i<0:
            return 0
        a=num[i]+solve(i-2,num)
        b=solve(i-1,num)
        d[i]=max(a,b)
        return d[i]
    return solve(len(nums)-1,nums)


# ---------------------------------------AND------------------------------------------
# tabulation
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp=[-1]*len(nums)
    dp[0]=nums[0]
    for i in range(1,len(nums)):
        take=nums[i]
        if i>1:
            take+=dp[i-2]
        nottake=dp[i-1]
        dp[i]=max(take,nottake)
    return dp[-1]
# -------------------------------OR------------------------------------------------

# space optimized
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    prev2=0
    prev1=nums[0]
    for i in range(1,len(nums)):
        curr=nums[i]
        if i>1:
            curr+=prev2
        curr=max(curr,prev1)
        prev2=prev1
        prev1=curr
    return prev1