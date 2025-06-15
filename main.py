class Book :
    def __init__ (self,book_number,name,author,genre):
        self.book_number = book_number
        self.name = name
        self.author = author
        self.genre = genre

    def __str__(self) :
        return f"Book Number: {self.book_number}\nName: {self.name}\nAuthor: {self.author}\nGenre: {self.genre}"
     



class Library : 
    def __init__ (self):
        self.books = []
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.name}' added successfully")

    def list_books(self):
        if not self.books:
            print("No books availble in the Library")
            return

        print("\nList of books in the library:\n")
        for book in self.books:
            print(book)
            print("-" * 40)

    def remove_book(self,book_number):
        for book in self.books:
            if book.book_number == book_number:
                self.books.remove(book)
                print(f"Book named '{book.name}' removed!!!")
                return
        print("Book not found")
        

    def give_book(self,book_number):
        for book in self.books:
            if book.book_number == book_number:
                self.books.remove(book)
                print(f"Book '{book.name}' has been given to the reader.")
                return
        print("Book not available for lending.")

    def return_book (self,book):
        self.books.append(book)
        print(f"Book '{book.name}' has been returned.")



library = Library()


while True:
    print("\nWelcome to the Library Management System 📚")
    print("1. Add a Book")
    print("2. List All Books")
    print("3. Remove a Book")
    print("4. Give a Book")
    print("5. Return a Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
       try:
          book_number = int(input("Enter Book Number: "))
          name = input("Enter Book Name: ")
          author = input("Enter Author Name: ")
          genre = input("Enter Genre: ")

          book = Book(book_number,name,author,genre)
          library.add_book(book)
       except ValueError:
          print("Invalid input. Book number must be a number.")

    elif choice == '2':
        library.list_books()
       

    elif choice == '3':
       try:
            book_number = int(input("Enter Book Number: "))
            library.remove_book(book_number)
       except ValueError:
            print("Invalid input. Book number must be a number.")

    elif choice == '4':
        try:
            book_number = int(input("Enter Book Number to lend: "))
            library.give_book(book_number)
        except ValueError:
            print("Invalid input. Book number must be a number.")

    elif choice == '5':
        try:
            book_number = int(input("Enter Returned Book Number: "))
            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            genre = input("Enter Genre: ")

            book = Book(book_number, name, author, genre)
            library.return_book(book)
        except ValueError:
            print("Invalid input. Book number must be a number.")

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


