#palindrome
st=input("enter the string")
l=len(st)
left=0
right=l-1
while left<right:
    if st[left]==st[right]:
        pal = True
        left+=1
        right-=1
    else:
            pal=False
            break
    if pal==True:
        print(st,"is palindraome")
    else:
        print(st,"is not palindrme")
        
        
