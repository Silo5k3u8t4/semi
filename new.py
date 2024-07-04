import sys
import math
def convert(u):
    b=[]
    while u != 0:
        k = u % 2
        u //= 2
        b+=[k]
    if len(b) < 7:
        b+=[0]
    b.reverse()
    return b
def encode(b):
    new=[]
    i = 0
    h=''
    while i < len(b):
        if b[i] == 0:
            new.append("00 ")
        else:
            new.append("0 ")
        count = 1
        while i + 1 < len(b) and b[i] == b[i + 1]:
            count += 1
            i += 1
        new.append("0" * count)
        if i + 1 < len(b):
            new.append(" ")
        i += 1
    for p in new:
        h+=p
    return h

message = input()
q=0
x=[]

if(len(message)>1):
    while(q!=len(message)):
        x.extend(convert(ord(message[q])))
        q+=1
    print(encode(x))
else:
    x=convert(ord(message))
    print(encode(x))


num1 = int(input("Enter age of first person: "))
num2 = int(input("Enter age of second person: "))
num3 = int(input("Enter age of third person: "))

print("person1") if (num1 < num2 and num1 < num3) else print("person2") if (num2 < num1 and num2 < num3) else print("person3")

