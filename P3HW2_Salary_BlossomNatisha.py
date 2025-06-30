#Natisha Blossom
#June 30, 2025
#P3HW2
#Program to calculate pay for employees based off hours and overtime worked.

#Initial input for employee information, hours worked, and pay rate.
print("Enter employee's name:")
employee_name = input()
print("Enter number of hours worked:")
hours_worked = float(input())
print("Enter employee's pay rate:")
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
print('-------------------------------------')
print(f"Employee name: {employee_name:}")

print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${reg_pay:<15.2f}${gross_pay:<15.2f}")
