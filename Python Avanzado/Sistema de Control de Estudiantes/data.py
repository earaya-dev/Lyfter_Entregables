import csv
from actions import Student
import os
base_dir = os.path.dirname(os.path.abspath(__file__))



def export_data_to_csv_file(file_path, data):
    if not data:
        print("Error: There is no data available to export for students.")
        return
    
    headers = ['Complete Name', 'Section', 'Spanish grade', 'English grade', 'Social studies grade', 'Science grade']
    with open(file_path, 'w', newline= '' ,encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        rows = []
        for student in data:
            rows.append({
                'Complete Name': student.CompleteName,
                'Section': student.Section,
                'Spanish grade': student.spanish_grade,
                'English grade': student.english_grade,
                'Social studies grade': student.social_studies_grade,
                'Science grade': student.science_grade,
            })
        writer.writerows(rows)


def import_data_from_exported_file(path):
    imported_student_list = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:

                new_student = Student(row['Complete Name'],row['Section'],row['Spanish grade'],row['English grade'],
                        row['Social studies grade'],row['Science grade'])
                
                imported_student_list.append(new_student)
        
        print(f"Successfully imported {len(imported_student_list)} students.")
        return imported_student_list

    except FileNotFoundError:
        print(f"Error [FileNotFoundError]: File not found or does not exist.")
        return []