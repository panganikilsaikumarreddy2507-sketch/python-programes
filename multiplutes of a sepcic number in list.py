n=list(map(int,input("enter :_").split()))
a=int(input("enter a number:"))
#by using list comhenzion
n1=[n[i] for i in range(len(n)) if n[i]%a==0]
print(n1)
