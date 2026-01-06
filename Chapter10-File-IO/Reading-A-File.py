# READING A FILE

# f.read()--> READS ENTIRE FILE.
# f.readline()--> READS ONE LINE AT A TIME.

f = open("D:\Python\Chapter7\demo.txt","r")
data1 = f.read()
data2 = f.read(10)                                # READS ONLY 10 CHARACTER
print(data1)
print(data2)
f.close()

f = open("D:\Python\Chapter7\dani.txt","r")
line1 = f.readline()                              # READS 1ST LINE
print(line1)
line2 = f.readline()                              # READS 2ND LINE
print(line2)
f.close()

f = open("D:\Python\Chapter7\practice.txt","r")
data = f.read()                                   # WHEN WE USE read() BEFORE readline(), readline() WILL NOT READ ANY THING, BECAUSE ENTIRE FILE IS ALREADY READ BY read().
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()
