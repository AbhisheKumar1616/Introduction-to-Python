"""Sum of string number"""
def myfunc(li):
    if len(li)==1:
        return int(li[0])
    return int(li[0])+myfunc(li[1:])
def str_sum(s):
    a=" ".join(s).split()
    return myfunc(a)

print(myfunc("123"))

#-----------------------------------------------------------------------------------
"""Sum of digits of a number"""
def myfun(n):
    if n<=9 and n>=0:
        return n
    return n%10 + myfun(n//10)
print(myfun(333))

#------------------------------------------------------------------------------------
"""Harmonic sum ==> 1+(1/2)+(1/3)+......(1/n-1)"""
def myfun(n):
    if n==1:
        return 1
    return 1/n + myfun(n-1)
print(f"{myfun(3):.2f}")

#---------------------------------------------------------------------------------------
"""Reverse an array"""
def rev(li,i):
    if i>=len(li)//2:
        return
    li[i],li[len(li)-i-1]=li[len(li)-i-1],li[i]
    rev(li,i+1)

li=[1,2,3,4,5,6]
rev(li,0)
print(li)

def rev(li):
    if len(li)==1:
        return li
    a=[li[len(li)-1]]
    return a + rev(li[:len(li)-1])

li=[1,2,3,4]
print(rev(li))
#--------------------------------------------------------------------------------------------
"""string Reverse"""
def rev(s):
    if len(s)==0:
        return s
    a=s[len(s)-1]
    return a+rev(s[:len(s)-1])
print(rev("abcd"))

#---------------------------------------------------------------------------------------------
#Palindrom String
def rev(s,i=0,f=True):
    if i>=len(s)//2:
        return f
    if s[i]!=s[len(s)-i-1]:
        return False
    i+=1
    return rev(s,i,True)
print(rev("ababaca"))
