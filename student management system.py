# Student Management System using Python OOP

# Class to store student info
class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    # Display student info
    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("----------------------")

# List to hold all students
students = []

print("Welcome to the Student Management System!")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == '1':
        student_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        student_obj = Student(student_id, name, age, course)
        students.append(student_obj)
        print("Student added successfully!")

    # Display all students
    elif choice == '2':
        if not students:
            print("No students available.")
        else:
            for student_obj in students:
                student_obj.display()

    # Search student by ID
    elif choice == '3':
        search_id = input("Enter ID to search: ")
        found = False
        for student_obj in students:
            if student_obj.student_id == search_id:
                student_obj.display()
                found = True
                break
        if not found:
            print("Student not found.")

    # Update student info
    elif choice == '4':
        update_id = input("Enter ID to update: ")
        for student_obj in students:
            if student_obj.student_id == update_id:
                student_obj.name = input("Enter new name: ")
                student_obj.age = input("Enter new age: ")
                student_obj.course = input("Enter new course: ")
                print("Student updated successfully!")
                break
        else:
            print("Student not found.")

    # Delete student
    elif choice == '5':
        delete_id = input("Enter ID to delete: ")
        for student_obj in students:
            if student_obj.student_id == delete_id:
                students.remove(student_obj)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found.")

    # Exit program
    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
