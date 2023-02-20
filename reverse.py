#int
n=int(input())
b=0
while n!=0:
    a=n%10
    if(a==0):
        c=b/10
        if(c>0):
            b=b*10 + a
    else:
        b=b*10 + a
    n=n//10
print(b)

#string
n=input()
a=n[::-1]
print(a)

#reverse list using function
def reverse_list(li):
    n=len(li)
    for i in range(n//2):
        li[i],li[n-i-1]=li[n-i-1],li[i]

def rev(li):
    n=len(li)//2
    m=len(li)-1
    for i in range(n):
        a=li[i]
        li[i]=li[m-i]
        li[m-i]=a

li=[int(x) for x in input().split()]
reverse_list(li)
print(li)
rev(li)
print(li)

#reverse list using indexing
li=[int(x) for x in input().split()]
li=li[::-1]
print(li)