#Palindrome
from sys import stdin


def isPalindrome(string):
    # Your code goes here
    s = string[::-1]
    if s == string:
        return True
    else:
        return False


# main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')
#----------------------------------------------------------------------------
#Permutation
def charcount(s,sc,s1,sc1):
    c,c1=0,0
    for i in s:
        if i==sc:
            c+=1
    for i in s1:
        if i == sc1:
            c1 += 1

    return c,c1

def isPermutation(string1, string2):
    # Your code goes here
    for i in string1:
        if i not in string2:
            return False
        else:
            c1,c2=charcount(string1,i,string2,i)
            if c1!=c2:
                return False
    else:
        return True


from sys import stdin
def isPermutation(string1, string2):
    # Your code goes here
    for i in string1:
        if i not in string2:
            return False
    else:
        s1=sorted(string1)
        s2=sorted(string2)
        if s1==s2:
            return True


# main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans:
    print('true')
else:
    print('false')
#-------------------------------------------------------------------------
#remove consecutive duplicate

from sys import stdin


def removeConsecutiveDuplicates(string):
    # Your code goes here

    t = ""
    t += string[0]
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            t += string[i]

    return t


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
#--------------------------------------------------------------------------
#Reverse Each Word
from sys import stdin
def reverseEachWord(string):
    # Your code goes here
    sr = string[::-1]
    sr = sr.split()[::-1]
    t = ""
    for i in sr:
        t += i + " "
    return t


# main
string = stdin.readline().strip()
ans = reverseEachWord(string)
print(ans)
#-----------------------------------------------------------------------------
#removing char
from sys import stdin
def removeAllOccurrencesOfChar(string, ch):
    # Your code goes here
    t = ""
    for i in string:
        if i != ch:
            t += i
    return t
# main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]
ans = removeAllOccurrencesOfChar(string, ch)
print(ans)
#----------------------------------------------------------------------------------------
#Higest occuring Char
from sys import stdin
def highestOccuringChar(string):
    count = 0
    t = count
    for i in string:
        count = string.count(i)
        if count > t:
            t = count
            char = i
    return char
# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)
print(ans)
#----------------------------------------------------------------------------
#Compress the String
from sys import stdin
def getCompressedString(input) :
    input+=" "
    t=input[0]
    i=1
    c=1
    while i<len(input):
        if input[i]==input[i-1]:
            i+=1
            c+=1
            continue
        else:
            if c==1:
                t+=input[i]
            else:
                t+=str(c)+input[i]
            i+=1
            c=1
    return t

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
#-----------------------------------------------------------------------------------