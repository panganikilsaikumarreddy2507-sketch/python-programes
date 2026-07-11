#linear search
n=list(map(int,input("enter the list of values :").split()))
key=int(input("enter the value :"))
found=0
for i in range(len(n)):
    if key==n[i]:
        found=1
        break
if found==1:
    print("yes")
else:
    print("no")
