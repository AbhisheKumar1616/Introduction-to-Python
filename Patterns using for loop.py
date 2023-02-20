"""
    *
    **
    ***
    ****
"""

n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

"""
   1
  232
 34543
4567654
"""

n=int(input())
for i in range(1,n+1):
    for s in range(n-i,0,-1):
        print(" ",end="")
    k=i
    for j in range(1,i+1):
        print(k,end="")
        k+=1

    l=k-2
    for o in range(1,i):
        print(l,end="")
        l-=1

    print()

"""
1234
123
12
1
"""
n=int(input())
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end="")
    print()

"""
   1
  121
 12321
1234321
"""

n=int(input())
for i in range(1,n+1):
    for s in range(n-i,0,-1):
        print(" ", end="")
    for j in range(1,i+1):
        print(j,end="")
    k=i-1
    for m in range(1,i):
        print(k,end="")
        k-=1
    print()

"""
   *
  ***
 *****
  ***
   *
"""

n=int(input())
m=n//2+1
o=n//2
for i in range(1,m+1):
    for s in range(m-i,0,-1):
        print(" ", end="")
    for j in range(1,i+1):
        print("*",end="")
    for k in range(1,i):
        print("*",end="")
    print()
for i in range(1,o+1):
    for s in range(1,i+1):
        print(" ", end="")
    for j in range(o-i+1,0,-1):
        print("*",end="")
    for k in range(o-i,0,-1):
        print("*",end="")
    print()

"""
*00*00*
0*0*0*0
00***00
"""
n=int(input())
for i in range(1,n+1):
    for j in  range(1,n+1):
        if j==i:
            print("*",end="")
        else:
            print("0",end="")
    print("*",end="")
    k=n-i+1
    for j in range(1,n+1):
        if j==k:
            print("*",end="")
        else:
            print("0",end="")

    print()

"""
    1      1
    12    21
    123  321
    12344321
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for s in range(n-i,0,-1):
        print(" ",end=" ")
    k=i
    for j in range(k,0,-1):
        print(k,end="")
        k-=1
    print()

"""
*
 **
  ***
   ****
  ***
 **
*
"""
n = int(input())
m = n // 2 + 1
o = n // 2
for i in range(1, m + 1):
    for s in range(1, i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(1, o + 1):
    for s in range(o - i, 0, -1):
        print(" ", end="")

    for j in range(o - i + 1, 0, -1):
        print("*", end="")

    print()

"""

123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456

"""
n=int(input())
m=n-1
for i in range(1,n+1):
    for s in range(1,i):
        print(" ",end="")
    for j in range(i,n+1):
        print(j,end="")
    print()
for i in range(1,m+1):
    for s in range(m-i,0,-1):
        print(" ",end="")
    k=m-i+1
    for j in range(1,i+2):
        print(k,end="")
        k+=1
    print()

"""
4444444       4        444444
4333334       43       3333       4
4322234       432      22        34
4321234  =>   4321              234
4322234       432      2        234
4333334       43       333       34
4444444       4        44444      4
"""
n=int(input())
if n%2==0:
    l=n+2
else:
    l=n+1
q=n
for i in range(1,n+1):
    k=n
    for j in range(1,i+1):
        print(k,end="")
        k-=1
    for j in range(1,l+1):
        print(q,end="")
    k=n-i+2
    for j in range(1,i):
        print(k,end="")
        k+=1

    print()
    q-=1
    l-=2
l=1
for i in range(1,n):
    k=n
    for j in range(1,n-i+1):
        print(k,end="")
        k-=1
    q=i
    for j in range(1,l+1):
        print(q+1,end="")
    q=i
    for j in range(n-i,0,-1):
        print(q+1,end="")
        q+=1

    print()
    l+=2


"""
n=5
1   2   3   4   5
11  12  13  14  15
21  22  23  24  25
16  17  18  19  20
6   7   8   9   10

n=8
1   2   3   4   5   6   7   8
17  18  19  20  21  22  23  24
33  34  35  36  37  38  39  40
49  50  51  52  53  54  55  56
57  58  59  60  61  62  63  64
41  42  43  44  45  46  47  48
25  26  27  28  29  30  31  32
9   10  11  12  13  14  15  16

"""
import math
n = int(input())
for i in range(math.ceil(n/2)):
    for j in range(1, n+1):
        print(n*2*i + j, end=' ');
    print()

for i in range(n//2, 0, -1):
    for j in range(1, n+1):
        print(n*(2*i-1)+j, end=' ')
    print()

# -----------------------------------------------------------------------------------------
def print_rangoli(size):
    # your code goes here
    w = ord("a")
    for i in range(size - 1, -1, -1):
        s = ""
        for j in range(size - 1, i - 1, -1):
            s += chr(w + j)
        ss=""
        for j in range(size-1,i, -1):
            ss= chr(w+j)+ss
        s=s+ss
        s= ("-".join(s)).center(size + (size - 1) + (size * 2) - 2,"-")
        print(s)
    for i in range(1,size):
        s=""
        for j in range(i,size):
            s = chr(w + j)+s
        ss=""
        for j in range(size - 1, i, -1):
            ss= chr(w + j)+ss
        s=s+ss
        s = ("-".join(s)).center(size + (size - 1) + (size * 2) - 2, "-")
        print(s)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)