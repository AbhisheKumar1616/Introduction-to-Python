#selection sort
def selection_sort(arr,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

    print(arr)

#bubble sort
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            break
    print(arr)

#insertion_sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        p=i
        for j in range(i-1,-1,-1):
            if arr[p]<arr[j]:
                arr[p],arr[j]=arr[j],arr[p]
                p=j
    print(arr)


#merge 2 sorted list to get a sorted list
def merge(a1,a2):
    a3=[]
    i,j=0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a3.append(a1[i])
            i+=1
        else:
            a3.append(a2[j])
            j+=1
    while i<len(a1):
        a3.append(a1[i])
        i+=1
    while j<len(a2):
        a3.append(a2[j])
        j+=1
    print(a3)

#merge 2 sorted list to get a sorted list
def merge(a1,a2):
    a3=[]
    i,j=0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a3.append(a1[i])
            i+=1
        else:
            a3.append(a2[j])
            j+=1
    else:
        if i<len(a1):
            a3.extend(a1[i:])
        else:
            a3.extend(a2[j:])
    print(a3)

#push all zeros to right side
def zeros(arr,n):
    for i in range(n-1):
        flag=True
        for j in range(i+1,n):
            if arr[j-1]==0 and arr[j]!=0:
                print(arr, j)
                arr[j-1],arr[j]=arr[j],arr[j-1]
                flag=False
        if flag:
            break
    print(arr)

def zeros2(a,n):
    i,k=0,0
    while i<len(a):
        if a[i]!=0:
            a[i],a[k]=a[k],a[i]
            i+=1
            k+=1
        else:
            i+=1
    print(a)


def rotate(arr,n):
    i=0
    while i<n:
        temp=arr[0]
        for j in range(1,len(arr)):
            if j!=len(arr)-1:
                arr[j-1]=arr[j]
            else:
                arr[j-1]=arr[j]
                arr[j]=temp
        i+=1
    print(arr)

def rorotate(arr,n,d):
    if arr!=0 and n!=0:
        arr1=arr[:d]
        for i in range(d,n):
            arr[i-d]=arr[i]
        arr[i-d+1:]=[]
        arr.extend(arr1)
    else:
        pass


#-------------------------------------------------------------------------------------------------------------------
"""Merge Sorting"""
def sorting_of_list(li):
    for i in range(len(li)-1):
        min=i
        for j in range(i+1,len(li)):
            if li[min]>li[j]:
                min=j
        li[min],li[i]=li[i],li[min]
    return li
def merge_sort(li):
    mid=len(li)//2
    li1=sorting_of_list(li[:mid])
    li2=sorting_of_list(li[mid:])
    i=0
    j=0
    k=0
    while i<len(li1) and j<len(li2):
        if li1[i]<li2[j]:
            li[k]=li1[i]
            i+=1
            k+=1
        else:
            li[k]=li2[j]
            k+=1
            j+=1
    while i<len(li1):
        li[k]=li1[i]
        k+=1
        i+=1
    while j<len(li2):
        li[k] = li2[j]
        k += 1
        j += 1
li=[5,2,22,8,97,7,6,22,5,1,26]
merge_sort(li)
print(li)

#---------------------------------------------------------------------------------------------------------------
"""Merge Sorting using recursion"""
def merge_func(li,li1,li2):
    i = 0
    j = 0
    k = 0
    while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            li[k] = li1[i]
            i += 1
            k += 1
        else:
            li[k] = li2[j]
            k += 1
            j += 1
    while i < len(li1):
        li[k] = li1[i]
        k += 1
        i += 1
    while j < len(li2):
        li[k] = li2[j]
        k += 1
        j += 1
def merge_sort(li):
    if len(li)==0 or len(li)==1:
        return
    mid=len(li)//2
    a=li[:mid]
    b=li[mid:]
    merge_sort(a)
    merge_sort(b)

    merge_func(li,a,b)

li=[5,2,22,8,97,7,6,22,5,1,26]
merge_sort(li)
print(li)



#_______________________________________________________________
"""s=[(1),(1,2,3),(2,2),(0,1),(2,1,0)]"""

def myfunc(li):
    new_list = []
    for i in li:
        l = len(i)
        i=sorted(i)
        for j in range(l - 1, -1, -1):
            if i[j] != l-1:
                new_list.append(False)
            l-=1
        else:
            new_list.append(True)

    if False in new_list:
        return False
    else:
        return True

n=int(input())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
print(li)
print(myfunc(li))