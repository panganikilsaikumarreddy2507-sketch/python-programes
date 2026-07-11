n=list(map(int,input("enter a numbers :").split()))
#by using list comhenzion
n1=[n[i] for i in range(len(n)) if n[i]%2==0]
print(n1)

       
