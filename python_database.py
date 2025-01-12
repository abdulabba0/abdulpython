import sqlite3
from random import randint, randrange, choices
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

Data Types
- INTEGER
- REAL
- FLOAT
- VARCHAR
- TEXT
- BOOL
- BOOLEAN
- BLOB
- DATETIME
- DATE
- NULL
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
               phone_number VARCHAR(225) NOT NULL UNIQUE,
               account_number INTEGER NOT NULL UNIQUE,
               balance REAL NOT NULL DEFAULT 0,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )""")

'Inserting Single Data'

'Inserting data Dynamically'
# def generate_phone_numbers(num_to_gen):
#     phone_numbers = []
#     for nums in range(num_to_gen):
#         phone_number = choices(range(10), k=10)
#         phone_number = "+234" + "".join([str(i) for i in phone_number])
#         phone_numbers.append(phone_number)
#     return tuple(phone_numbers)

# def generate_account_numbers(acct_to_gen):
#     acc_numbers = []
#     for nums in range(acct_to_gen):
#         acc_number = choices(range(10), k=10)
#         acc_number = "+234" + "".join([str(i) for i in acc_number])
#         acc_numbers.append(acc_number)
#     return tuple(acc_numbers)

# data = [
#     ('aaron@gmail.com', 'Abdul', 'Khan', '1234567490', 1000.00),
#     ('bukar@gmail.com', 'Bukar', 'Baba', '2345678910', 2000.00),
#     ('charlier@gmail.com', 'Charlie', 'Bob', '2345674310', 2500.00),
#     ('David@gmail.com', 'David', 'John', '2345672610', 2300.00),
#     ('Erik@gmail.com', 'Erik', 'Bale', '2345743610', 2900.00)
#     ]

# account = generate_account_numbers(5)
# phone_number = generate_account_numbers(5)

# for i in range(len(data)):
#     phone = phone_number[i]
#     acct = account[i]
#     *rem, _, _ = data[i]
#     item = tuple(rem) + (phone, acct)
#     del data[i]
#     data.insert(i, item)

# print(type(data))

# try :
#     cursor.executemany("""
#                    INSERT INTO customerAccountTable (email, first_name, last_name, phone_number, account_number)
#                     VALUES (?, ?, ?, ?, ?)
#                    """, data)
#     if cursor.rowcount > 0:
#         print(f"Customer cretaed successfully {cursor.rowcount}")
#     conn.commit()
# except Exception as e:
#     print(f"Error occured: " + str(e))


# conn.close()

'Using a loop to insert data'

# def generate_phone_numbers(num_to_gen):
#     phone_numbers = []
#     for nums in range(num_to_gen):
#         phone_number = choices(range(10), k=10)
#         phone_number = "+234" + "".join([str(i) for i in phone_number])
#         phone_numbers.append(phone_number)
#     return tuple(phone_numbers)

# def generate_account_numbers(acct_to_gen):
#     acc_numbers = []
#     for nums in range(acct_to_gen):
#         acc_number = choices(range(10), k=10)
#         acc_number = "+234" + "".join([str(i) for i in acc_number])
#         acc_numbers.append(acc_number)
#     return tuple(acc_numbers)

# data = [
#     ('frank@gmail.com', 'Frank', 'Smith', '2345678911', 3000.00),
#     ('george@gmail.com', 'George', 'Brown', '2345678912', 3100.00),
#     ('harry@gmail.com', 'Harry', 'White', '2345678913', 3200.00),
#     ('ian@gmail.com', 'Ian', 'Green', '2345678914', 3300.00),
#     ('jack@gmail.com', 'Jack', 'Black', '2345678915', 3400.00)
#     ]

# account = generate_account_numbers(5)
# phone_number = generate_account_numbers(5)

# for i in range(len(data)):
#     phone = phone_number[i]
#     acct = account[i]
#     *rem, _, _ = data[i]
#     item = tuple(rem) + (phone, acct)
#     del data[i]
#     data.insert(i, item)

# print(type(data))

# for row in data :
#     try :
#         cursor.execute("""
#                     INSERT INTO customerAccountTable (email, first_name, last_name, phone_number, account_number)
#                         VALUES (?, ?, ?, ?, ?)
#                     """, row)
#         print("Customer cretaed successfully" + str(cursor.lastrowid))
#         conn.commit()

#     except Exception as e:
#         print(f"Error occured: " + str(e))
    

# email = input('Enter your email address: ').strip()
# first_name = input('Enter your First Name: ').strip()
# last_name = input('Enter your Last Name: ').strip()
# phone_number = input('Enter your Phone Number: ').strip()
# account_number = choices(range(9), k=10)
# acct = "".join([str(i) for i in account_number])
# print(account_number)
# print(len(account_number))
# try :
#     cursor.execute("""
#                    INSERT INTO customerAccountTable (email, first_name, last_name, phone_number, account_number)
#                     VALUES (?, ?, ?, ?, ?)
#                    """, (email, first_name, last_name, phone_number, acct))
#     if cursor.rowcount > 0:
#         print(f"Customer cretaed successfully {cursor.rowcount}")
#     conn.commit()
# except Exception as e:
#     print(f"Error occured: " + str(e))


'Inserting a single row'
# cursor.execute("""
#                INSERT INTO customerAccountTable (email, first_name, last_name, phone_number, account_number, balance)
#                 VALUES ('aaron@gmail.com', 'Abdul', 'Khan', '1234567490', 1234267890, 1000.00)
            #    """)

