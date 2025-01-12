"""
CRUD
READING

SELECT * FROM TABLE NAME

WHERE
    Condition
    <, >, >=, <=
    LIKE, NOT LIKE, IN, NOT IN, BETWEEN, AND, OR
"""
import sqlite3
from random import randint, randrange, choices


conn = sqlite3.connect("bankingDatabase.db")
cursor = conn.cursor()

# cursor.execute("SELECT * FROM customerAccountTable")

# cursor.execute(""" SELECT email, first_name, last_name account_number, created_at FROM customerAccountTable WHERE created_at <= '2025-01-11' """)
cursor.execute(""" SELECT email, first_name, last_name account_number, created_at FROM customerAccountTable WHERE email LIKE '%gmail%' AND first_name IN ('David', 'Abdul') """)

for rows in cursor.fetchall():
    print(f"Customer Email: {rows[0]}")
    print(f"Customer Name: {rows[1]} {rows[2]}")
    print(f"Customer Account: {rows[3]}")
    # print(f"Date Created: {rows[4]}")
    print("===" * 15)
    print(" ")


# print(rows)
conn.commit()
conn.close