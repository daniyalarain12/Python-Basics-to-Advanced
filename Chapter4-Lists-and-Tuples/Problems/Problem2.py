#WRITE A PROGRAM TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.

list = [1, 2, 1]
copy_list = list.copy()
copy_list.reverse()
if(list == copy_list):
    print("LIST CONTAINS A PALINDROME OF ELEMENTS.")
else:
    print("LIST DOES NOT CONTAINS A PALINDROME OF ELEMENTS.")
