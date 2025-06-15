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


book1 = Book(1, "Smart Work is Success", "Dilshad", "Non Fiction")
book2 = Book(2, "Atomic Habits", "James Clear", "Self-help")


my_library = Library()

my_library.add_book(book1)
my_library.add_book(book2)


my_library.list_books()

my_library.give_book(1)
my_library.list_books()

my_library.return_book(book1)
my_library.list_books()