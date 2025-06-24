#Natisha Blossom
#June 23, 2025
#P2HW2
#This is a program for inputting grades using floats and integers

#Enter grades for each module and place input in a list
print("Enter grade for Module 1: ")
module_1 = float(input())
print("Enter grade for Module 2: ")
module_2 = float(input())
print("Enter grade for Module 3: ")
module_3 = float(input())
print("Enter grade for Module 4: ")
module_4 = float(input())
print("Enter grade for Module 5: ")
module_5 = float(input())
print("Enter grade for Module 6: ")
module_6 = float(input())
overall_grades = [module_1, module_2, module_3, module_4, module_5, module_6]

#Calculating results for highest, lowest, sum, and average of grades
lowest_grade = min(overall_grades)
highest_grade = max(overall_grades)
grade_sum = sum(overall_grades)
grade_average = sum(overall_grades)/len(overall_grades)

#Results from calculations
print('----------Results----------')
print(f"{'Lowest Grade: ':<20}{lowest_grade:.1f}")
print(f"{'Highest Grade: ':<20}{highest_grade:.1f}")
print(f"{'Sum of Grades: ':<20}{grade_sum:.1f}")
print(f"{'Average: ':<20}{grade_average:.2f}")
print('---------------------------')
