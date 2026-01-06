# FILE I/O IN PYTHON
# PYTHON CAN BE USED TO PERFORM OPERATIONS ON A FILE. (READ AND WRITE DATA)
# TYPES OF FILES
# 1. TEXT FILES: .txt, .docx, .csv etc
# 2. BINARY FILES: .png, .mp3, .mp4, .jpeg etc

# OPEN, READ AND CLOSE FILE
# WE HAVE TO OPEN A FILE BEFORE READING OR WRITING.

f = open("D:\Python\Chapter7\demo.txt","r")           # f = open("file name","mode")
data = f.read()
print(data)
print(type(data))
f.close()

# CHARACTERS      | MEANING
#     r           | READ MODE --> OPEN FOR READING (DEFAULT).
#     w           | WRITE MODE --> OPEN FOR WRITING (RE-WRITING), TRUNCATING THE FILE FIRST.
#     a           | APPEND MODE --> OPEN FOR WRITING, APPENDING TO THE END OF THE FILE.
