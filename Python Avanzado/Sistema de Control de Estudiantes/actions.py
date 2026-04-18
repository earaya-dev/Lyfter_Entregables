import heapq


class Student():
    def __init__(self,name,section,Spanish,English,Socialstudies,Science):
        self.CompleteName = name
        self.Section = section
        self.spanish_grade = Spanish
        self.english_grade = English
        self.social_studies_grade= Socialstudies
        self.science_grade = Science

    def get_average(self):
        grade_average = (self.spanish_grade + self.english_grade + self.social_studies_grade
                        + self.science_grade) / 4
        return grade_average


def create_student():
    return Student(
        check_for_valid_name("Full name"),
        check_for_valid_section("section"),
        check_for_valid_grade("Spanish"),
        check_for_valid_grade("English"),
        check_for_valid_grade("Social studies"),
        check_for_valid_grade("Science"),
        
    )

def check_for_valid_grade (class_name):
    while True:
        try:
            grade = int(input(f"Enter the student's {class_name} grade:"))
            if 0 <= grade <= 100:
                return grade
            print("Invalid grade entered. Please enter a valid grade between 0 and 100.")
        except ValueError:
            print(f"Error: Can't convert entered value to a valid number.")


def check_for_valid_name (Complete_Name):
    while True:
        name = input(f"Enter the student's {Complete_Name}: ")
        if name.replace(" ", "").isalpha() and len(name) > 0:
            return name
        print("Invalid name entered. Please enter a valid name containing only letters and spaces.")


def check_for_valid_section (student_section):
    while True:
        section = input(f"Enter the student's {student_section} (A, B, C, D, E): ").upper()
        if section in ['A', 'B', 'C', 'D', 'E']:
            return section
        print("Invalid section entered. Please enter a valid section (A, B, C, D, E).")


def view_all_student_information (main_student_collection):
    if not main_student_collection:
        print("\n[!] The student list is currently empty.")
        print("  Please add students (Option 1) or import a file (Option 6) first.")
        return
    
    for student in main_student_collection:
        print(f"Name: {student.CompleteName} | "
            f"Section: {student.Section} | "
            f"SPA grade: {student.spanish_grade} | "
            f"ENG grade: {student.english_grade} | "
            f"SOC grade: {student.social_studies_grade} | "
            f"SCI grade: {student.science_grade}")


def check_top3_average_grades (main_student_collection):
    if not main_student_collection:
        print("\n[!] The student list is currently empty.")
        print("  Please add students (Option 1) or import a file (Option 6) first.")
        return

    grade_collection = []
    for student in main_student_collection:
        grade_collection.append([student.get_average(), student.CompleteName])
    
    top3_average_grades = heapq.nlargest(3,grade_collection)
    print("\n TOP 3 STUDENTS ")
    for data in top3_average_grades:
        print(f"Student: {data[1]} | Average: {data[0]}")



def view_overall_average_grades (main_student_collection):
    averages_collection = []
    for student in main_student_collection:
        averages_collection.append(student.get_average())
    try:
        class_average =sum(averages_collection) / len(averages_collection)
        print(f'The class total average is: {class_average}')

    except ZeroDivisionError:
        print(f"Error: Cannot calculate average because no student data exists yet.")