#--------Assigenment 11---------#
#Classe Methods:
#Create a Class Book with a Class Varaiable total_books. Add a class method increamenent_book_count to increase the count
# when a new book is added.
class Book:
    total_books = 0               # Class variable to track total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

if __name__ == "__main__":
   book1 = Book("1984", "George Orwell")
   book2 = Book("To Kill a Mockingbird", "Harper Lee")

print("Total books:", Book.get_total_books())
