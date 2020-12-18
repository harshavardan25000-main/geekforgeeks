arr=[3,4,5,6,7,8,1,2]
####[0,1,2,3,4,5,6,7]
start=0
end=len(arr)
key=71
if len(arr)==0 or arr is None:
    print('-1')
def find_pivot(arr,start,end):
    if start>end:
        return -1
    mid=((end-start)//2)+start
    if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
        return mid+1
    elif arr[mid]>arr[mid-1]:
        return find_pivot(arr,mid+1,end)
    else:
        return find_pivot(arr,start,mid)

def search(arr,start,end):
    if start>end:
        return -1
    mid=((end-start)//2)+start
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return search(arr,start,mid)
    else:
        return search(arr,mid+1,end)
pivot=find_pivot(arr,start,end)
if arr[0]==key:
    print('0')
elif arr[0]<key:
    print(search(arr,0,pivot-1))
else:
    print(search(arr,pivot,end))
