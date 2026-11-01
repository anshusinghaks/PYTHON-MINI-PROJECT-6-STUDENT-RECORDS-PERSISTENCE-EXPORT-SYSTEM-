import json
import csv
import os
from datetime import datetime

# File names
JSON_FILE = "students.json"
CSV_FILE = "students.csv"
LOG_FILE = "activity_log.txt"


# Function to write activity in log file
def log_activity(message):
    with open(LOG_FILE, "a") as file:
        time = datetime.now()
        file.write(str(time) + " - " + message + "\n")


# Load student records
def load_students():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is damaged.")
            return None
    else:
        return {}


# Save student records
def save_students(students):
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student(students):

    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    department = input("Enter Department: ")

    marks = {}

    subjects = ["Python", "Maths", "DBMS"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(subject + " Marks: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter numeric marks.")

    students[sid] = {
        "name": name,
        "department": department,
        "marks": marks
    }

    save_students(students)
    log_activity("Student added: " + sid)

    print("Student record saved successfully!")


# Display all students
def display_students(students):

    if not students:
        print("No student records found.")
        return

    for sid, details in students.items():
        print("\nStudent ID:", sid)
        print("Name:", details["name"])
        print("Department:", details["department"])
        print("Marks:", details["marks"])


# Search student
def search_student(students):

    sid = input("Enter Student ID to search: ")

    if sid in students:
        student = students[sid]

        print("\nName:", student["name"])
        print("Department:", student["department"])

        for subject, marks in student["marks"].items():
            print(subject, ":", marks)

    else:
        print("Student not found.")


# Export records to CSV
def export_csv(students):

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Student ID", "Name", "Department",
            "Python", "Maths", "DBMS"
        ])

        for sid, student in students.items():

            writer.writerow([
                sid,
                student["name"],
                student["department"],
                student["marks"]["Python"],
                student["marks"]["Maths"],
                student["marks"]["DBMS"]
            ])

    log_activity("Student records exported to CSV")
    print("CSV export completed successfully!")


# View log using read()
def view_log_read():
    try:
        with open(LOG_FILE, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Log file not found.")


# View log using readline()
def view_log_readline():
    try:
        with open(LOG_FILE, "r") as file:
            print(file.readline())
    except FileNotFoundError:
        print("Log file not found.")


# View log using readlines()
def view_log_readlines():
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line, end="")
    except FileNotFoundError:
        print("Log file not found.")


# JSON string operations
def json_string_demo(students):

    if not students:
        print("No records available.")
        return

    sid = list(students.keys())[0]

    # Convert dictionary into JSON string
    json_text = json.dumps(students[sid], indent=4)

    print("\nJSON String:")
    print(json_text)

    # Convert JSON string back into dictionary
    data = json.loads(json_text)

    print("\nConverted Python Dictionary:")
    print(data)


# Main program
def main():

    students = load_students()

    if students is None:
        print("Fix the JSON file before running the program.")
        return

    while True:

        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Export to CSV")
        print("5. View Log using read()")
        print("6. View Log using readline()")
        print("7. View Log using readlines()")
        print("8. JSON String Demo")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            export_csv(students)

        elif choice == "5":
            view_log_read()

        elif choice == "6":
            view_log_readline()

        elif choice == "7":
            view_log_readlines()

        elif choice == "8":
            json_string_demo(students)

        elif choice == "9":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


main()


def writelines_demo():
    lines = [
        "Student Record System\n",
        "Python File Handling\n",
        "JSON and CSV Operations\n"
    ]

    with open("demo.txt", "w") as file:
        file.writelines(lines)

    print("Data written successfully!")
    