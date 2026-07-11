#palindrom of a number
import math
n=int(input("enter the number:"))
temp=n
sum=0
while temp >0:
    x=temp%10
    sum=sum*10+x
    temp=temp//10
if n==sum:
    print("palindrome")
else:
    print("not")
print(sum)

