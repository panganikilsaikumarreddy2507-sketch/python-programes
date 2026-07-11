n=int(input("enter the number:"))
sum=0
temp=n
product = 1
while temp > 0:
    x=temp%10
    sum=sum+x
    product = product*x
    temp=temp//10
if sum==product:
    print("spy")
else:
    print("not")
