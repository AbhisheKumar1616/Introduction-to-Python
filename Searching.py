#binary search
def binary_search(arr,n):
    arr.sort()
    min=0
    max=len(arr)-1
    while min<=max:
        mid=(max+min)//2
        if n==arr[mid]:
            print("Found")
            break
        elif n>arr[mid]:
            min=mid+1
        else:
            max=mid-1
    else:
        print("Not found")

#________________________________________________________________________________________________
"""Binary Search using Recursion"""
def func(li,n,low,high):
    if low>high or len(li)==0:
        return -1
    mid=(low+high)//2
    if li[mid]==n:
        return mid
    else:
        if li[mid]>n:
            high=mid-1
        else:
            low=mid+1
        return func(li,n,low,high)
li=[1,2,3,4,5,6,7]
print(func(li,1111,0,len(li)-1))
