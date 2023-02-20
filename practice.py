#swapping alternate
def swapal(arr,n):
    for i in range(0,n-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)

n=int(input())
for i in range(n):
    l=int(input())
    li=[int(x) for x in input().split()]
    swapal(li,l)

#unique no
import sys

def findUnique(arr, n) :
    #Your code goes here
    for i in range(n):
        for j in range(n):
            if i!=j:
                if arr[i]==arr[j]:
                    break
        else:
            return arr[i]


#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1

#duplicate no
import sys

def findUnique(arr, n) :
    #Your code goes here
    for i in range(n):
        for j in range(n):
            if i!=j:
                if arr[i]==arr[j]:
                    return arr[i]


#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1

#find intersection points
import sys

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    for i in range(n):
        for j in range(m):
            if arr1[i]==arr2[j]:
                print(arr1[i],end=" ")
                arr2[j]=0
                break

#Taking Input Using Fast I/O

def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1


#pair sum
from sys import stdin

def pairSum(arr, n, x):
    c=0
    arr.sort()
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==x:
                c+=1
    return c


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1

#triplet sum

from sys import stdin

def findTriplet(arr, n, x) :
    #Your code goes here
    arr.sort()
    c=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==x:
                    c+=1
    #return your answer
    return c



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1