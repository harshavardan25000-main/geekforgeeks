arr=[1,2,3,4,5,6,7]
#arr=None
def rotate(arr,d):
    if not arr or len(arr)<d:
        return None
    return arr[d:]+arr[:d]
print(rotate(arr,2))