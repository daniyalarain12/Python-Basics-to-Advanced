# FROM A FILE CONTAINING NUMBERS SEPARATED BY COMMA, PRINT THE COUNT OF EVEN NUMBERS.

with open("D:\Python\practice.txt","r") as f:
    data = f.read()

    list = data.split(",")
    print(list)
    count = 0
    
    for i in list:
        if(int(i) %2 == 0):
            count += 1
    print("COUNT :",count)
