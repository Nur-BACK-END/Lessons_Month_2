import sqlite3

def setup_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        users = [("Олег", 35), ("Егор", 33), ("Игорь", 32)]
        cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)

    conn.commit()
    conn.close()

def get_user_by_number(number):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM users WHERE id = ?", (number,))
    result = cursor.fetchone()

    conn.close()
    if result:
        return result[0]
    else:
        return "Пользователь с таким номером не существует."

if __name__ == "__main__":
    setup_database()

    user_number = 2
    result = get_user_by_number(user_number)
    print(result)
