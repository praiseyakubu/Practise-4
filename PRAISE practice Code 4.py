# -*- coding: utf-8 -*-
"""Code (PA)Q1 By praise Yakubu 20006951

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15iq8YWkLhJS_73Pg1VYQmsSqY-vvhDpM
"""

def validate_number(prompt): #  Validate user input to ensure it's a valid float number.
    while True:
        try:
            no = float(input(prompt))
            return no
        except ValueError:
            print("Error: Please enter a valid number.")

def validate_percentage(prompt):
    while True:
        try:
            percentage = float(input(prompt))
            if 0 <= percentage <= 100:
                return percentage
            else:
                print("Error:")
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_pay(hours_worked, hourly_rate, overtime_rate, standard_tax_rate, overtime_tax_rate):
    standard_hours = 37.5
    overtime_hours = max(0, hours_worked - standard_hours)
    standard_pay = standard_hours * hourly_rate
    overtime_pay = overtime_hours * overtime_rate
    total_earnings = standard_pay + overtime_pay

    # Calculate deductions
    standard_tax = (standard_pay * standard_tax_rate) / 100
    overtime_tax = (overtime_pay * overtime_tax_rate) / 100
    total_deductions = standard_tax + overtime_tax

    # Calculate net pay
    net_pay = total_earnings - total_deductions

    return total_earnings, total_deductions, net_pay

def print_payslip(employee_name, employee_number, week_ending, hours_worked, hourly_rate, overtime_rate, standard_tax_rate, overtime_tax_rate):
    total_earnings, total_deductions, net_pay = calculate_pay(
        hours_worked, hourly_rate, overtime_rate, standard_tax_rate, overtime_tax_rate)

    print("\nPAYSLIP")
    print(f"WEEK ENDING {week_ending}")
    print(f"Employee: {employee_name}")
    print(f"Employee Number: {employee_number}\n")

    print("\t\tEarnings\tDeductions")
    print("\t\tHours  Rate    Total")
    print(f"Hours (normal)  {min(hours_worked, 37.5):.2f}   {hourly_rate:.2f}   {min(hours_worked, 37.5) * hourly_rate:.2f}  Tax @ {standard_tax_rate}%  {total_earnings * standard_tax_rate / 100:.2f}")
    print(f"Hours (overtime) {max(hours_worked - 37.5, 0):.2f}   {overtime_rate:.2f}    {max(hours_worked - 37.5, 0) * overtime_rate:.2f}  Tax @ {overtime_tax_rate}%  {total_earnings * overtime_tax_rate / 100:.2f}\n")

    print(f"Total pay:  {total_earnings:.2f}")
    print(f"Total deductions:  {total_deductions:.2f}")
    print(f"Net pay:  {net_pay:.2f}")

def main():
    employee_name = input("Employee Name: ")  # employee should enter first name and lastname.
    employee_number = input("Employee Number: ")  # employee enters ID number
    week_ending = input("Week ending: ")  # employee inputs last working day
    hours_worked = validate_number("Number of hours worked: ")  # how many hours did an employee work in a week
    hourly_rate = validate_number("Hourly Rate: ")  # how much per hour
    overtime_rate = validate_number("Overtime Rate: ")  # if the employee worked overtime, how much per hour
    standard_tax_rate = validate_percentage("Standard Tax Rate: ")  # input standard tax rate for normal working hours
    overtime_tax_rate = validate_percentage("Overtime Tax Rate: ")  # how many percentage is on an overtime rate

    print_payslip(employee_name, employee_number, week_ending, hours_worked, hourly_rate, overtime_rate,
                  standard_tax_rate, overtime_tax_rate)

if __name__ == "__main__":
    main()