def add_student(students):
    student_id = input("Enter your ID: ")
    name = input("Enter your name: ")
    dob = input("Enter your dob(DD-MM-YYYY): ")
    student = {'id': student_id, 'name': name, 'dob': dob, 'marks': {}}
    students.append(student)

def add_course(courses):
    course_id = input("Enter your course_ID: ")
    name = input("Enter your course name: ")
    course = {'id': course_id, 'name': name}
    courses.append(course)

def list_students(students):
    print("List of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses(courses):
    print("List of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def input_marks(students):
    for i in range(len(students)):
        student_id = input("Enter your id: ")
        for student in students:
            if student['id'] == student_id:
                for i in range(num_courses):
                    course_id = input("Enter your course_id: ")
                    student['marks'][course_id] = float(input("Enter your marks: "))
                    print("Marks added successfully.")

def show_student_marks(students, courses):
    for i in range(len(students)):
        student_id = input("Enter your ID: ")
        for student in students:
            if student['id'] == student_id:
                for course in range(len(courses)):
                    course_id = input("Enter your course_id: ")
                    marks = student['marks'].get(course_id, "N/A")
                    print(f"Student ID: {student_id}, Course ID: {course_id}, Marks: {marks}")


# Example usage:
students_list = []
courses_list = []

# Input number of students
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    add_student(students_list)

# Input number of courses
num_courses = int(input("Enter the number of courses: "))
for i in range(num_courses):
    add_course(courses_list)

# List students and courses
list_students(students_list)
list_courses(courses_list)

# Select a course and input marks for a student
input_marks(students_list)

# Show student marks for a given course
show_student_marks(students_list, courses_list)
