"""
a
bb
ccc
dddd
"""
x=97
n=int(input())
for i in range(n):
    for j in range(i+1):
     print(chr(x),end=" ")
    x+=1
    print(end="\n")
#also
    a=97
for i in range(1,n+1):
    for j in range(1, i+1):
        print("%c" %(a), end=" ")  #%c to represent char value 
    a +=1
    print()


"""
a
ab
abc
abcd

"""
n=int(input("enter n for pattern"))
x=97
for i in range(n):
   for j in range(i+1):
      print(chr(x+j),end=" ")  
   print()

"""
a
bc
def
ghij

"""
x=97
n=int(input())
for i in range(n):
    for j in range(i+1):
     print(chr(x),end=" ")
     x+=1
    print(end="\n")


    



