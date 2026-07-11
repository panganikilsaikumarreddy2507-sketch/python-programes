#no of digits in a number
n=int(input("enter number:"))

temp=n
sum=0
while temp > 0:
    x=temp%10
    sum=sum+1
    temp=temp//10
print(sum)
