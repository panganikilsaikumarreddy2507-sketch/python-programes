#spy number
n=input("enter  anumber")
l=len(n)
sum=0
product=1
for i in n:
    sum=sum+int(i)
    product=product*int(i)
if sum==product:
    print("correct")
else:
    print("no")
