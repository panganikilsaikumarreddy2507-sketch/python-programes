n=input("enter:")
x=len(n)
sum=0
for i in n:
    sum=sum+int(i)**x
print(sum)
if sum==int(n):
   print("it is amstrong number")
else:
       print("no")
   

