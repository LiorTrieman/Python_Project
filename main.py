"""
She-code python course final project
Lior Trieman (september 2019)

IMPORTANT INSTRUCTIONS:
    * Make sure you wrire each functionality as a seperate function
    * There should be one file with the main code, and at least one more file for functions, classes and utils you need.
    * Main code file will show the navifation (the commands to the user) and will call functinos from other files.
    * There should be proper checks for data validation.
    * Use exceptions and catch them without letting the program fail
"""

import pandas as pd
import os.path
import project_functions as pf  # file with functions
"""
INITIAL EMPLOYEES LIST
"""
columns = ['employee_ID', 'employee_name', 'employee_age', 'employee_phone_no']
columns_log = ['date', 'time', 'employee_ID', 'employee_name']  # Attandance log: This includes date, time, employee_id,
#  name #

# get df of employees from file #
if os.path.isfile("Employee_List.csv"):
    employee_df = pd.read_csv("Employee_List.csv")
else:
    employee_df = pd.DataFrame(columns=columns)
# get df of employees attendance from file #
if os.path.isfile("Employee_Attendance_Log.csv"):
    attendance_df = pd.read_csv("Employee_Attendance_Log.csv")
else:
    attendance_df = pd.DataFrame(columns=columns_log)


# adding employees manually to list

action = input("Would you like to insert another employee to list?")
if action in ('y', 'Y', 'yes', 'Yes'):
    new_employee_data = pf.get_employee_details()
    employee_df = pf.add_employee_to_df_employees(employee_df, columns, new_employee_data)
    print(employee_df)
    employee_df.to_csv('Employee_List.csv', index=False)
else:
    print("GoodBye!")

# delete employees manually from list

action = input("Would you like to delete an employee from list?")
if action in ('y', 'Y', 'yes', 'Yes'):
    # get employ ID
    employee_ID_to_drop = pf.get_employee_ID()
    # search if it is inside df
    item = employee_df.loc[employee_df['employee_ID'] == int(employee_ID_to_drop)]
    if not item.empty:
        # if yes - delete it,
        employee_df = employee_df[employee_df.employee_ID != int(employee_ID_to_drop)]
    else:
        print("Error:  employee not found.!")

    print(employee_df)
    # employee_df = pf.delete_employee_record_from_df_employees(employee_df, columns, employee_ID_to_drop)
    print("dropped employee ID: ", employee_ID_to_drop)
    employee_df.to_csv('Employee_List.csv', index=False)

else:
    print("GoodBye!")

# --------------------------  #
""" Mark Attendance:
--------------------
Employee enters his id, and the attendance is marked.
 The program gets date and time from computer clock (not from user). 
 Stores the attendance in the Attendance log file. 
 Give an error message to the user if the id is not in the Empolyees  file.
"""

action = input("Would you like to recod your attendance??")
if action in ('y', 'Y', 'yes', 'Yes'):
    pf.mark_attendance(employee_df, attendance_df)
else:
    print("GoodBye!")


"""
Generate Attendance report of an employee:
------------------------------------------
Attendance report for a given employee, given the employee ID, return all the entries of his attendance. Give an error 
message to the user if something is wrong.

Print a report for current month for all employees:
------------------------------------------------------
Attendance report for a given employee, given the employee ID, return all the entries of his attendance. Given an error
 message to the user if something is wrong.

Print an attendance report for all employees who were late (came after 9:30am) similar to the previous section

generate Attendance report of an employee:

Attendance report for a given employee, given the employee ID, return all the entries of his attendance. Give an error
 message to the user if something is wrong."""


def generate_report(attendance_df):
    employee_ID = pf.get_employee_ID()
    employee_name = pf.get_employee_name()
    # attendance_df.loc[attendance_df['employee_ID'] == str(employee_ID)]
    # df1 = attendance_df['employee_name'].str.contains(employee_name)
    print(attendance_df[['date','time']])
    return


def generate__late_entrees_report(attendance_df):
    # get all lines for which time>=9:30
    pass




action = input("Would you like to generate and attendance report?")
if action in ('y', 'Y', 'yes', 'Yes'):
    generate_report(attendance_df)
else:
    print("GoodBye!")

"""Print an attendance report for all employees who were late (came after 9:30am) similar to the previous section"""

action = input("Would you like to generate a report for all late entrees??")
if action in ('y', 'Y', 'yes', 'Yes'):
    generate__late_entrees_report(attendance_df)
else:
    print("GoodBye!")
