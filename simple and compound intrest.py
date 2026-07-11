#simple and compound intrest
import math
P=float(input("enter p:"))
t=float(input("enter t:"))
r=float(input("enter r:"))
si=(P*t*r)/100
ci=P+(1+(r/100))**t
print("simple inrest :",si)
print("compound intrest:",ci)
