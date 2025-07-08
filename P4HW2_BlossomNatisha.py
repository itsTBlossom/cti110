#Natisha Blossom
#July 7, 2025
#P4HW2
#Program to calculate pay for multiple employees based off regular hours and overtime worked. An option to stop entering employee information and determine total amounts for employees paid.

#Initial count for employees, overtime pay, regular hour pay, and gross pay.
total_employees = 0
total_overtime = 0
total_reg = 0
total_gross = 0

#Employee name, hours, and pay in a loop.
while True:
    print("Enter employee's name or 'Done' to terminate: ")
    employee_name = input()

    if employee_name == 'Done':
            break
    print(f"How many hours did {employee_name} work? ")
    hours_worked = float(input())

    print(f"What is {employee_name}'s pay rate? ")
    pay_rate = float(input())

#Determine if employee worked overtime. 
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        reg_hours = hours_worked

    else:
        overtime_hours = 0
        reg_hours = hours_worked

#Regular, gross, and overtime pay calculations.
    reg_pay = (hours_worked - overtime_hours) * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = reg_pay + overtime_pay

#Result of pay calculations output.
    print("")
    print("Employee name:", employee_name)
    print("")
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<15.2f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:<15.2f}")

#New totals for employees, overtime pay, regular hour pay, and gross pay.
    total_employees += 1
    total_overtime += overtime_pay
    total_reg += reg_pay
    total_gross += gross_pay

#Results of all totals
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_reg:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
