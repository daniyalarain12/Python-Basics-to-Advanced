# Design and implement a Library Management System in Python using OOP concepts. Create a Book class with attributes
# title, author, pages, and type, and implement the magic methods __str__() to display book details, __len__() to return
# the total number of pages, and __add__() to return the combined pages of two books. Create an EBook class that inherits
# from Book and adds an additional attribute file_size, while overriding the __str__() method to include file size
# information. Implement a decorator named track_action_decorator that records the function name along with the current
# date and time into a file named library_logs.txt whenever a decorated function is executed. Then create a Library class
# that maintains separate lists for books, eBooks, available books, and available eBooks, and overload the += operator
# using __iadd__() to add books and eBooks into the library. Also implement borrowBook(title, type) and
# returnBook(title, type) methods decorated with track_action_decorator to manage borrowing and returning operations
# with appropriate success or error messages. Finally, create multiple Book and EBook objects, add them into the library,
# demonstrate all magic methods, perform borrow and return operations, and display the updated library records.

from datetime import datetime as dt

def track_action_decorator(func):
    def wrapper(*args,**kwargs):
        with open("library_logs.txt","a") as f:
            f.write(f"{dt.now()} :: {func.__name__} FUNCTION IS CALLED\n")
        return func(*args,**kwargs)
    return wrapper

class Book:
    def __init__(self, title:str, author:str, pages:int, type:str):
        self.title = title
        self.author = author
        self.pages = pages
        self.type = type

    def __str__(self):
        record = ""
        record += f"BOOK TITLE : {self.title}\n"
        record += f"BOOK AUTHOR : {self.author}\n"
        record += f"BOOK PAGES : {self.pages}\n"
        record += f"BOOK TYPE : {self.type}\n"
        return record
    
    def __len__(self):
        return self.pages
    
    def __add__(self, book2):
        return self.pages + book2.pages

class EBook(Book):
    def __init__(self, title:str, author:str, pages:int, type:str, file_size:float):
        super().__init__(title,author, pages, type)
        self.file_size = file_size
    
    def __str__(self):
        record = super().__str__()
        record += f"FILE SIZE : {self.file_size} MB\n"
        return record

class Library:
    def __init__(self):
        self.bookList = []
        self.eBookList = []
        self.availableBookList = []
        self.availableEBookList = []
    
    def __iadd__(self, other:object):
        if (other.type.lower() == "book"):
            self.bookList.append(other)
            self.availableBookList.append(other)
        elif (other.type.lower() == "ebook"):
            self.eBookList.append(other)
            self.availableEBookList.append(other)
        return self
    
    @ track_action_decorator
    def borrowBook(self, title, type):
        if (type.lower() == "book"):
            for book in self.availableBookList:
                if (book.title.lower() == title.lower()):
                    self.availableBookList.remove(book)
                    print("BOOK BORROWED SUCCESSFULLY")
                    break
            else:
                print("BOOK NOT FOUND")
        elif (type.lower() == "ebook"):
            for book in self.availableEBookList:
                if (book.title.lower() == title.lower()):
                    self.availableEBookList.remove(book)
                    print("E-BOOK BORROWED SUCCESSFULLY")
                    break
            else:
                print("BOOK NOT FOUND")

    @ track_action_decorator
    def returnBook(self, title, type):
        if (type.lower() == "book"):
            for book in self.bookList:
                if (book.title.lower() == title.lower()):
                    self.availableBookList.append(book)
                    print("BOOK RETURNED SUCCESSFULLY")
                    break
            else:
                print("BOOK NOT FOUND")
        elif (type.lower() == "ebook"):
            for book in self.eBookList:
                if (book.title.lower() == title.lower()):
                    self.availableEBookList.append(book)
                    print("E-BOOK RETURNED SUCCESSFULLY")
                    break
            else:
                print("BOOK NOT FOUND")

    def __str__(self):
        record = ""
        record += "TOTAL AVAILABLE BOOKS :\n"
        for book in self.availableBookList:
            record += book.title + "\n"
        record += "*"*20 + "\n"
        record += "TOTAL AVAILABLE E-BOOKS :\n"
        for book in self.availableEBookList:
            record += book.title + "\n"
        record += "*"*20
        return record

b1 = Book("DATA SCIENCE","DANIYAL ARAIN",200,"Book")
b2 = Book("ARTIFICIAL INTELLIGENCE","DANIYAL ARAIN",100,"Book")
eb1 = EBook("MACHINE LEARNING","DANIYAL ARAIN",300,"EBook", 25.5)
eb2 = EBook("DEEP LEARNING","DANIYAL ARAIN",500,"EBook", 25.5)

print(b1)
print(b2)

print("NO. OG PAGES IN eb1 :",len(eb1))
print("SUM OF PAGES OF b1 AND b2 :",b1+b2)

library = Library()
library += b1
library += b2
library += eb1
library += eb2
print(library)

library.borrowBook("DATA SCIENCE","BOOK")
print(library)

library.returnBook("DATA SCIENCE","BOOK")
print(library)
