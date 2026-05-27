# WRITE A FUNCTION WHICH TAKES A NUMBER "n" AS INPUT FROM THE USER AND THEN CHECK IF A NUMBER IS EVEN OR ODD.

def check():
    n = int(input("ENTER ANY NUMBER : "))
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")

check()
