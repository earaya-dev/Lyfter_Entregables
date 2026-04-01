total_grades = int(input("Enter the total amount of grades: "))
grade_counter = 1
actual_grade = 0
amount_of_approved_grades = 0
amount_of_failed_grades = 0
average_approved_grades = 0
average_failed_grades = 0
total_average_grades = 0

while(grade_counter <= total_grades):
    print("Enter note number ")
    grade_counter = grade_counter + 1 
    actual_grade = int(input("Enter current grade: "))
    if(actual_grade < 70):
        amount_of_failed_grades = amount_of_failed_grades + 1
        average_failed_grades =  average_failed_grades + actual_grade
    else:
        amount_of_approved_grades = amount_of_approved_grades + 1
        average_approved_grades = average_approved_grades + actual_grade
total_average_grades = total_average_grades + (actual_grade / total_grades)

average_failed_grades = average_failed_grades / amount_of_failed_grades
average_approved_grades = average_approved_grades / amount_of_approved_grades

print(f"The student has the following amount of approved grades: {amount_of_approved_grades}")
print(f"This is the average of approved grades: {average_approved_grades}")
print(f"The student has the following amount of failed grades: {amount_of_failed_grades}")
print(f"This is the average of approved grades: {average_failed_grades}")
print(f"This is the average of total grades: {total_average_grades}")
