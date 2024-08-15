
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


#Define the book class

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.is_available = True

#     def __str__(self):
#         return f"'{self.title}' by {self.author} - {'Available' if self.is_available else 'Not Available'}"

# #Define the member class MY ATTEMPT

# class Member:
#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.borrowed_books = []
    
#     def borrow_book(self, book):
#         if book.is_available: 
#             self.borrowed_books.append(book)
#             book.is_available = False
#             return True
#         return False
 
#     def return_book(self, book):
#         if book in self.borrowed_books:
#             self.borrowed_books.remove(book)
#             book.is_available = True
#             return True
#         return False

#     def __str__(self):
#         borrowed_books_titles = ','.join([book.title for book in self.borrowed_books])
#         return f"Member: {self.name},ID: {self.member_id}, Borrowed books: {borrowed_books_titles if borrowed_books_titles else 'None'}                    

#USING CHAT GPT           
def add_book(self, book): # addds book to the library collection
    self.books.append(book)
    print(f"Book added: {book}")

def register_member(self, member):#registers a new member
    self.members.append(member)
    print(f"Member registered: {member}")

def lend_book(self, book_title, member_id): # lend book action
    book = next((b for b in self.books if b.title == book_title and b.available), None)
    member = next((m for m in self.members if m.member_id == member_id), None)

    if book and member:
        book.available = False
        member.borrowed_books.append(book)
        print(f"Book '{book_title}' lent to member {member_id}")
    else:
        print("Book or member not found, or book not available")

def return_book(self, book_title, member_id): # return book action
    member = next((m for m in self.members if m.member_id == member_id), None)
    
    if member:
        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        
        if book:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"Book '{book_title}' returned by member {member_id}")
        else:
            print(f"Book '{book_title}' not found in member {member_id}'s borrowed books")
    else:
        print(f"Member with ID {member_id} not found")
