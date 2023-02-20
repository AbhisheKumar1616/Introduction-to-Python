def myfun(n):
    if n<=1:
        return n
    ans=n
    i=1
    while i**2<=n:
        ans=min(ans,myfun(n-i**2))+1
        i+=1
    return ans
print((myfun(3)))