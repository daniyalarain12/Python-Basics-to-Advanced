# READING A FILE

# f.read()--> READS ENTIRE FILE.
# f.readline()--> READS ONE LINE AT A TIME.
# f.readlines() --> READS ALL LINES OF A FILE AND STORES EACH LINE AS A STRING IN A LIST.

f = open("demo.txt","r")
data1 = f.read()
data2 = f.read(10)                                # READS ONLY 10 CHARACTER
print(data1)
print(data2)
f.close()

try:                                           # Using try-except to handle FileNotFoundError because an error occurs if the file does not exist.
    f = open("daniyal.txt","r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError as e:
    print(e)

f = open("dani.txt","r")
line1 = f.readline()                              # READS 1ST LINE
print(line1)
line2 = f.readline()                              # READS 2ND LINE
print(line2)
f.close()

f = open("practice.txt","r")
data = f.read()                                   # WHEN WE USE read() BEFORE readline(), readline() WILL NOT READ ANY THING, BECAUSE ENTIRE FILE IS ALREADY READ BY read().
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

f = open("data2.txt","r")
line = f.readline()
print(line.strip().split(","))                  # Remove extra spaces/newline, split data by comma, and convert it into a list.
f.close()

f = open("data2.txt","r")
data = f.readlines()                        # READ ALL LINES FROM THE FILE AND STORE THEM IN A LIST.
print(data)
f.close()

f = open("data2.txt","r")
data = f.readlines()
for line in data:
    print(line)                             # READ ALL LINES AND PRINT EACH LINE ONE BY ONE, INCLUDING THE NEW LINE CHARACTER.
f.close()

f = open("data2.txt","r")
data = f.readlines()
for line in data:
    print(line.strip().split(","))          # READ ALL LINES, REMOVE EXTRA SPACES/NEWLINES, SPLIT DATA BY COMMA, AND CONVERT EACH LINE INTO A LIST.
f.close()
