# WRITING TO A FILE

f = open("dani.txt","w")         # OVERWRITES THE ENTIRE FILE
f.write("I AM DANIYAL ARAIN.")

f = open("dani.txt","a")         # ADDS TO THE FILE
f.write("\nI AM LEARNING PYTHON.")

f.close()
