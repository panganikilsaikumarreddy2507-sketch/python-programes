n=int(input("enter matrix order:"))
m=tuple(tuple(map(int,input().split()))for _ in range(n))
trace=0
for i in range(n):
    trace+=m[i][i]
print("trace =",trace)


