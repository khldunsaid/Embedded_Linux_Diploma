import sqlite3

#Connect to SQlite database 
conn= sqlite3.connect('employees.db')
cursor= conn.cursor()

# query= 'select sqlite_version();'
# cursor.execute(query)

results = cursor.fetchall()
print(f'SQlite version is {results}')

#create a table of employees if it doesn't exist

cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    job TEXT NOT NULL,
                    salary REAL NOT NULL)
               ''')

def add_employee(name,job,salary):
    cursor.execute("INSERT INTO employees(name,job,salary) VALUES(?,?,?)",(name, job,salary))
    conn.commit()
    print("Employee added successfully!")

def print_employee(employee_id):
    cursor.execute("SELECT* FROM employees WHERE id=?",(employee_id,))
    employee = cursor.fetchone()
    if employee:
        print(f"ID: {employee[0]}, NAME: {employee[1]},JOB:,{employee[2]},SALARY:{employee[3]}")
    else:
        print("Employee not found")


def print_employee_table():
    cursor.execute("SELECT* FROM employees")
    # employees = cursor.fetchall()
    
    for row in cursor:
        print(row)

def remove_employee(employee_id):
    cursor.execute("DELETE* FROM employees WHERE id=?",(employee_id,))
    conn.commit()
    if cursor.rowcount:
        print("Employee removed successfully !")
    else:
        print("Employee not found")

def update_employee(employee_id, name=None, job= None, salary= None):
    if name:
        cursor.execute("UPDATE employee SET name=? WHERE id=?",(name, employee_id))
    if job: 
        cursor.execute("UPDATE employee SET job=? WHERE id=?",(job, employee_id))
    if salary:
        cursor.execute("UPDATE employee SET salary=? WHERE id=?",(salary, employee_id))
    conn.commit()
    if cursor.rowcount:
        print("Employee updated successfully!")
    else:
        print("Employee not found.")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add new employee")
        print("2. Print employee data")
        print("3. Print employee table")
        print("4. Remove employee")
        print("5. Update employee")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            job = input("Enter employee job: ")
            salary = float(input("Enter employee salary: "))
            add_employee(name, job, salary)
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            print_employee(employee_id)
        elif choice == '3':
            print_employee_table()
        elif choice == '4':
            employee_id = int(input("Enter employee ID: "))
            remove_employee(employee_id)
        elif choice == '5':
            employee_id = int(input("Enter employee ID: "))
            print("Enter new data (leave blank to keep current value):")
            name = input("Enter new name: ") or None
            job = input("Enter new job: ") or None
            salary = input("Enter new salary: ")
            salary = float(salary) if salary else None
            update_employee(employee_id, name, job, salary)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# if __name__ == "main":
main()

# Close the database connection when the script ends
conn.close()
        

    
    