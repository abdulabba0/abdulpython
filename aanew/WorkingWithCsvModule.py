import csv

employees = [
    {"FirstName": "John", "LastName": "Smith", "Age": 35, "Email": "john.smith@company.com", "Department": "HR"},
    {"FirstName": "Mary", "LastName": "Johnson", "Age": 29, "Email": "mary.johnson@company.com", "Department": "Finance"},
    {"FirstName": "Alex", "LastName": "Brown", "Age": 41, "Email": "alex.brown@company.com", "Department": "IT"},
    {"FirstName": "Sophia", "LastName": "Taylor", "Age": 33, "Email": "sophia.taylor@company.com", "Department": "Marketing"},
    {"FirstName": "James", "LastName": "Anderson", "Age": 38, "Email": "james.anderson@company.com", "Department": "Operations"},
    {"FirstName": "Linda", "LastName": "Thomas", "Age": 27, "Email": "linda.thomas@company.com", "Department": "Sales"},
    {"FirstName": "David", "LastName": "Jackson", "Age": 42, "Email": "david.jackson@company.com", "Department": "IT"},
    {"FirstName": "Emma", "LastName": "White", "Age": 30, "Email": "emma.white@company.com", "Department": "HR"},
    {"FirstName": "Michael", "LastName": "Harris", "Age": 36, "Email": "michael.harris@company.com", "Department": "Finance"},
    {"FirstName": "Olivia", "LastName": "Martin", "Age": 28, "Email": "olivia.martin@company.com", "Department": "Sales"},
    {"FirstName": "Daniel", "LastName": "Thompson", "Age": 39, "Email": "daniel.thompson@company.com", "Department": "Operations"},
    {"FirstName": "Isabella", "LastName": "Garcia", "Age": 31, "Email": "isabella.garcia@company.com", "Department": "Marketing"},
    {"FirstName": "Ethan", "LastName": "Martinez", "Age": 34, "Email": "ethan.martinez@company.com", "Department": "Finance"},
    {"FirstName": "Mia", "LastName": "Robinson", "Age": 26, "Email": "mia.robinson@company.com", "Department": "HR"},
    {"FirstName": "Matthew", "LastName": "Clark", "Age": 40, "Email": "matthew.clark@company.com", "Department": "IT"},
    {"FirstName": "Charlotte", "LastName": "Rodriguez", "Age": 32, "Email": "charlotte.rodriguez@company.com", "Department": "Sales"},
    {"FirstName": "Joseph", "LastName": "Lewis", "Age": 37, "Email": "joseph.lewis@company.com", "Department": "Operations"},
    {"FirstName": "Amelia", "LastName": "Lee", "Age": 29, "Email": "amelia.lee@company.com", "Department": "Marketing"},
    {"FirstName": "William", "LastName": "Walker", "Age": 43, "Email": "william.walker@company.com", "Department": "Finance"},
    {"FirstName": "Emily", "LastName": "Hall", "Age": 30, "Email": "emily.hall@company.com", "Department": "HR"},
]

students = [
    ["John", "Smith", 20, "john.smith@example.com", "Math"],
    ["Mary", "Johnson", 19, "mary.johnson@example.com", "Physics"],
    ["Alex", "Brown", 21, "alex.brown@example.com", "Chemistry"],
    ["Sophia", "Taylor", 22, "sophia.taylor@example.com", "Biology"],
    ["James", "Anderson", 23, "james.anderson@example.com", "History"],
    ["Linda", "Thomas", 20, "linda.thomas@example.com", "English"],
    ["David", "Jackson", 24, "david.jackson@example.com", "Computer Science"],
    ["Emma", "White", 18, "emma.white@example.com", "Economics"],
    ["Michael", "Harris", 21, "michael.harris@example.com", "Math"],
    ["Olivia", "Martin", 19, "olivia.martin@example.com", "Physics"],
    ["Daniel", "Thompson", 20, "daniel.thompson@example.com", "Chemistry"],
    ["Isabella", "Garcia", 22, "isabella.garcia@example.com", "Biology"],
    ["Ethan", "Martinez", 23, "ethan.martinez@example.com", "History"],
    ["Mia", "Robinson", 18, "mia.robinson@example.com", "English"],
    ["Matthew", "Clark", 25, "matthew.clark@example.com", "Computer Science"],
    ["Charlotte", "Rodriguez", 20, "charlotte.rodriguez@example.com", "Economics"],
    ["Joseph", "Lewis", 21, "joseph.lewis@example.com", "Math"],
    ["Amelia", "Lee", 19, "amelia.lee@example.com", "Physics"],
    ["William", "Walker", 22, "william.walker@example.com", "Chemistry"],
    ["Emily", "Hall", 20, "emily.hall@example.com", "Biology"],
]

