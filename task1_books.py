import requests
import sqlite3
import json

def fetch_books():
    """
    Fetches a list of books from the OpenLibrary API.
    Returns a list of dictionaries with title, author, and year.
    """
    url = "https://openlibrary.org/subjects/python.json?limit=10"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        books = []
        for work in data.get('works', []):
            title = work.get('title', 'Unknown Title')
            # Authors is a list of dicts: [{'name': '...', 'key': '...'}]
            authors_list = work.get('authors', [])
            author_names = ", ".join([a.get('name', 'Unknown') for a in authors_list])
            year = work.get('first_publish_year', None)
            
            books.append({
                'title': title,
                'author': author_names,
                'year': year
            })
        return books
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def save_to_db(books, db_name="books.db"):
    """
    Saves the list of books to a SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    ''')
    
    # Clear existing data to avoid duplicates on re-runs
    cursor.execute('DELETE FROM books')
    
    # Insert data
    for book in books:
        cursor.execute('''
            INSERT INTO books (title, author, publication_year)
            VALUES (?, ?, ?)
        ''', (book['title'], book['author'], book['year']))
    
    conn.commit()
    print(f"Successfully saved {len(books)} books to {db_name}")
    conn.close()

def display_books(db_name="books.db"):
    """
    Reads data from the database and prints it to the console.
    """
    print("\n--- Retrieved Books from Database ---")
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('SELECT title, author, publication_year FROM books')
    rows = cursor.fetchall()
    
    if not rows:
        print("No books found in database.")
    
    for row in rows:
        print(f"Title: {row[0]}")
        print(f"Author: {row[1]}")
        print(f"Year: {row[2]}")
        print("-" * 30)
        
    conn.close()

if __name__ == "__main__":
    print("Fetching books data...")
    books_data = fetch_books()
    if books_data:
        save_to_db(books_data)
        display_books()
    else:
        print("No data found.")
