#printing the piramidal numbers
n= int(input("enter n value:"))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,sep='',end='')
   
    for l in range(i-1,0,-1):
        print(l,sep='',end='')
    print("")
    

