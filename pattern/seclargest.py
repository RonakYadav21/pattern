arr=list(map(int,input().split()))
print(arr)
large=arr[0]
seclarge=arr[1]
for i in range(1,len(arr)):
   if arr[i] > large:
     seclarge=large
     large=arr[i]
   elif arr[i]>seclarge:
        seclarge=arr[i]
print("large elements is ",large)
print("seclargest element is ",seclarge)


# 1+2/2!+3/3!....+n/n!

n=int(input("enter n"))
def factorial(i):
   if i==1 or i==0:
      return 1
   else:
      return i*factorial(i-1)
   
sum=0
for i in range(n+1):
  sum=sum+i/factorial(i)

print("sum of the series upto n is ",sum)

   





