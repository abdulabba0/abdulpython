"""
CRUD
READING

SELECT * FROM TABLE NAME

WHERE
    Condition
    <, >, >=, <=
    LIKE, NOT LIKE, IN, NOT IN, BETWEEN, AND, OR

DELETE
    DELETE FROM TABLE_NAME 
"""
import sqlite3
from random import randint, randrange, choices


conn = sqlite3.connect("bankingDatabase.db")
cursor = conn.cursor()

# cursor.execute("SELECT * FROM customerAccountTable")

# cursor.execute(""" SELECT email, first_name, last_name account_number, created_at FROM customerAccountTable WHERE created_at <= '2025-01-11' """)
# cursor.execute(""" SELECT * FROM customerAccountTable
#     WHERE email LIKE '%gmail%' AND first_name IN ('David', 'Abdul') """)

# cursor.execute(""" SELECT DISTINCT firest_name, last_name FROM customerAccountTable
# """)


# Updating a Table
"""
UPDATE customerAccountTable SET COLUMN_NAME = 'VALUE' WHERE CONDITION
"""
# cursor.execute(f"""
#     UDPATE customerAccountTable SET balance = {randint(1000, 100000)}
# """)
# res = cursor.execute(f"SELECT * FROM customerAccountTable")
# print(res.fetchall()[0])

# for x in range(len(res.fetchall())):
#     cursor.execute("UPDATE customerAccountTable SET balance = {randint(2000, 50000)} WHERE customer_id = {x}")
#     print(res.fetchall())
    # print("===" * 15)
    # print(" ")






# for rows in cursor.fetchall():
#     print(f"Customer Email: {rows[0]}")
#     print(f"Customer Name: {rows[1]} {rows[2]}")
#     print(f"Customer Account: {rows[3]}")
#     # print(f"Date Created: {rows[4]}")
#     print("===" * 15)
#     print(" ")


# print(rows)
conn.commit()
conn.close