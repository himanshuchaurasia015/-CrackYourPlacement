arr=[4,6,2,5,7,9,1,3,8]
def partition(arr,low,high):
    if low<high:
        i=low
        j=high
        pivot=arr[low]
        while i<j:
            while arr[i]<=pivot and i<high: i+=1
            while arr[j]>pivot and j>low: j-=1
            if i<j: arr[i],arr[j]=arr[j],arr[i]
            else:
                arr[low],arr[j]=arr[j],arr[low]
                return j
def quicksort(arr,low,high):
    if low<high:
        partion=partition(arr,low,high)
        quicksort(arr,low,partion-1)
        quicksort(arr,partion+1,high)

quicksort(arr,0,len(arr)-1)
print(arr)

