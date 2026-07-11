n=int(input("VALUE:"))
a,b=0,1
print("fibonaci series:",end="")
for i in range(n+1):
    print(a,end="")
    a,b=b,a+b