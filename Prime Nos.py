# prime1
n = int(input())
i = 1
c = 0
while (i <= n):
    if (n % i == 0):
        c += 1
        i += 1
    else:
        i += 1
if (c == 2):
    print("Prime")

# prime2
n = int(input())
i = 2
c = 0
while (i <= n):
    if (n % i == 0):
        c += 1
        i += 1
    else:
        i += 1
if (c == 1):
    print("Prime")

# prime3
n = int(input())
i = 2
c = 0
while (i < n):
    if (n % i == 0):
        c += 1
        i += 1
    else:
        i += 1
if (c == 0):
    print("Prime")

# prime4
n = int(input())
i = 2
Flag = False
while (i < n):
    if (n % i == 0):
        Flag = True
        break
    i += 1
if Flag:
    print("Not Prime")
else:
    print("Prime")

# prime5 (All prime b/w 2.....n)
n = int(input())
i=2
while (i < n):
    j = 2
    Flag = False
    while(j<i):
        if (i % j == 0):
            Flag = True
            break
        j += 1
    if not Flag:
        print("Prime {}".format(i))

    i+=1
#all prime b/w 2 to n
n=int(input())
i=2
while i<=n:
    j=2
    f=True
    while j<i:
        if i%j==0:
            f=False
            break
        j+=1
    if f:
        print(i)
    i+=1

#all prime b/w 2 to n
n=int(input())
for i in range(2,n+1):
    f=True
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        print(i)