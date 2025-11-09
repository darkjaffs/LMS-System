
class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) | Available: {self.available}"
        
    def borrow(self):
        if self.available == False:
            print('Book not availabe')
        else:
            self.available = False
            
    def return_book(self):
        if self.available == False:
            self.available = True
            print('Book Has Been Returned')
        else:
            print("Book Already Exists")
            
class Member: 
    
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowedBooks = []
        
    def borrow_book(self, book=Book):
        if book.available == True:
            self.borrowedBooks.append(book)
            book.borrow()
            print(f"Book {book.title} Has Been Succesfully Borrowed By {self.name} With Member ID: {self.member_id}")
        else:
            print("Book is Not Available")
            
    def return_book(self, book=Book):
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
            book.return_book()
        else:
            print("Book is Not Borrowed By This Person")
            
    def __str__(self):
        borrowedTitle = ", ".join([books.title for books in self.borrowedBooks])
        return f"Member Name: {self.name} | Member_ID: {self.member_id} | Borrowed Books: {borrowedTitle}"
            
class Library(Book, Member):
    
    def __init__(self):
        self.books=[]
        self.members = []
        
    def add_book(self, book=Book):
        if book not in self.books:
            self.books.append(book)
            print(f"{book.title} Has Been Added To Library")
        else:
            print(f"{book.title} Already Exists")      
            
    def add_member(self, member=Member):
        if member not in self.members:
            self.members.append(member)
            print(f"{member.name} Has Been Added To Member List")
            
        else:
            print(f"{member.name} Already Exists")     
            
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
            
    def issue_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        
        if member and book:
            member.borrow_book(book)
        else:
            print("Member or Book Not Found")
    
    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book =self.find_book(isbn)
        
        if member and book:
            member.return_book(book)
        else:
            print("Member or Book Not Found")
    
    def display_books(self):
        print("Current Book in Library:")
        for book in self.books:
            print(book)
            
    
        
    
lib = Library()

# Add books
b1 = Book("1984", "George Orwell", 123)
b2 = Book("The Alchemist", "Paulo Coelho", 456)
lib.add_book(b1)
lib.add_book(b2)

# Add members
m1 = Member("Ali", "M001")
lib.add_member(m1)

# Issue book
lib.issue_book("M001", 123)

# Return book
lib.return_book("M001", 123)

# Display books
lib.display_books()
