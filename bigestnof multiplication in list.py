'''product of 3 maximum numbers'''
lst=list(map(int,input("enter:").split()))
lst.sort()
print(lst)
p1=lst[-1]*lst[-2]*lst[-3]
p2=lst[0]*lst[1]*lst[-1]
print(p1,p2)
print(max(p1,p2))


