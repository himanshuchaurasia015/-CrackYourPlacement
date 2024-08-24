def merge(arr,low,high,mid):
    if low>=high: return
    temp=[]
    l=low
    r=mid+1
    while( l<=mid and r<=high):
        if arr[l]<=arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    while(l<=mid):
        temp.append(arr[l])
        l+=1
    while(r<=high):
        temp.append(arr[r])
        r+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]


def mergeSort(arr,low,high):
    if low==high:
        return
    mid =(low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,high,mid)

re=[9,8,7,6,5,4,3,2,1]
mergeSort(re,0,len(re)-1)
print(re)
    