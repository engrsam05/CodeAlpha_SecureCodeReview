"""
VULNERABLE CODE - FOR EDUCATIONAL USE ONLY
This code contains security flaws on purpose.
"""

import sqlite3
import hashlib
import os

# Problem 1: Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Problem 2: SQL Injection
def get_user_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Problem 3: Weak password storage (MD5)
def store_password(username, password):
    password_hash = hashlib.md5(password.encode()).hexdigest()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password_hash}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    print(f"User {username} stored with MD5 hash: {password_hash}")

# Problem 4: Command Injection
def ping_host(host):
    os.system(f"ping -c 4 {host}")

# Problem 5: No file path validation
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# Problem 6: No error handling
def divide_numbers(a, b):
    result = a / b
    return result

# Problem 7: Shows too much error info
def show_error_details(error):
    print(f"Error: {error}")

# Problem 8: No input validation
def process_age(age):
    if age < 18:
        print("User is a minor")
    else:
        print("User is an adult")

# Problem 9: Predictable session IDs
def create_session(user_id):
    session_id = user_id + "123"
    return session_id

# Problem 10: Hardcoded API key
API_KEY = "abc123xyz789"

def call_api():
    print(f"Using API key: {API_KEY}")

def main():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()
    
    print("=" * 50)
    print("VULNERABLE CODE - TESTING")
    print("=" * 50)
    
    print("\n1. Testing SQL Injection:")
    get_user_by_username("admin' OR '1'='1")
    
    print("\n2. Testing Command Injection:")
    ping_host("google.com; echo 'HACKED'")
    
    print("\n3. Testing Password Storage:")
    store_password("testuser", "mypassword")
    
    print("\n4. Testing Division:")
    divide_numbers(10, 2)
    
    print("\n5. Testing Age Processing:")
    process_age(-5)

if __name__ == "__main__":
    main()