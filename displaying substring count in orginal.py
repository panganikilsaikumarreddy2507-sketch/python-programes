#displaing substring count in the originaln string
s1=input("enter orginal string")
sub_str=input("enter substring:")
s2=len(sub_str)
c=0
for i  in range(len(s1)-len(sub_str)+1):
    if s1[i:i+s2]==sub_str:
        c+=1
print(sub_str,"is present in ",s1,"for",c,"times")
