#reverse of anumber
n=int(input("enter num:"))
temp=n
sum=0
while temp >0:
    x=temp%10
    sum=sum*10+x
    temp=temp//10
print("rverse of  a number:",sum)  
