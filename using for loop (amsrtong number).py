#amstong number
n=input("enter a number:")
l=len(n)
sum=0
for i in n:
    sum+=int(i)**l
if int(n)==sum:
    print(n,"is amrstrong number")
else:
    print(n,"not a amstrong number")
