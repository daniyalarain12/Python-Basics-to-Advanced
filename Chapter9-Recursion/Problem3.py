# WRITE A RECURSIVE FUNCTION TO PRINT ALL ELEMENTS IN A LIST.

def print_list(list,n=0):
    if(n == len(list)):
        return
    print(list[n], end = " ")
    print_list(list,n+1)

fruits = ["MANGO","ORANGE","APPLE","BANANA"]
print_list(fruits)
