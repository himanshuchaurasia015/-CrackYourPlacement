#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		def solve(arr,i,res,curr):
			if i==n:
				res.append(curr)
				return
			curr+=arr[i]
			solve(arr,i+1,res,curr)
			curr-=arr[i]
			solve(arr,i+1,res,curr)
		 
		res=[]
		arr.sort()
		solve(arr,0,res,0)
		return res
		  