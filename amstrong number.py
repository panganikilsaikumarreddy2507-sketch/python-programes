#amstrong number
import  math
n=int(input("enter the number :"))
l=len(str(n))
sum=0
temp=n
while n > 0:
    x=n%10
    sum+=x**l
    n=n//10
if temp==sum:
    print("it is amstrong number:")
else:
    print("not a amstong number")
print(sum)
    
