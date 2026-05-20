# READING A FILE

# f.read()--> READS ENTIRE FILE.
# f.readline()--> READS ONE LINE AT A TIME.

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

f = open("D:\Python\Chapter8\data2.txt","r")
line = f.readline()
print(line.strip().split(","))                  # Remove extra spaces/newline, split data by comma, and convert it into a list
f.close()
