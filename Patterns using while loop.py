"""
    ****
    ****
    ****
    ****
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print("*",end=" ")
        j+=1
    print()
    i+=1



"""
    1111
    2222
    3333
    4444
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(i,end=" ")
        j+=1
    print()
    i+=1



"""
    1234
    1234
    1234
    1234
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(j,end=" ")
        j+=1
    print()
    i+=1



"""
    4321
    4321
    4321
    4321
"""
n=int(input())
i=1
while(i<=n):
    j=1
    m=n
    while(j<=n):
        print(m,end=" ")
        j+=1
        m-=1
    print()
    i+=1


"""
    4321
    4321
    4321
    4321
"""
n=int(input())
i=1
while(i<=n):
    j=0
    while(j<n):
        print(n-j,end=" ")
        j+=1
    print()
    i+=1


"""
    1
    12
    123
    1234
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j,end=" ")
        j+=1
    print()
    i+=1


"""
    1
    23
    345
    4567
"""
n=int(input())
i=1
while(i<=n):
    j=0
    while(j<i):
        print(i+j,end=" ")
        j+=1
    print()
    i+=1


"""
    1
    2 3
    4 5 6
    7 8 9 10
"""
n=int(input())
i=1
c=1
while(i<=n):
    j=1
    while(j<=i):
        print(c,end=" ")
        j+=1
        c+=1
    print()
    i+=1


"""
    1
    2 1
    3 2 1
    4 3 2 1
"""
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(i-j+1,end=" ")
        j+=1
    print()
    i+=1


"""
    ABCD
    ABCD
    ABCD
    ABCD
"""

n=int(input())
i=1
while i<=n:
    j=0
    while j<n:
        print(chr(ord('A')+j),end=" ")
        j+=1
    print()
    i+=1


"""
    ABCD
    ABCD
    ABCD
    ABCD
"""

v=input()
n=ord(v)-ord('A')+1
i=1
while i<=n:
    j=0
    while j<n:
        print(chr(ord('A')+j),end=" ")
        j+=1
    print()
    i+=1

"""
    ABCD
    BCDE
    CDEF
    DEFG
"""

n=int(input())
i=0
while i<n:
    j=0
    p=ord('A')+i
    while j<n:
        print(chr(p),end=" ")
        j+=1
        p+=1
    print()
    i+=1


"""
    ABCD
    BCDE
    CDEF
    DEFG
"""

n=int(input())
i=1
while i<=n:
    j=1
    p=ord('A')+i-1
    while j<=n:
        print(chr(p+j-1),end=" ")
        j+=1
    print()
    i+=1


"""
   1
  121
 12321
1234321
"""

n=int(input())
i=1
while i<=n:
    #space
    s=1
    while s<=n-i:
        print(" ",end="")
        s+=1
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    k=2
    p=i-1
    while k<=i:
        print(p,end="")
        k+=1
        p-=1
    print()
    i+=1


"""
   1
  121
 12321
1234321
"""

n=int(input())
i=1
while i<=n:
    #space
    s=1
    while s<=n-i:
        print(" ",end="")
        s+=1
    p=1
    j=1
    while j<=i:
        print(p,end="")
        p+=1
        j+=1
    k=i-1
    while k>=1:
        print(k,end="")
        k-=1
    print()
    i+=1


"""
   *
  ***
 *****
  ***
   *
"""

m=int(input())
if(m%2==0):
    n=m//2
    x=m//2
else:
    n=(m//2)+1
    x=m//2
i=1
while i<=n:
    #space
    s=1
    while s<=n-i:
        print(" ",end="")
        s+=1
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    k=2
    while k<=i:
        print("*",end="")
        k+=1
    print()
    i+=1

i=1
while i<=x:
    #space
    s=1
    while s<=i:
        print(" ",end="")
        s+=1
    j=x
    while j>=i:
        print("*",end="")
        j-=1
    k=x-i
    while k>=1:
        print("*",end="")
        k-=1
    print()
    i+=1


"""
    *000*000*
    0*00*00*0
    00*0*0*00
    000***000
"""

n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        if j==i:
            print("*",end="")
        else:
            print("0",end="")
        j+=1
    print("*", end="")
    k=n
    while k>=1:
        if k==i:
            print("*",end="")
        else:
            print("0",end="")
        k-=1
    print()
    i+=1


"""
n=odd 7
*
 **
  ***
   ****
  ***
 **
*
"""

n=int(input())
a=n//2+1
b=n//2
i=1
while(i<=a):
    j=1
    s=1
    while(j<=i):
        while s<=i-1:
            print(" ",end="")
            s+=1
        print("*",end="")
        j+=1
    print()
    i+=1
i=0
while i<b:
    j=b-i
    s=b-i
    while j>=1:
        while s>1:
            print(" ",end="")
            s-=1
        print("*",end="")
        j-=1
    print()
    i+=1

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
n = int(input())
m = n - 1
i = 1
while i <= n:
    j = i
    s = 1
    while j <= n:
        while s <= i - 1:
            print(" ", end="")
            s += 1
        print(j, end="")
        j += 1
    print()
    i += 1
i = 1
while i <= m:
    s = m - i
    while s >= 1:
        print(" ", end="")
        s -= 1
    j = m - i + 1
    while j <= m + 1:
        print(j, end="")
        j += 1
    print()
    i += 1


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
i=1
if n%2==0:
    l=n+2
else:
    l=n+1
q=n
while i<=n:
    j=1
    k=n
    while j<=i:
        print(k,end="")
        k-=1
        j+=1
    j=1
    while j<=l:
        print(q,end="")
        j+=1
    j=2
    k=n
    while j<=i:
        print(k-i+2,end="")
        k+=1
        j+=1

    print()
    i+=1
    l-=2
    q-=1
i=1
l=1
q=2
while i<n:
    j=1
    k=n
    while j<=n-i:
        print(k,end="")
        k-=1
        j+=1
    j=1
    while j<=l:
        print(q,end="")
        j+=1
    j=1
    k=i+1
    while j<=n-i:
        print(k,end="")
        j+=1
        k+=1

    print()
    i+=1
    l+=2
    q+=1

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
n=int(input())
m=math.ceil(n/2)
x=n//2

i=0
while i<m:
    j=1
    while j <= n:
        print((n*2*i)+j,end=" ")
        j+=1
    print()
    i+=1
i=x
while i>0:
    j=1
    while j<=n:
        print((n*(2*i-1)+j),end=" ")
        j+=1
    print()
    i-=1