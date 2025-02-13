import json

# Book information
book = 
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "isbn": "9780743273565"}


# Save book information to a JSON file
with open("book.json", "w") as file:
    json.dump(book, file)

# Load book information from the JSON file
with open("book.json", "r") as file:
    book_info = json.load(file)

print(f"""
    Book Information:
    Title: {book_info["title"]}
    Author: {book_info["author"]}
    Year: {book_info["year"]}
    ISBN: {book_info["ISBN"]}
    """)