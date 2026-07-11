#linear search
   
n=list(map(int,input("enter list of values :").split()))
target= int(input("enter traget value :"))
found=0
for i in range(len(n)):
    if target==n[i]:
        found=1
        break
if found==1:
    print(target, " is persent in ",i,"position")
else:
    print(target, "not found")
