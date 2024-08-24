# reverse array
arr=[1,2,3,4,5,6]


def revarr(l,r,arr):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    revarr(l+1,r-1,arr)
revarr(0,5,arr)

arr=[1,2,3,4,5,6]

def revarr2(i,n):
    if i>=n-1-i:
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    revarr2(i+1,n)

revarr2(0,6)
print(arr)

s="hima"
def rev(i,n):
    if i>=n/2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return rev(i+1,n)

print(rev(0,len(s)))



