arr=[1,2,3,4,5,6,7,8,9]
d=2
l=len(arr)
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start,end=start+1,end-1
def rotation(arr,d,l):
    if d==0:
        return 
    reverse(arr,0,d-1)
    reverse(arr,d,l-1)
    reverse(arr,0,l-1)
rotation(arr,d,l)
print(arr)