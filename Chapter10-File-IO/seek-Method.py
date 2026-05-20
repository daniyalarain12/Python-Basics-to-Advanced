# seek() METHOD
# Used to move the file cursor to a specific position.

# r+ MODE
with open("D:\Python\Chapter8\data4.txt","r+") as f:
    data = f.read()
    end = len(data)
    f.seek(end)            # Move cursor to the end of the file
    f.write("DANIYAL")     # Add new data at the end of the file

# w+ MODE
with open("D:\Python\Chapter8\data4.txt","r+") as f:
    f.write("DANIYAL")
    f.seek(0)                # Move cursor back to the start for reading
    data = f.read()
    end = len(data)

# a+ MODE
with open("D:\Python\Chapter8\data4.txt","a+") as f:
    f.seek(0)                # Move cursor to the start for reading data
    data = f.read()
    end = len(data)
