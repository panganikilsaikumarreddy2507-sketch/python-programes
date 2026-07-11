#printing squares of a number
import math
start=int(input("enter  the starting number:"))
end=int(input("enter the end number:"))
for i in range(start,end+1):
    print("square of ",i,"is",i*i)
    i+=1
