import sqlite3
from typing import Optional

# Function to connect to the database
def connect_database():
    connection = sqlite3.connect("CABINETMEDICAL.db")
    cursor = connection.cursor()
    return connection, cursor

# Function to authenticate a user
def authenticate_user(username: str, password: str) -> Optional[dict]:
    connection, cursor = connect_database()
    try:
        query = "SELECT USERNAME, PERMISSIONS FROM USERS WHERE USERNAME = ? AND PASSWORD = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        if user:
            return {"username": user[0], "permissions": user[1].split(",")}
        return None
    except Exception as e:
        print(f"Error authenticating user: {e}")
        raise
    finally:
        connection.close()

# Function to check if a user has access to a table
def has_access(user: dict, table: str) -> bool:
    return table in user["permissions"]

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = authenticate_user(username, password)
    if user:
        print(f"Welcome, {user['username']}!")
        table = input("Enter the table you want to access: ")
        if has_access(user, table):
            print(f"Access granted to table: {table}")
        else:
            print(f"Access denied to table: {table}")
    else:
        print("Invalid username or password.")