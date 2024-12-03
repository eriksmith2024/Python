
#LIBRARY EXERCISE MY PSEUDOCODE
# books & members & library are objects
#classify books
    #detail properties of books including title author & whether borrowed
    #detail any methods / actions of books if any??? think status available or not may be

#Define members
    #detail member properties including name ID & record of any bowrrowed books
    #detail of member actions / methods i.e. borrow or return books

#Implement a library class to manage the books - library will have actions / methods i.e. notify users book is overdue or not available (Car reverse go forward starte engine)
#Implemet class Methods ??? Think means make the libray do its actions???
#add extra actions /  methods for libray to add new books and members
# Add extra actions / methods for library to lend book to members and process returns

#MY SECOND ATTEMPT ALL WRITTEN BY ME FOLLOWING EXERCISE INSTRUCTIONS
class Library:
    def __init__(self, manager,):
        self.manager = manager
        
    def register(self):
        input('Please complete registration details, name, age, address')
    def loanbook (self):
        input("Provide details of book title and author,")
    def bookreturn (self):
        input("Provide " + author + "and " + title)

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

class Member:
    def __init__(self, fullName, memberID, borrowedBooks):
        self.fullName = fullName
        self.memberID = memberID
        self.borrowedBooks = borrowedBooks
           

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}"




   

