import os
import sqlite3

API_KEY = "sk-test-123456789abcdef" 

def login(user_input):

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + user_input + "';")
    return cursor.fetchall()

def dangerous_eval():
    code = input("Enter code to run: ")
    eval(code)

print("Logged in as admin")
