def myfunc(n):
    if n<0:
        return 0
    if n==0:
        return 1

    a=myfunc(n-1)

    b=myfunc(n-2)

    c=myfunc(n-3)

    return a+b+c
n=int(input())
print(myfunc(n))
