from actions import (
    enter_student_information,
    view_all_student_information,
    check_top3_average_grades,
    view_overall_average_grades,
)


from data import export_data_to_csv_file, import_data_from_exported_file


def student_control_menu ():
    current_action = 0
    main_student_collection = []
    while True:
        print(f"--- CURRENT ACTION SELECTED: {current_action} ---")
        print("1. Enter individual student information")
        print("2. Show all current students information")
        print("3. Check Top 3 students with the best average grade")
        print("4. View the overall average grade across all students")
        print("5. Export all current data to a CSV File")
        print("6. Import all data from a CSV file previously exported")
        print("7. Exit")

        user_input = input("Please choose an action from the menu above: ")
        if user_input == "1":           
            current_action = 1
            try:
                number_of_students = int(input("How many students will you like to add into the system?"))
                for student_count in range(number_of_students):
                    main_student_collection.append(enter_student_information())
            except ValueError as e:
                print(f"Error [ValueError]: Please enter a whole number or the amount of students required. Details: {e}")
        elif user_input == "2":
            current_action = 2
            view_all_student_information(main_student_collection)
        elif user_input == "3":
            current_action = 3
            check_top3_average_grades(main_student_collection)
        elif user_input == "4":
            current_action = 4
            view_overall_average_grades(main_student_collection)
        elif user_input == "5":
            current_action = 5
            export_data_to_csv_file('student_information_list.csv', main_student_collection)

            print("\n Student data has been exported to 'student_information_list.csv'successfully.")
        elif user_input == "6":
            current_action = 6
            main_student_collection = import_data_from_exported_file('student_information_list.csv')
        elif user_input == "7":
            print(f'Goodbye!')
            break
        else:
            print("ERROR: Please enter a valid action number from the menu.")
    return main_student_collection

