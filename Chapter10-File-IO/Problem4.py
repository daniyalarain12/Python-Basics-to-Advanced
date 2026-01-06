# WRITE A FUNCTION TO FIND IN WHICH LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST. PRINT -1 IF NOT FOUND.

def check():
    word = "LEARNING"
    count = 1
    data = True
    with open("D:\Python\practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(count)
                return
            count += 1

    return -1

print(check())
