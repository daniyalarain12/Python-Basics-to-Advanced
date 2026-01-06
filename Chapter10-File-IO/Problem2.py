# WRITE A FUNCTION THAT REPLACE ALL OCCURENCES OF "JAVA" WITH "PYTHON" IN ABOVE FILE.

with open("D:\Python\practice.txt","r") as f:
    data = f.read()

new_data = data.replace("JAVA","PYTHON")
print(new_data)

with open("D:\Python\practice.txt","w") as f:
    f.write(new_data)
