#factorial
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

n=int(input())
r=int(input())

n_fact=fact(n)
r_fact=fact(r)
nr_fact=fact((n-r))
c=n_fact//(r_fact*nr_fact)
print(c)

 #prime no
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

n=int(input())
a=isprime(n)
if a:
    print("Prime")
else:
    print("Not Prime")

#all prime no b/w 2 to n
n=int(input())
for i in range(2,n+1):
    a=isprime(i)
    if a:
        print(i," Prime")
    else:
        print(i," Not Prime")


#prime in range 2 to n
def isprimerange(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

n=int(input())
isprimerange(n)


#prime in range 2 to n
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return True
    return False

def isprimerange(n):
    for i in range(2,n+1):
        a=isprime(i)
        if a:
            print(i)

n=int(input())
isprimerange(n)