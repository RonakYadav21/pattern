"""
   *
  * *
 * * *
* * * *


"""
n =int(input("enter n"))
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" " ,end=" ")
    for k in range(1,i+1):
           print("*", end="   ")
    print()


"""
 * * * *
  * * *
   * *
    *
    
"""
n=int(input("enter no"))

for i in range(n+1,1,-1):
     for j in range(n+1-i,0,-1):
          print(" ",end=" ")
     for k in range(1,i):
          print("*" ,end="   ")
     print()



    #pascal  traingle
     """
       1
      1 1
     1 2 1
   1 4  6  1 
     
     """
n=int(input("enter n"))
for i in range(1,n+1):
     x=1
     for j in range(1,n+1-i):
             print(" ",end=" ")
     for k in range(i) :
         print(x,end=" ") ; 
         x=x*(i-j)//j
     print()


"""
**** ****
***   ***
**     **
*       *
*       *
**     **
***   ***
**** ****
"""
n =int(input("enter n"))
for i in range(n):
     for j in range(2*n):
          if i+j< n:
               print("*",end=" ")
          else:
               print(" " ,end=" ")
          if i+n<=j:
               print("*" ,end=" ")
          else:
               print(" ",end=" ")    
     
     print()
      
for i in range(n):
     for j in range(2*n):
          if j<=i:
               print("*",end=" ")
          else:
               print(" ", end=" ")
          if i>=(2*n-i)-j:
             print("*" ,end=" ")
          else: 
             print(" ",end=" ")
     print()

     
