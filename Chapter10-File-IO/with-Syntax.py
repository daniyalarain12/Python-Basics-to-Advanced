# with SYNTAX

with open("dani.txt","r") as f:
    data = f.read()
    print(data)

with open("dani.txt","w") as f:
    f.write("HELLO! DANIYAL")
