class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        def solve(index,arr,curr,res,n,sub=[]):
            if curr==target:
                res.append(sub.copy())
                return
            if curr>target:
                return
            for i in range(index,n):
                if i>index and arr[i-1]==arr[i]:
                    continue
                curr+=arr[i]
                sub.append(arr[i])
                solve(i+1,arr,curr,res,n,sub)
                curr-=sub.pop()
        res=[]
        arr.sort()
        solve(0,arr,0,res,len(arr))
        return res



        

        