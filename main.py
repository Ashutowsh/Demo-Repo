# vulnerable_test.py

import os
import sqlite3

API_KEY = "sk-test-123456789abcdef"  # 🔥 Hardcoded secret

def login(user_input):
    # 🔥 SQL Injection risk
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "';")
    return cursor.fetchall()

def dangerous_eval():
    # 🔥 Insecure function
    code = input("Enter code to run: ")
    eval(code)

print("Logged in as admin")
