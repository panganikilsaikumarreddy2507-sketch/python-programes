try :
    with open("data.txt","r") as f:
        content=f.read()
        print("file content :")
        print(content)
except FileNotFoundError :
    print("file not found")

