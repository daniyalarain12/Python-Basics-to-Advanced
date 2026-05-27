# GIVEN A LIST OF TUPLES WITH info(name,subject):
# LIST ALL UNIQUE COURSES
# LIST STUDENTS ENROLLED IN ENGLISH
# CREATE DICTIONARY (STUDENT, SET OF COURSES)

info = [
    ("ALICE","MATH"),
    ("BOB","SCIENCE"),
    ("ALICE","SCIENCE"),
    ("CHARLIE","MATH"),
    ("BOB","MATH"),
    ("ALICE","ENGLISH"),
    ("CHARLIE","ENGLISH")
]

courses_set = set()
for tup in info:
    courses_set.add(tup[1])
print(courses_set)

for name, course in info:
    if course == "ENGLISH":
        print(name)

dict = {}
for name, course in info:
    if (dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
