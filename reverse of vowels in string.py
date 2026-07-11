#reverse of a vowels in strings
s="icecream"
v="aeiouAEIOU"
s1=list(s)
print(s1)
left,right=0,len(s1)-1
while left<right:
    if s1[left]not in v:
        left+=1
    if s1[right]not in v:
        right-=1
    else:
        s1[left],s1[right]=s1[right],s1[left]
        left+=1
        right-=1
print("".join(s1))
    
    
