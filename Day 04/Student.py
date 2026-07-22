

import json



FILE_NAME = "Students.JSON"


def loadData():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def saveData(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def update_student_details(student):
    print(f"\nUpdating {student['name']}")

    new_class = input("Enter new class (leave blank to keep current): ")
    if new_class:
        student["class_name"] = new_class

    print("\nCurrent Subjects and Marks:")
    for sub, mark in student["marks_info"].items():
        print(f"{sub}: {mark}")

    choice = input("\nDo you want to update marks? (yes/no): ").lower()

    if choice == "yes":
        new_marks = {}

        while True:
            subject = input("Enter subject (or 'done'): ")

            if subject.lower() == "done":
                break

            try:
                marks = int(input(f"Enter marks for {subject}: "))
                new_marks[subject] = marks
            except ValueError:
                print("Marks must be a number.")

        if new_marks:
            student["marks_info"] = new_marks

    return student


while True:

    print("\n========== Student Record Management ==========")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # ---------------- Add ----------------

    if choice == 1:

        name = input("Enter Student Name: ")

        class_name = input("Enter Class: ")

        marks_info = {}

        while True:

            subject = input("Enter subject (or 'done'): ")

            if subject.lower() == "done":
                break

            try:
                marks = int(input(f"Enter marks for {subject}: "))
                marks_info[subject] = marks
            except ValueError:
                print("Marks must be numeric.")

        student = {
            "name": name,
            "class_name": class_name,
            "marks_info": marks_info
        }

        data = loadData()

        data[name] = student

        saveData(data)

        print("Student added successfully.")

    # ---------------- Update ----------------

    elif choice == 2:

        name = input("Enter student name: ")

        data = loadData()

        if name in data:

            data[name] = update_student_details(data[name])

            saveData(data)

            print("Student updated successfully.")

        else:
            print("Student not found.")

    # ---------------- Search ----------------

    elif choice == 3:

        name = input("Enter student name: ")

        data = loadData()

        if name in data:

            student = data[name]

            print("\nName:", student["name"])
            print("Class:", student["class_name"])
            print("Subjects and Marks:")

            for sub, mark in student["marks_info"].items():
                print(f"  {sub}: {mark}")

        else:
            print("Student not found.")

    # ---------------- Delete ----------------

    elif choice == 4:

        name = input("Enter student name: ")

        data = loadData()

        if name in data:

            del data[name]

            saveData(data)

            print("Student deleted successfully.")

        else:
            print("Student not found.")

    # ---------------- Display ----------------

    elif choice == 5:

        data = loadData()

        if not data:
            print("No student records found.")

        else:

            print("\n===== Student Records =====")

            for student in data.values():

                print("-------------------------")
                print("Name :", student["name"])
                print("Class:", student["class_name"])
                print("Subjects and Marks:")

                for sub, mark in student["marks_info"].items():
                    print(f"  {sub}: {mark}")

    # ---------------- Exit ----------------

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")