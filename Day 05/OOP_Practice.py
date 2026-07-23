

# class Student:
#     def __init__(self,name,age,course):
#         self.name= name
#         self.age =age
#         self.course = course
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")


# student1= Student("John", 20, "Computer Science")
# student2 = Student("Alice", 22, "Mathematics")
# # student1.display()
# # student2.display()


# class Employee:
#     def __init__(self,name,salary,Employee_ID):
#         self.name= name
#         self.salary = salary
#         self.Employee_ID = Employee_ID
#     def Employee_display(self):
#         print(f"Name :{self.name}, Salary :{self.salary}, Employee ID : {self.Employee_ID}")    

# employee1 = Employee("John", 50000, "E001")
# employee2 = Employee("Alice", 60000, "E002 ")

# # employee1.Employee_display()
# # employee2.Employee_display()








# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def display(self):
#         print(f"Brand :{self.brand}, Model : {self.model}, Year : {self.year}")
#     def star(self):
#         print(f"{self.brand} {self.model} is starting.")


# Car1 = Car("Toyota", "Camry", 2020)
# Car2 = Car("Honda", "Civic", 2021)

# # Car1.display()
# # Car2.display()

# # Car1.star() 
# # Car2.star()


class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def display(self):
        print(f"Name : {self.name}, Age : {self.age}")


class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course = course
    def display(self):
        super().display()
        print(f"Course : {self.course}")

# private data member logic

class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.__salary = salary
    def set_salary(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary        
    def display(self):
        super().display()
        print(f"Salary : {self.get_salary()}")



student1 = Student("John", 20, "Computer Science")
employee1 = Employee("Alice", 30, 50000)

student1.display()
employee1.display()