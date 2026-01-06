# WRITE A PROGRAM THAT SEARCHES IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT.

f = open("D:\Python\practice.txt","r")
data = f.read()

if(data.find("LEARNING") != -1):
    print("TARGET FOUND")
else:
    print("TARGET NOT FOUND")
    
f.close()
