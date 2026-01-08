import csv
import sqlite3
import os

def import_csv_to_db(csv_filename, db_name="users.db"):
    """
    Reads a CSV file and imports data into a SQLite database.
    """
    if not os.path.exists(csv_filename):
        print(f"Error: File {csv_filename} not found.")
        return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    
    # Clear existing data
    cursor.execute('DELETE FROM users')
    
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                               (row['name'], row['email']))
                count += 1
            
        conn.commit()
        print(f"Successfully imported {count} users into {db_name}")
        
        # Verify
        print("\n--- Users in Database ---")
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
            
    except Exception as e:
        print(f"Error processing CSV: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    import_csv_to_db("users.csv")