# # Creating and writing to a CSV file
# with open("studentDetails.csv", "w") as file :
#     writer = csv.writer(file)
#     writer.writerows(students)
#     writer.writerow(["FirstName", "LastName", "Age", "Email", "Subject"])
#     writer.writerows(students)

# # Writting to a CSV file along 
# with open("employee.csv",  "w", newline="") as file:
#     writer = csv.DictWriter(file, employees[0].keys())
#     writer.writeheader()
#     writer.writerows(employees)

# # Reading a CSV file
# with open("studentDetails.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open("studentDetails.csv", "r") as file :
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# with open("studentDetails.xlsx", "r") as file :
#     reader = csv.DictReader(file)
#     for rows in reader:
#         print(rows)

# 10 Practical Data Processing Questions

"""
1. Filtering Rows
Load the CSV and print all students/employers whose age is greater than 30.

2. Sorting
Sort the CSV data by Age in ascending order and save the result into a new CSV file.

3. Unique Values
Find all the unique classes (for students) or unique departments (for employers).

4. Counting Frequency
Count how many students are enrolled in each class OR how many employers work in each department.

5. Average Calculation
Calculate the average age of students OR employers.

6. Normalization (Min-Max Scaling)
Normalize the Age column to a range of [0, 1] using the min-max normalization formula:
X_norm = (X - X_min) / (X_max - X_min)

7. Standardization (Z-score Normalization)
Normalize the Age column using Z-score standardization:
Z = (X - μ) / σ
where μ = mean, σ = standard deviation.

8. Top-N Selection
Print the top 5 oldest students/employers.

9. Group By & Aggregation
Group students by Class or employers by Department and compute the average age per group.

10. Data Cleaning
Suppose some rows have missing Email values.
Write a function that replaces missing emails with "unknown@example.com"
and saves the cleaned data back into CSV."""

#Load the CSV and print all students/employers whose age is greater than 30.
with open("employee.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Age"]) > 30:
            print(row)

# Sort the CSV data by Age in ascending order and save the result into a new CSV file.

# def sort_csv(file, new_file_name) :
#     updated_file = []
#     with open(file, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:

# def sort_csv(file) :
#     left = []
#     right = []
#     all_ages = []

#     readers = []
#     with open(file, 'r+') as file:
#         reader = csv.DictReader(file)
#         for rows in reader:
#             readers.append(rows)

#     all_ages = [x['Age'] for x in readers]
#     sorted_age = [x['Age'] for x in readers]
#     all_ages.sort()
#     mid = sorted_age[int(len(sorted_age) / 2)]
#     print(mid)
#     for age in enumerate(all_ages):
#         if age > mid:
#             right.append((index, age))

# file = "employee.csv"
# sort_csv(file)

input_file = 'employee.csv'
output_file = 'sorted_output.csv'

with open(input_file, 'r', newline='') as file:
    reader = csv.DictReader(file)
    sorted_rows = sorted(reader, key=lambda row: int(row['Age']))

with open(output_file, mode='w', newline='') as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sorted_rows)

print({output_file})

