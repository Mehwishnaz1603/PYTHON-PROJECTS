import json
import os

LIBRARY_FILE = "library.txt"

# Load the library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    else:
        return []

# Save the library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

# Show the menu to the user
def show_menu():
    print("Welcome to Personal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("5. Show stats")
    print("6. Exit")

# Function to add a book
def add_book(library):
    title = input("Enter title: ")
    author = input("Enter author: ")
    try:
        year = int(input("Enter year: "))
    except:
        print("Please enter a number for year.")
        return
    genre = input("Enter genre: ")
    read = input("Have you read it? (yes/no): ").lower()
    if read == "yes":
        read = True
    else:
        read = False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print("Book added!")

# Function to remove a book
def remove_book(library):
    title = input("Enter book title to remove: ")
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed!")
            found = True
            break
    if not found:
        print("Book not found.")

# Function to search a book
def search_book(library):
    print("Search by: 1. Title or 2. Author")
    option = input("Enter option: ")
    query = input("Enter your search: ").lower()
    found_books = []

    if option == "1":
        found_books = [b for b in library if query in b["title"].lower()]
    elif option == "2":
        found_books = [b for b in library if query in b["author"].lower()]
    else:
        print("Invalid option")
        return

    if found_books:
        for i, book in enumerate(found_books):
            print(f"{i+1}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No books found.")

# Function to show all books
def show_books(library):
    if not library:
        print("Library is empty.")
    else:
        for i, book in enumerate(library):
            print(f"{i+1}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Show statistics
def show_stats(library):
    total = len(library)
    if total == 0:
        print("No books yet.")
    else:
        read_books = sum(1 for book in library if book["read"])
        percent = (read_books / total) * 100
        print(f"Total books: {total}")
        print(f"Books read: {percent:.1f}%")

# Main program loop
def main():
    library = load_library()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            show_books(library)
        elif choice == "5":
            show_stats(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Bye!")
            break
        else:
            print("Please enter a valid choice.")

main()
