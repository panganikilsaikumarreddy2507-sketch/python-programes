#count number of vowels consonats and digits in a
s=input("enter string:")
v="aeiouAEIOU"
v_c=0
c_c=0
d_c=0
for i in s:
    if i in v:
        v_c+=1
    elif i.isalpha():
        c_c+=1
    elif i.isdigit():
        d_c+=1
print("no.of vowels: ",v_c)
print("no.of consonants: ",c_c)
print("no.of digits: ",d_c)
