import csv

def export_data_to_csv_file(file_path, data):
    if not data:
        print("Error: There is no data available to export for students.")
        return
    
    headers = data[0].keys()
    with open(file_path, 'w', newline= '' ,encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def import_data_from_exported_file(path):
    imported_student_list = []
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:

                row['Spanish grade'] = int(row['Spanish grade'])
                row['English grade'] = int(row['English grade'])
                row['Social studies grade'] = int(row['Social studies grade'])
                row['Science grade'] = int(row['Science grade'])
                
                imported_student_list.append(row)
        
        print(f"Successfully imported {len(imported_student_list)} students.")
        return imported_student_list

    except FileNotFoundError:
        print(f"Error [FileNotFoundError]: File not found or does not exist.")
        return []