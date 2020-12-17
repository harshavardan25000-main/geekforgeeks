import math
arr=[1,2,3,4,5,6,7,8,9]
d=2
l=len(arr)
gcd_n=math.gcd(d,l)
#arr=None
def rotate(arr,d,l,gcd_n):
    if not arr or len(arr)<d:
        return None
    for i in range(gcd_n):
        temp=arr[i]
        for i in range(i,l-gcd_n,gcd_n):
            arr[i]=arr[i+gcd_n]
        arr[i+gcd_n]=temp
rotate(arr,d,l,gcd_n)

print(arr)