# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            sub=[]
            for j in range(i+1):
                val=1
                if (0<=i-1<=i-1 and 0<=j-1<=i-1) and j<=i-1:
                    val=ans[i-1][j-1]+ans[i-1][j]
                sub.append(val)
            ans.append(sub)
        return ans
            

        