import sqlite3
connection = sqlite3.connect('passwordManager.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE Users (
Username TEXT,
Password TEXT
);""")

cursor.execute("""CREATE TABLE LogInHistory (
Username TEXT
);""")

cursor.execute("""CREATE TABLE Credentials(
Service TEXT,
UsernameOnService TEXT,
Password TEXT,
Username TEXT
);""")
