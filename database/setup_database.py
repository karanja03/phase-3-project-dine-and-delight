import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('ourrecipes.db')
        conn.close()
        print("Database file 'ourrecipes.db' created successfully!")
    except sqlite3.Error as e:
        print("Error creating database file:", e)

if __name__ == '__main__':
    create_database()
