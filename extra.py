def printUncommon(arr1, arr2, n1, n2):
    i = 0
    j = 0
    f = True
    count=0
    while i<=len(arr1)-1:
        while j<=len(arr2)-1:
            if arr1[i] == arr2[j]:
                f=False
                break
            j+=1
        if f:
            count+=1
        else:
            f=True
        i+=1
    return count
# Driver code

arr1 = [10, 20, 30]

arr2 = [20, 25, 30, 40, 50]

n1 = len(arr1)

n2 = len(arr2)

count=printUncommon(arr1, arr2, n1, n2)
print(count)