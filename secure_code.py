"""
SECURE CODE - Fixed Version

This application demonstrates secure coding practices by fixing
common security vulnerabilities.
"""

import sqlite3
import os
import re
import secrets
import bcrypt
import subprocess
import platform

# ==========================================================
# Fix 1: Use Environment Variables for Credentials
# ==========================================================

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
API_KEY = os.environ.get("API_KEY")


# ==========================================================
# Database Setup
# ==========================================================

def initialize_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password BLOB
        )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# Fix 2: Prevent SQL Injection
# ==========================================================

def get_user_by_username(username):

    if not username or len(username) > 50:
        raise ValueError("Invalid username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    result = cursor.fetchall()

    conn.close()

    return result


# ==========================================================
# Fix 3: Secure Password Storage
# ==========================================================

def store_password(username, password):

    if not username or not password:
        raise ValueError("Username and password are required.")

    password_hash = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password_hash)
    )

    conn.commit()
    conn.close()

    print("Password stored securely.")


# ==========================================================
# Fix 4: Prevent Command Injection
# ==========================================================

def ping_host(host):

    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host.")

    count = "-n" if platform.system() == "Windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", count, "4", host],
            capture_output=True,
            text=True,
            timeout=10,
            check=True
        )

        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("Ping timed out.")

    except subprocess.CalledProcessError:
        print("Ping failed.")


# ==========================================================
# Fix 5: Secure File Handling
# ==========================================================

def read_file(filename):

    if not re.match(r'^[a-zA-Z0-9_.-]+$', filename):
        raise ValueError("Invalid filename.")

    allowed_directory = os.path.join(os.getcwd(), "allowed_files")

    safe_path = os.path.join(allowed_directory, filename)

    if not os.path.abspath(safe_path).startswith(os.path.abspath(allowed_directory)):
        raise ValueError("Access denied.")

    try:
        with open(safe_path, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found.")
        return None


# ==========================================================
# Fix 6: Proper Error Handling
# ==========================================================

def divide_numbers(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

    except Exception:
        print("Unexpected error.")
        return None


# ==========================================================
# Fix 7: Hide Internal Errors
# ==========================================================

def show_error_details(error):

    print("An unexpected error occurred.")


# ==========================================================
# Fix 8: Validate Input
# ==========================================================

def process_age(age):

    try:

        age = int(age)

        if age < 0 or age > 150:
            print("Invalid age.")
            return

        if age < 18:
            print("User is a minor.")
        else:
            print("User is an adult.")

    except ValueError:
        print("Please enter a valid number.")


# ==========================================================
# Fix 9: Secure Session IDs
# ==========================================================

def create_session(user_id):

    return secrets.token_urlsafe(32)


# ==========================================================
# Fix 10: Secure API Key Usage
# ==========================================================

def call_api():

    if not API_KEY:
        raise ValueError("API_KEY is not configured.")

    print("Calling API securely...")


# ==========================================================
# Main Function
# ==========================================================

def main():

    initialize_database()

    print("=" * 50)
    print("SECURE CODE - TESTING")
    print("=" * 50)

    print("\n1. Testing SQL Injection Protection")

    try:
        get_user_by_username("admin' OR '1'='1")
        print("Query executed safely.")
    except ValueError:
        print("SQL Injection blocked.")

    print("\n2. Testing Command Injection Protection")

    try:
        ping_host("google.com")
    except ValueError:
        print("Invalid host.")

    print("\n3. Testing Password Storage")

    store_password("testuser", "StrongPassword123!")

    print("\n4. Testing Division")

    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))

    print("\n5. Testing Input Validation")

    process_age(20)
    process_age(-5)
    process_age("abc")

    print("\n6. Creating Session")

    print(create_session("testuser"))

    print("\n7. API Test")

    try:
        call_api()
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()