"""
1
22
333
4444
"""
n=int(input("enrter n"))
for i in range(n+1):
    for j in range(i):
        print(i ,end=" ")  
    print(end="\n")

"""
1111
222
33
4
"""
print("second pattern")
for i in range( 1,n+1):
    for j in range(n-i+1):
        print(i ,end=" ")
    print(end="\n")
"""
    1
   22
  333
 4444
"""
print("third pattern")
for i in range(1,n+1):
    for j in range( 1,n+1-i):
      print(" " ,end=" ")  
    for k in range(n-i+1,n+1,1):
      print("*" ,end=" ")
    print(end="\n")

"""
1111
 333
  22
   1
"""
print("fourth pattern")
for i in range(n,0,-1):
   for j in range(n-i,0,-1):
      print(" ",end=" ")
   for k in range(i,0,-1):
      print( n-i+1, end=" ")
   print( end="\n")

#  
n= int(input("enter no for sum"))
i=1
sum=0
while(i<=n):
  #i=i*5
  sum=sum+i*5
  i=i+1
print("sum is ",sum) 

arr=list(map(int,input().split()))
print(arr)
large=arr[0]
seclarge=arr[1]
for i in range(1,len(arr)):
   if arr[i] > large:
     seclarge=large
     large=arr[i]
     if arr[i]>seclarge and arr[i]<large:
        seclarge=arr[i]
print("large elements is ",large)
print("seclargest element is ",seclarge)

"""
1
12
123
1234
"""
a=int(input("enter a"))
for i in range(1,a+1):
   for j in range(1,i+1):
     print(j ,end=" ")
   print(end="\n")

"""
1
2 3
4 5 6 
7 8 9 10

"""
x=1
b=int(input("enter b"))
for i in range(1,b+1):
   for j in range(0,i):
      print(x, end=" ")
      x=x+1
   print(end="\n")

"""
a
bb
ccc
dddd
"""
print("abc pattren")
x='a'
for i in range(n):
   for j in range(i):
      print(a ,end=" ")
   
   print(end="\n")

