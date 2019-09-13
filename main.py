"""
She-code python course final project
Lior Trieman (september 2019)

* OOP of an Employees management system
"""

import pandas as pd
import time
import os.path

"""
INITIAL EMPLOYEES LIST
"""
columns = ['employee_ID', 'employee_name', 'employee_age', 'employee_phone_no']
""" ADD EMPLOYEE MANUALY 
EMPLOYEE MUST HAVE ALL DATA: ID, NAME, PHONE, AGE"""

# get df of employees from file #
if os.path.isfile("Employee_List.csv"):
    employee_df = pd.read_csv("Employee_List.csv")
else:
    employee_df = pd.DataFrame(columns=columns)


def get_employee_name():
    while True:
        try:
            first_name = input("Please enter new employee's first name:")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if first_name.isdigit():
            print("Sorry, I didn't understand that.")
            continue
        if len(first_name) < 2:
            print('Name if too short, Try again')
        else:
            # first_name was successfully parsed!
            # we're ready to exit the loop.
            break
    while True:  # data validation
        try:
            last_name = input("Please enter the last name of the new employee")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if last_name.isdigit():
            print("Sorry, I didn't understand that.")
            continue
        if len(last_name) < 2:
            print('Name if too short, Try again')
        else:
            # last_name was successfully parsed!
            # we're ready to exit the loop.
            break
    return first_name, last_name


def get_employee_phone():
    while True:  # data validation
        try:
            employee_phone = int(input("Please enter new employee's phone number: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if len(str(employee_phone)) < 8:
            print('Phone Number is too short, missing digits, Please try again')
        else:
            # Phone was successfully parsed!
            # we're ready to exit the loop.
            break
    return employee_phone


def get_employee_ID():
    while True:  # data validation
        try:
            employee_ID = int(input("Please enter new employee's ID number: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if len(str(employee_ID)) < 8:
            print('Phone Number is too short, missing digits, Please try again')
        else:
            # Phone was successfully parsed!
            # we're ready to exit the loop.
            break
    return employee_ID


def get_employee_age():
    while True:  # data validation
        try:
            employee_age = int(input("Please enter new employee's age: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if len(str(employee_age)) > 2:
            print('Seams to old to me.., Please try again')
        if employee_age < 16:
            print('illegal employee age! too young, please try again')
        else:
            # age was successfully parsed!
            # we're ready to exit the loop.
            break
    return employee_age


def add_employee_to_df_employees(employee_df, columns, new_employee):
    employee_df = employee_df.append(pd.Series(new_employee, index=columns), ignore_index=True)
    return employee_df


def delete_employee_record_from_df_employees(employee_df, columns, new_employee):
    employee_df.set_index('employee_ID')
    employee_df = employee_df.append(pd.Series(new_employee, index=columns), ignore_index=True)
    return employee_df


# add new employee to the data-frame of all employees
def create_new_employee_record(employee_ID, new_employee_name, employee_age, employee_phone):
    new_employee_list = [employee_ID, new_employee_name, employee_age, employee_phone]
    return new_employee_list


def employee_full_name(first_name, last_name):
    new_employee_name = first_name + "_" + last_name
    return new_employee_name


def get_employee_details():
    first_name, last_name = get_employee_name()
    new_employee_name = employee_full_name(first_name, last_name)
    employee_age = get_employee_age()
    employee_phone = get_employee_phone()
    employee_ID = get_employee_ID()
    new_employee = create_new_employee_record(employee_ID, new_employee_name, employee_age, employee_phone)
    return new_employee


action = input("Would you like to insert another employee to list?")
if action in ('y', 'Y', 'yes', 'Yes'):
    new_employee_data = get_employee_details()
    employee_df = add_employee_to_df_employees(employee_df, columns, new_employee_data)
    print(employee_df)
    employee_df.to_csv('Employee_List.csv',index=False)
else:
    print("GoodBye!")







