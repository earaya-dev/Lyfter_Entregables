from menu import student_control_menu
from data import export_data_to_csv_file
import os
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'student_information_list.csv')


if __name__ == "__main__":
    list_to_export = student_control_menu()

    if list_to_export:
        export_data_to_csv_file(CSV_PATH, list_to_export)
        print("Before closing the program, latest student data has been exported successfully.")
    else:
        print("No available data to export.")