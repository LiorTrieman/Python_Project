import pandas as pd
import datetime
import os


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


def employee_full_name(first_name, last_name):
    new_employee_name = first_name + "_" + last_name
    return new_employee_name


def get_employee_info_from_id(attendent_employee_id, employee_df):
    print(attendent_employee_id)
    print(type(attendent_employee_id))


# add new employee to the data-frame of all employees
def create_new_attendance_record(att_date, att_time, employee_ID, new_employee_name):
    new_attendance = [att_date, att_time, employee_ID, new_employee_name]
    return new_attendance


def mark_attendance(employee_df, attendance_df):
    attendent_employee_id = input("please enter your ID:")
    employee_id_list = employee_df.employee_ID.tolist()
    print("employee_id_list", employee_id_list)
    print("attendent_employee_id", attendent_employee_id)
    if int(attendent_employee_id) in employee_id_list:
        attendent_employee_id = input("ID not found, please try again:")
        if attendent_employee_id in employee_id_list:
            print("ID not found, goodbye!")
            quit()
    # get employee name matches his ID
    # new_employee_name = get_employee_info_from_id(attendent_employee_id, employee_df)  #check this function
    # mark attendance in the attendance log df:
    print("we have it, your attendance has being submitted")
    attendent_time = datetime.datetime.now().time()
    attendent_date = datetime.datetime.now().date()
    new_employee_name = 'NK'
    print(attendent_date, attendent_time)
    new_attendance = [attendent_date, attendent_time, attendent_employee_id, new_employee_name]
    columns_log = attendance_df.columns
    attendance_df = attendance_df.append(pd.Series(new_attendance, index=columns_log), ignore_index=True)
    attendance_df.to_csv('Employee_Attendance_Log.csv', index=False)


def add_employee_to_df_employees(employee_df, columns, new_employee):
    employee_df = employee_df.append(pd.Series(new_employee, index=columns), ignore_index=True)
    return employee_df


def add_attendent_to_df_attendance(attendance_df, columns_log, attendent_employee_id):
    employee_info = get_employee_info_from_id(attendent_employee_id)
    attendance_df = attendance_df.append(pd.Series(employee_info, index=columns_log), ignore_index=True)
    return attendance_df


def delete_employee_record_from_df_employees(employee_df, columns, new_employee):
    employee_df.set_index('employee_ID')
    employee_df = employee_df.drop(pd.Series(new_employee, index=columns), ignore_index=True)
    return employee_df


# add new employee to the data-frame of all employees
def create_new_employee_record(employee_ID, new_employee_name, employee_age, employee_phone):
    new_employee_list = [employee_ID, new_employee_name, employee_age, employee_phone]
    return new_employee_list


def get_employee_details():
    first_name, last_name = get_employee_name()
    new_employee_name = employee_full_name(first_name, last_name)
    employee_age = get_employee_age()
    employee_phone = get_employee_phone()
    employee_ID = get_employee_ID()
    new_employee = create_new_employee_record(employee_ID, new_employee_name, employee_age, employee_phone)
    return new_employee


"""
def add_from_file():

    while True:  # getting dir from user
        file_path = input("Enter File Name and path")
        if os.path.exists(os.path.dirname(file_path)):
            file = 1
        else:
            print("dir is not valid try again")
            file = 0
        if file == 1:
            print("We found your file!")
            break
    # getting file name from path:
    base = os.path.basename(file_path)
    file_name = os.path.splitext(base)[0]
    print(file_name)
    # check for valid employee in file:
    num_lines = sum(0 for line in open('New Employee.txt'))
    print(num_lines)
    if num_lines:
        # we would like to add all employees in this file the the Employees file
        f = open("Employee", 'a')
        ff = open(base, 'r')
        new_employee = ff.read()
        # need to check if all data of employee is valid
        # converting new employee data from a string to list
        new_employee_data = new_employee.split()
        print(new_employee_data)
        print(new_employee)
        # check validation of data
        valid_employee = 1
        if new_employee_data[0].isdigit():
            print("Sorry, first name is not valid")
            valid_employee = 0
        if len(new_employee_data[0]) < 2:
            print('Sorry, first name is not valid')
            valid_employee = 0
        if new_employee_data[1].isdigit():
            print("Sorry, Last name is not valid")
            valid_employee = 0
        if len(new_employee_data[1]) < 2:
            print('Sorry, Last name is not valid')
            valid_employee = 0
        if new_employee_data[2].isdigit() is not True:
            print("Sorry, ID is not valid")
            valid_employee = 0
        if len(new_employee_data[2]) < 8:
            print('Sorry, ID is not valid')
            valid_employee = 0
        if valid_employee:
            f.write(new_employee + '\n')
    else:
        print("no new employees in this file")"""
