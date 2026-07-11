'''string MATCHING in a array'''
r=[]
words=list(input("enter string:").split())
for i in range(len(words)):
    for j in range(len(words)):
        if i!=j and words[i]in words[j]:
            r.append(words[i])
            break
print(r)
