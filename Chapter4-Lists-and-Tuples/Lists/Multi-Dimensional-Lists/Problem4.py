# STUDENT MARKS SYSTEM
# STORE MARKS OF STUDENTS (ROWS = STUDENTS, COLUMNS = SUBJECTS)
# FIND:
#      1. AVERAGE PER STUDENT
#      2. TOPPER STUDENT

data = [
    [50,60,70,80,90],
    [60,67,80,90,100],
    [50,60,80,70,90],
    [80,90,70,80,90],
    [60,60,70,80,100]
]

result = []
for i in range(len(data)):
    std = data[i]
    sum , avg = 0 , 0
    for j in range(len(std)):
        sum += std[j]
    avg = sum / len(std)
    result.append(avg)
    print("AVERAGE OF STUDENT",(i+1), "IS :", avg)

max , pos = -1 , 0
for i in range(len(result)):
    if (result[i]>=max):
        max = result[i]
        pos = i + 1

print("TOPPER IS STUDENT ",pos, "WITH AVERAGE OF :", result[pos-1])
