#column with largest sum
li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n,m=3,4
i=0
sum_l=[]
for j in range(m):
    su=0
    for i in li:
        su+=i[j]
    sum_l.append(su)
m=max(sum_l)
i=sum_l.index(m)
print(i,m)
#---------------------------------------------------------------------------------
#largest row or column
'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin


def findLargest(arr, n, m):
    max_r,max_c=-2147483648,-2147483648
    pos_r,pos_c=0,0
    if n==0 and m==0:
        print("row " + str(pos_r) + " " + str(max_r))
        return
    #largest row value
    for i in arr:
        su=sum(i)
        if su>max_r:
            max_r=su
            pos_r=arr.index(i)


    #largest col val
    for j in range(m):
        s=0
        for i in arr:
            s+=i[j]
        if s>max_c:
            max_c=s
            pos_c=j


    if max_r>=max_c:
        print("row " + str(pos_r) + " " + str(max_r))
    else:
        print("column " + str(pos_c) + " " + str(max_c))


# Your code goes here


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
#--------------------------------------------------------------------------------------------
#wave patern
from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    st=""
    for j in range(mCols):
        if j%2==0:
            for i in mat:
                st=st+str(i[j])+" "
        else:
            for k in range(nRows-1,-1,-1):
                st=st+str(mat[k][j])+" "
    print(st)


#Taking Iput Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0 :
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
#------------------------------------------------------------------------------------------------
#spiral
from sys import stdin


def spiralPrint(mat, n, m):
    rs,cs=0,0
    re,ce=n-1,m-1
    st=""
    count=0
    len_list=n*m
    while count!=len_list:
        for i in range(cs,ce+1):
            st=st+str(mat[rs][i])+" "
            count+=1
        rs+=1
        for i in range(rs,re+1):
            st=st+str(mat[i][ce])+" "
            count+=1
        ce-=1
        for i in range(ce,cs-1,-1):
            st=st+str(mat[re][i])+" "
            count+=1
        re-=1
        for i in range(re,rs-1,-1):
            st=st+str(mat[i][cs])+" "
            count+=1
        cs+=1

    print(st)



# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
#-----------------------------------------------------------------------------------------------------