# DYNAMIC ATTRIBUTE HANDLING USING __setattr__(name,value) AND __getattr__(name)
# THIS TECHNIQUE ALLOWS A GENERIC MECHANISM FOR SETTING AND GETTING ATTRIBUTES IN A CLASS. INSTEAD OF CREATING MULTIPLE SETTERS AND GETTERS FOR
# EACH ATTRIBUTE, WE CAN USE MAGIC METHODS TO HANDLE ATTRIBUTES DYNAMICALLY.

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""
    
    def __setattr__(self, name, value):               # USED TO SET VALUE OF ANY ATTRIBUTE IN THE CLASS
        super().__setattr__(name,value)

    def __getattr__(self, name):                      # USED TO GET VALUE OF AN ATTRIBUTE FROM THE CLASS
        return super().__getattribute__(name)

p1 = Person()

# SETTING VALUES USING __setattr__
p1.__setattr__("name","DANIYAL")
p1.__setattr__("age",20)
p1.__setattr__("gender","MALE")

# ACCESSING VALUES USING __getattr__
print(p1.__getattr__("name"))
print(p1.__getattr__("age"))
print(p1.__getattr__("gender"))
