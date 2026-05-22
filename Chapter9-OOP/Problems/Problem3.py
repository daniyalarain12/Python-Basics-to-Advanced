# Design a Python program OOP to manage a list of students by defining a Student class to store student details such as name, father name, and ID, 
# and a ListOfStudents class to manage multiple student objects by providing functionalities to add a student, remove a student by index, 
# and display all students; also demonstrate the use of type hints in methods to specify parameter and return types, and finally create at least 
# three student objects, add them to the list, display all students, remove one student, and then display the updated list.

class Student:
    def __init__(self,name, fName, id):
        self.name = name
        self.fName = fName
        self.id = id

    def print_std(self):
        print(f"NAME : {self.name}, FATHER NAME : {self.fName} AND ID : {self.id}")

class listOfStudents:
    def __init__(self):
        self.stdList = []

    def addStudent(self, std) -> None:
        self.stdList.append(std)

    def removeStudent(self, index:int) -> Student:
        return self.stdList.pop(index)
    
    def printAllStudents(self) -> None:
        for std in self.stdList:
            std.print_std()

std1 = Student("DANIYAL ARAIN","GHULAM SHABBIR","24SW039")
std2 = Student("NABEEL","SHAHID","24SW038")
std3 = Student("IBRAR","SAEED","24SW024")

stdList = listOfStudents()

stdList.addStudent(std1)
stdList.addStudent(std2)
stdList.addStudent(std3)

stdList.printAllStudents()
print("*"*70)

print("REMOVED STUDENT:")
deltedStd = stdList.removeStudent(1)
deltedStd.print_std()
print("*"*70)

stdList.printAllStudents()
