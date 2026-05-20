# WRITING TO A FILE

f = open("dani.txt","w")         # OVERWRITES THE ENTIRE FILE
f.write("I AM DANIYAL ARAIN.")

f = open("dani.txt","a")         # ADDS TO THE FILE
f.write("\nI AM LEARNING PYTHON.")

f.close()

# f.writelines() ---> Writes a list of strings into a file (does not add new line automatically).

listData = ["DANIYAL,GHULAM SHABBIR,03092313464,daniyalarain123786@gmail.com,da12\n",
            "SAMI,GHULAM SAGHEER,03492313464,samiarain123786@gmail.com,sa29"]

with open("data.csv","w") as f:
    f.writelines(listData)
