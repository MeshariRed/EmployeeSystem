

<h1 align="center"> 
    Employee System
</h1>

<h3 align="center"> 
    This Project is a simple employee management application built using the Tkinter GUI toolkit and SQLite database.
</h3>

<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
    <a href="https://GitHub.com/MeshariRed">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love">
    </a> <br>
    <img src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor" alt="Python Version">
    <img title="Author" src="https://img.shields.io/badge/Author-MeshariRed-blue.svg?color=54aeff&style=for-the-badge&logo=github" /><br>
    <img src="https://img.shields.io/github/license/MeshariRed/EmployeeSystem.svg" alt="LICENSE">
    <img src="https://img.shields.io/github/watchers/MeshariRed/EmployeeSystem.svg" alt="Watching">
    <img src="https://img.shields.io/github/forks/MeshariRed/EmployeeSystem.svg" alt="Forks">
    <img src="https://img.shields.io/github/stars/MeshariRed/EmployeeSystem.svg" alt="Stars">
</p>

## Project introduction
This code is a simple employee management application built using the Tkinter GUI toolkit and SQLite database.
The application allows the user to add, edit, and delete employee records, as well as view employee details.


## Quick revision
The Employee class is used to represent an employee and has attributes for first name, last name, age, gender, and salary.
The EmployeeSystem class is the main application class and contains the GUI components and methods for interacting 
with the database.


## What About Database?
The application creates an SQLite database called "employees.db" and a table called "employees" with columns for id,
first name, last name, age, gender, and salary. The GUI components include entry fields for adding
and editing employee records, buttons for adding, editing, and deleting employees,
a listbox for displaying employee names, and labels for displaying employee details.


## Features 
The add_employee method retrieves employee details from the entry fields, creates an Employee object, inserts the employee
into the database, clears the entry fields, and reloads the employee list.
The load_employees method clears the listbox and loads employee records from the database.
The edit_employee method retrieves the selected employee from the listbox, populates the entry fields with the employee
details, deletes the employee from the database, and reloads the employee list.
The delete_employee method deletes the selected employee from the database and reloads the employee list.
The show_employee_details method retrieves the selected employee from the listbox, creates a new window to display
the employee details, and displays the employee details in labels.

The application also includes a listbox that displays the timer values that have been set and completed,
The completed timer values are displayed in green, and the stopped timer values are displayed in red.

The del method is called when the application is closed and closes the database connection.
The main function creates an instance of the EmployeeSystem class and starts the main event loop.


## Conclusion
Overall, this application provides a simple and user-friendly interface for setting and managing Employees.

All The Best
