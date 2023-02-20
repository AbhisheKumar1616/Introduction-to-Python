Flag=True

while Flag:
    n=int(input())
    while n<=5 and n>0:
        if n==1:
            a=int(input())
            b=int(input())
            print(a+b)
            exit()
        elif n==2:
            a=int(input())
            b=int(input())
            print(a-b)
            break
        elif n==3:
            a=int(input())
            b=int(input())
            print(a*b)
            break
        elif n==4:
            a=int(input())
            b=int(input())
            print(a//b)
            break
        elif n==5:
            a=int(input())
            b=int(input())
            print(a%b)
            break
    if n==6:
        Flag=False
        exit()
    elif n>6 or n<0:
        print("Invalid Operation")