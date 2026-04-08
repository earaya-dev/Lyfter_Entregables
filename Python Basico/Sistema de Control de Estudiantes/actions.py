import heapq

def check_for_valid_grade (class_name):
    while True:
        try:
            grade = int(input(f"Enter the student's {class_name} grade:"))
            if 0 <= grade <= 100:
                return grade
            print("Invalid grade entered. Please enter a valid grade between 0 and 100.")
        except ValueError as e:
            print(f"Error [ValueError]: Cant convert entered value to a valid number. Details: {e}")


def enter_student_information ():
    current_student_collection = {}
    current_student_collection['Complete Name'] = input("Enter the student's full name:")
    current_student_collection['Section'] = input("Enter the student's section:")

    current_student_collection['Spanish grade'] = check_for_valid_grade("Spanish")
    current_student_collection['English grade'] = check_for_valid_grade("English")
    current_student_collection['Social studies grade'] = check_for_valid_grade("Social studies")
    current_student_collection['Science grade'] = check_for_valid_grade("Science")

    return current_student_collection




def view_all_student_information (main_student_collection):
    if not main_student_collection:
        print("\n[!] The student list is currently empty.")
        print("  Please add students (Option 1) or import a file (Option 6) first.")
        return
    
    for student in main_student_collection:
        print(f"Name: {student['Complete Name']} | "
            f"Section: {student['Section']} | "
            f"SPA grade: {student['Spanish grade']} | "
            f"ENG grade: {student['English grade']} | "
            f"SOC grade: {student['Social studies grade']} | "
            f"SCI grade: {student['Science grade']}")


def check_top3_average_grades (main_student_collection):
    grade_collection = []
    for student in main_student_collection:
        grade_average = (student['Spanish grade'] + student['English grade'] + student['Social studies grade'] 
                        + student['Science grade']) / 4
        grade_collection.append([grade_average, student['Complete Name']])
    
    top3_average_grades = heapq.nlargest(3,grade_collection)
    print("\n TOP 3 STUDENTS ")
    for data in top3_average_grades:
        print(f"Student: {data[1]} | Average: {data[0]}")



def view_overall_average_grades (main_student_collection):
    averages_collection = []
    for student in main_student_collection:
        grade_average = (student['Spanish grade'] + student['English grade'] + student['Social studies grade'] 
                        + student['Science grade']) / 4
        averages_collection.append(grade_average)
    try:
        class_average =sum(averages_collection) / len(averages_collection)
        print(f'The class total average is: {class_average}')

    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Cannot calculate average because no student data exists yet. Details: {e}")