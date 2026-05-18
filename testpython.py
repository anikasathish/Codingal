class Book:
    # 1. __init__ constructor setting title, author, and availability status
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Defaults to False as required

    # 2. borrow() method to check out a book
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Confirmation: You have successfully borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    # 3. return_book() method to bring a book back
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Confirmation: '{self.title}' has been successfully returned.")
        else:
            print(f"'{self.title}' is already available in the library.")


# 4. Creating at least 3 Book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Demonstrating the methods on the objects
print("--- Library System Demonstration ---\n")

# Testing Book 1: Borrowing and trying to borrow again
print(f"Testing {book1.title}:")
book1.borrow()      # Successful borrow
book1.borrow()      # Already borrowed check
print("-" * 40)

# Testing Book 2: Borrowing and Returning
print(f"Testing {book2.title}:")
book2.borrow()      # Successful borrow
book2.return_book() # Successful return
print("-" * 40)

# Testing Book 3: Returning a book that wasn't borrowed yet
print(f"Testing {book3.title}:")
book3.return_book() # Already available check
book3.borrow()      # Successful borrow
print("-" * 40)