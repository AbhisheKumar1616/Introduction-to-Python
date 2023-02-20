def func(s):
    if s=="":
        return True
    if len(s)==1:
        if s=="a":
            return True
        else:
            return False
    if s[0]=="a":
        if s[1:3]=="bb":
            return func(s[3:])
        elif s[1]=="a":
            return func(s[1:])
        else:
            return False
    else:
        return False

s=input()
print(func(s))