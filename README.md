# Python_Project
Final Python course project from she-codes
# Employee Attendance Management System
This program will maintain employee attandance for a company or factory

# Files
The program will maintain these files:
Employees: This includes employee_id, name, phone, age
Attandance log: This includes date, time, employee_id, name
**You can choose to maintain more files if you need to.

# Functionality
Progam has following functionality:

**Add employee manually**

The user can choose to add a new employee to the Employees file if all the data is supplied
Given an error message to the use if something is wrong.
  
**Add employee from file**

The user can enter a file path which contains data of employees to add to the Employees file
if all the data of all the employees is supplied.
The file can be empty or contain one or more new employees.
You can choose the structure of the file (Bonus: read csv files and make it support tables made with Excel).
Give an error message to the user if something is wrong.
  
**Delete employees manualy**
  
The user can choose the delete an employee from the employee file.
Give an error message to the user if something is wrong.
  
**Delete employees from file**

 The user can engter a file path which contains data of employees to delete from the Employees file if all the data of all the employees is supplier (ID's).
 the file can be empty or contain one or more employees to delet.
 You can choose the structure of the file (Bonus: read csv files and make it support tables made with Excel).
Give an error message to the user if something is wrong.
    
**Mark Attendance:**

Employee enters his id, and the attendance is marked. The program gets date and time from computer clock (not from user). Stores the attendance in the Attendance log file.
Give an erroe message to the user if the id is not in the Empolyees file.
      
**Generate Attendance report of an employee:**

Attendance report for a given employee, given the employee ID, return all the entries of his attendance.
Give an error message to the user if something is wrong.
      
**Print a report for current month for all employees:**
      
Attendance report for a given employee, given the employee ID, return all the entries of his attendance.
Given an error message to the user if something is wrong.
        
**Print an attendance report for all employees who were late (came after 9:30am)**
similar to the previous section
        
        
 ## Intructions:
        * Make sure you wrire each functionality as a seperate function
        * There should be one file with the main code, and at least one more file for functions, classes and utils you need.
        * Main code file will show the navifation (the commands to the user) and will call functinos from other files.
        * There should be proper checks for data validation.
        * Use exceptions and catch them without letting the program fail.
        
      
