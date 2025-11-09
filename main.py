from tools import Book
from tools import Library
from tools import Member


def main():
    lib = Library()

    while True:
        
        print("---------------- LMS SOFTWARE ----------------")
        print("Select One Of The Following Choices (1-6)\n")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            isbn = input("Enter Book ISBN: ")
            book = Book(title, author, isbn)
            lib.add_book(book)
            
        elif choice == "2":
            name = input("Enter Person Name: ")
            member_id = input("Enter Member ID: ")
            mem = Member(name, member_id)
            lib.add_member(mem)
            
        elif choice == "3":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the Book: ")
            lib.issue_book(member_id, isbn)
            
        elif choice == "4":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the Book: ")
            lib.return_book(member_id, isbn)
         
        elif choice == "5":
            lib.display_books()       
        
        else:
            break
                
                
if __name__ == "__main__":
    main()
