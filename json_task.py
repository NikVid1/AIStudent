import json

book = {"title":"Notes from the underground","author":"Fyodor Dostoevsky","year":1864
}

with open("book.json", "w") as file:
    json.dump(book, file)

with open("book.json", "r") as file:
    book_info = json.load(file)

print(f"""
    Book Information:
    Title: {book_info["title"]}
    Author: {book_info["author"]}
    Year: {book_info["year"]}
    """)