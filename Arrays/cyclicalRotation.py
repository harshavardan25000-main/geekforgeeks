arr=[1,2,3,4,5,6,7,8,9]
# output -: 9 1 2 3 4 5 6 7 8
l=len(arr)
def rotation(arr,l):
    if l==0 or arr is None:
        return
    temp=arr[-1]
    for i in range(l-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
rotation(arr,l)
print(arr)