"""
Hi There,

This code is a simple employee management application built using the Tkinter GUI toolkit and SQLite database.
The application allows the user to add, edit, and delete employee records, as well as view employee details.

The Employee class is used to represent an employee and has attributes for first name, last name, age, gender, and salary.
The EmployeeSystem class is the main application class and contains the GUI components and methods for interacting 
with the database.

The application creates an SQLite database called "employees.db" and a table called "employees" with columns for id,
first name, last name, age, gender, and salary. The GUI components include entry fields for adding
and editing employee records, buttons for adding, editing, and deleting employees,
a listbox for displaying employee names, and labels for displaying employee details.

The add_employee method retrieves employee details from the entry fields, creates an Employee object, inserts the employee
into the database, clears the entry fields, and reloads the employee list.
The load_employees method clears the listbox and loads employee records from the database.
The edit_employee method retrieves the selected employee from the listbox, populates the entry fields with the employee
details, deletes the employee from the database, and reloads the employee list.
The delete_employee method deletes the selected employee from the database and reloads the employee list.
The show_employee_details method retrieves the selected employee from the listbox, creates a new window to display
the employee details, and displays the employee details in labels.

The del method is called when the application is closed and closes the database connection.
The main function creates an instance of the EmployeeSystem class and starts the main event loop.


All The Best

"""

# Libraries
import tkinter as tk
import sqlite3

# Class Employee
class Employee:
    def __init__(self, first_name, last_name, age, gender, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.salary = salary

# Main Class
class EmployeeSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee System")
        self.master.geometry("200x350")
        self.master.resizable(False, False)
        self.master.configure(bg="#F5F5F5")

        # Create employee database
        self.conn = sqlite3.connect("employees.db")
        self.c = self.conn.cursor()  # Add this line
        self.c.execute("""CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            gender TEXT NOT NULL,
                            salary REAL NOT NULL
                            )""")
        self.conn.commit()

        # Create GUI components
        tk.Label(master, text="First Name").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(master)
        self.first_name_entry.grid(row=0, column=1)

        tk.Label(master, text="Last Name").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(master, text="Age").grid(row=2, column=0)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=2, column=1)

        tk.Label(master, text="Gender").grid(row=3, column=0)
        self.gender_entry = tk.Entry(master)
        self.gender_entry.grid(row=3, column=1)

        tk.Label(master, text="Salary").grid(row=4, column=0)
        self.salary_entry = tk.Entry(master)
        self.salary_entry.grid(row=4, column=1)

        self.add_button = tk.Button(master, text="Add", command=self.add_employee)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.edit_button = tk.Button(master, text="Edit", command=self.edit_employee)
        self.edit_button.grid(row=7, column=0, pady=0)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_employee)
        self.delete_button.grid(row=7, column=1, pady=5)

        self.employee_listbox = tk.Listbox(master)
        self.employee_listbox.grid(row=6, column=0, columnspan=2, padx=10)

        self.employee_listbox.bind("<<ListboxSelect>>", self.show_employee_details)

        self.load_employees()
    


    def add_employee(self):
        # Get employee details from entry fields
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = int(self.age_entry.get())
        gender = self.gender_entry.get()
        salary = float(self.salary_entry.get())

        # Create Employee object and insert into database
        employee = Employee(first_name, last_name, age, gender, salary)
        self.c.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?)", 
                       (employee.first_name, employee.last_name, employee.age, employee.gender, employee.salary))
        self.conn.commit()
        
        # Clear entry fields and reload employee list
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        
        self.load_employees()
    


    def load_employees(self):
        # Clear listbox and load employees from database
        self.employee_listbox.delete(0, tk.END)
        for row in self.c.execute("SELECT * FROM employees ORDER BY id"):
            employee = Employee(*row[1:])
            self.employee_listbox.insert(tk.END, f"{employee.first_name} {employee.last_name}")



    def edit_employee(self):
        # Get selected employee from listbox and populate entry fields
        selection = self.employee_listbox.curselection()
        if len(selection) == 1:
            # Get employee ID from selection and retrieve employee from database
            employee_id = selection[0] + 1
            self.c.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
            row = self.c.fetchone()
            employee = Employee(*row[1:])

            # Populate entry fields with employee details
            self.first_name_entry.delete(0, tk.END)
            self.first_name_entry.insert(0, employee.first_name)
            self.last_name_entry.delete(0, tk.END)
            self.last_name_entry.insert(0, employee.last_name)
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, employee.age)
            self.gender_entry.delete(0, tk.END)
            self.gender_entry.insert(0, employee.gender)
            self.salary_entry.delete(0, tk.END)
            self.salary_entry.insert(0, employee.salary)

            # Delete employee from database and reload employee list
            self.c.execute("DELETE FROM employees WHERE id=?", (employee_id,))
            self.conn.commit()
            self.load_employees()



    def delete_employee(self):
        selection = self.employee_listbox.curselection()
        if len(selection) == 1:
            # Get employee ID from selection and delete employee from database
            employee_id = selection[0] + 1
            self.c.execute("DELETE FROM employees WHERE id=?", (employee_id,))
            self.conn.commit()

            # Reload employee list
            self.load_employees()



    def show_employee_details(self, event):
        selection = self.employee_listbox.curselection()
        if len(selection) == 1:
            # Get employee ID from selection and retrieve employee from database
            employee_id = selection[0] + 1
            self.c.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
            row = self.c.fetchone()
            employee = Employee(*row[1:])

            # Create a new window to display employee details
            details_window = tk.Toplevel(self.master)
            details_window.geometry("200x150")
            details_window.resizable(False, False)
            details_window.configure(bg="#F5F5F5")
            details_window.title("Employee Details")

            # Display employee details in labels
            tk.Label(details_window, text=f"First Name: {employee.first_name}").pack()
            tk.Label(details_window, text=f"Last Name: {employee.last_name}").pack()
            tk.Label(details_window, text=f"Age: {employee.age}").pack()
            tk.Label(details_window, text=f"Gender: {employee.gender}").pack()
            tk.Label(details_window, text=f"Salary: {employee.salary}").pack() 

    
    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    login = EmployeeSystem(root)
    root.mainloop()
