
# implementation of a student class
from operator import add


class Student:
    def __init__(self,name,Subjects,marks,Class):
        self.name =name
        self.subjects= Subjects
        self.marks= marks
        self.student_class= Class
    def sum_numbers(self):              # sum of marks
        total =0
        for marks in self.marks:
            total +=marks
        return total
    def average(self):                  # Function to calculate average marks
        if len(self.marks) == 0:
            return 0    
        total = self.sum_numbers()
        average = total/len(self.marks)
        return average
    def grade(self):                    # Function to calculate grade based on average marks
        avg = self.average()
        if (avg >= 90 ):
            return "A"
        elif (avg >= 80 ):
            return "B"
        elif (avg >= 70 ):
            return "C"
        elif (avg >= 60 ):
            return "D"
        elif (avg >= 50 ):
            return "E"
        else:
            return "F"
    def display(self):                  # Function to display student details
        print("Name:    ", self.name)
        print("Subjects   and   Marks:")
        for i in range(len(self.subjects)):
            print(self.subjects[i]+ "          "  + str(self.marks[i]))
        print("Class:   ", self.student_class)
        print("Total Marks: ", self.sum_numbers())
        print("Average Marks:   ",round(self.average(),2))
        print("Grade:   ", self.grade())    
   


student_list= []                # List to store student objects
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = int(input("Enter your choice: "))          # Manu Base input from user
    if choice == 1:
        name = input("Enter the Name of Student : ")
        subjects = list(input ("Enter Subjects of " + name + " comma seperated : ").split(","))
        marks = list(map(int, input("Enter Marks of " + name + " comma seperated : ").split(",")))
        if (len(subjects) != len(marks)):
            print("Error: Number of subjects and marks do not match.")
            continue
        class_name = input("Enter Class of " + name + " : ")
        student = Student(name, subjects, marks, class_name)   # Create a new student object and add it to the list
        student_list.append(student)                           

    elif choice == 2:
        for student in student_list:
            student.display()                   # Display details of each student in the list
            print("--------------------")
    elif choice == 3:                           # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")
