# with SYNTAX

with open("D:\Python\Chapter7\dani.txt","r") as f:
    data = f.read()
    print(data)

with open("D:\Python\Chapter7\dani.txt","w") as f:
    f.write("HELLO! DANIYAL")
