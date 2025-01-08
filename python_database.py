import sqlite3
"""
SQL stands for Structured Query Language
A language we use to query data from database
NO SQL does not support SQL

Type of SQL Database
1. MySQL
2. PostgreSQL
3. SQLite3
4. Oracle

Type of No SQL Database
1. MongoDB
2. Cassandra
3. mariadb

1. SQL 
-Tabular form: Column rows
- Fixed schema where that data structure is define before use.

2. No SQL:
- Uses document form or graph form
- Flexible schema

CRUD
- Create : INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
- Read : SELECT FROM  table_name (column1, column2, ...) FROM table_name WHERE condition;
- update : UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
- Delete : DELETE FROM table_name WHERE condition;
"""

conn = sqlite3.connect("bankingDatabase.db")
cursor = conn.cursor()

# Create a Table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS customerAccountTable (
               customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
               email VARCHAR(225) NOT NULL UNIQUE,
               first_name VARCHAR(225) NOT NULL,
               last_name VARCHAR(225) NOT NULL,
               phone_number VARCHAR(225) NOT NULL,
               account_number INTEGER NOT NULL UNIQUE,
               balance REAL NOT NULL DEFAULT 0,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )""")

cursor.execute("""
               INSERT INTO customerAccountTable (email, first_name, last_name, phone_number, account_number, balance)
                VALUES ('abdul@gmail.com', 'Abdul', 'Khan', '1234567890', 1234567890, 1000.00)
               """)
conn.commit()