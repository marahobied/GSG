class Course:
    course_id=0
    def __init__(self,course_name,course_level):
        Course.course_id+=1
        self.course_id=Course.course_id
        self.course_name=course_name
        self.course_level=course_level
class Student:
    student_id=0
    def __init__(self, student_name,student_level):
        Student.student_id+=1
        self.student_id=Student.student_id
        self.student_name=student_name
        self.student_level = student_level
        self.student_courses = []

    def add(self, course):
        if self.student_level == course.course_level:
            if course not in self.student_courses:
                self.student_courses.append(course)
                print(f"Course {course.course_name} added to {self.student_name}'s courses")
            else:
                print(f"{self.student_name} is already enrolled in {course.course_name}")
        else:
            print(f"Error: {self.student_name} and {course.course_name} are in different levels")

    def display(self):
        print(f"Name: {self.student_name}")
        print(f"Level: {self.student_level}")
        print("Courses enrolled:")
        for course in self.student_courses:
            print(f"- {course.course_name}")


students = []
courses = []

while True:
    print("Selaect Choice Please :")
    print("1. Add new student")
    print("2. Remove student")
    print("3. Edit student")
    print("4. Display all students")
    print("5. Create new course")
    print("6. Add course to student")
    print("0. Exit \n")
    choice=(int)(input())
    if choice==0 :
        break
    elif choice==1:
        name=input("Enter student name :")
        level=""
        while level not in ["A","B","C"]:
            level = input("Enter student level (A-B-C): ").upper()
        student=Student(name,level)
        students.append(student)
        print("student saved successfully !")
    elif choice==2:
        id=(int)(input("Enter the student id:"))
        for student in students:
            if student.student_id==id:
                students.remove(student)
                print("Delete done successfully")
                break
        else:
             print("User not exist")
    elif choice==3:
        id = int(input("Enter student ID: "))
        for student in students:
            if student.student_id==id:
                name=input("Enter a new name :")
                level=""
                while level not in ["A", "B", "C"]:
                    level = input("Enter student new  level (A, B or C): ").upper()
                student.student_name=name
                student.student_level=level
                print("Edit done successfully")
                break
        else:
                print("User not exist")
    elif choice==4:
        print("All Students:")
        for student in students:
            student.display()
    elif choice==5:
        name = input("Enter class name :")
        level=""
        while level not in ["A", "B", "C"]:
            level = input("Enter student level (A, B or C): ").upper()
        course=Course(name,level)
        courses.append(course)
        print("Course saved successfully")
    elif choice == 6:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        student = None
        for s in students:
            if s.student_id == student_id:
                student = s
                break
        else:
            print("Student not exist")
            continue
        course = None
        for c in courses:
            if c.course_id == course_id:
                course = c
                break
        else:
            print("Course not exist")
            continue
        student.add(course)



