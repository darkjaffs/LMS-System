
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
            print("Book Has Been Successfully Borrowed")
            
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
            print(f"Book {book.title} has been succesfully borrowed by {self.name} with Member ID: {self.member_id}")
        else:
            print("Book is not available")
            
    def return_book(self, book=Book):
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
            book.return_book()
        else:
            print("Book is not borrowed by this person")
            
    def __str__(self):
        borrowedTitle = ", ".join([books.title for books in self.borrowedBooks])
        return f"Member Name: {self.name} | Member_ID: {self.member_id} | Borrowed Books: {borrowedTitle}"
            
            
    
    
book1 = Book("Percy Jackson", "Rick Riordan", 11223344)
book2 = Book("Pokemon", "Japs", 33224455)

member1 = Member("Huraira", "1")
member2 = Member("Jaffs", "2")

print(member1)

member1.borrow_book(book1)

print(member1)
    
member1.return_book(book1)   
        
print(member1)       

member2.return_book(book1)   