# CREATE A STUDENT class THAT TAKE NAME AND MARKS OF 3 SUBJECTS AS AN ARGUMENTS IN CONSTRUCTOR. THEN CREATE A METHOD TO PRINT THE AVERAGE.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def cal_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(self.name,"YOUR AVGEARGE IS :",sum/3)

s1 = Student("DANIYAL",[99,98,97])
s1.cal_avg()
s1.name = "DANIYAL ARAIN"
s1.cal_avg()
