#perfect number
import math
n = int(input("enter the number"))
sum=0
for i in  range(1,n):
    if n%i==0:
        sum=sum+i

if sum==n:
     print("pf")
else:
     print("no")
    
