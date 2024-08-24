# subarray
arr=[3,2,1]
res=[]
def subseq(i,arr,res,sub=[]):
    if i==len(arr):
        res.append(sub.copy())
        return
    sub.append(arr[i])
    subseq(i+1,arr,res,sub)
    sub.pop()
    subseq(i+1,arr,res,sub)
subseq(0,arr,res)
print(res)



# subbarray of k summ
arr=[1,2,1]
res=[]
def subseq(i,arr,k,summ,res,sub=[]):
    if i==len(arr):
        if summ==k:
            res.append(sub.copy())
        return
    sub.append(arr[i])
    summ+=arr[i]
    subseq(i+1,arr,k,summ,res,sub)
    sub.pop()
    summ-=arr[i]
    subseq(i+1,arr,k,summ,res,sub)
k=2
summ=0
subseq(0,arr,k,summ,res)
print(res)


# print one subseq of sum sum
arr=[1,2,1]
summ=2
res=[]
def subseq(arr,i,n,summ,curr,res,sub=[]):
    if i==n:
        if curr==summ:
            res=res.append(sub.copy())
            return True
        else:
            return False
    sub.append(arr[i])
    curr+=arr[i]
    if  subseq(arr,i+1,n,summ,curr,res,sub):
        return True
    curr-=arr[i]
    sub.pop()
    if subseq(arr,i+1,n,summ,curr,res,sub):
        return True
    return False
subseq(arr,0,len(arr),summ,0,res)
print(res)



# count subseq sum==k
arr=[1,2,1]
k=2
def subseqcount(arr,i,k,summ,n,sub=[]):
    if i==n:
        if summ==k:
            return 1
        else:
            return 0
    sub.append(arr[i])
    summ+=arr[i]
    a=subseqcount(arr,i+1,k,summ,n,sub)
    summ-=arr[i]
    sub.pop()
    b=subseqcount(arr,i+1,k,summ,n,sub)
    return a+b
print(subseqcount(arr,0,k,0,len(arr)))     

