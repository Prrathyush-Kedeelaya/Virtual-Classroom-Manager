import logging


class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return [student.name for student in self.students]

    def schedule_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        return [assignment.name for assignment in self.assignments]

    def remove_assignment(self, assignment):
        self.assignments.remove(assignment)


# Define a Student class to manage students
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def submit_assignment(self, assignment):
        assignment.add_submission(self.student_id)
        logging.info(f"Assignment submitted by Student {self.student_id} in {assignment.classroom.name}.")


# Define an Assignment class to manage assignments
class Assignment:
    def __init__(self, name, classroom):
        self.name = name
        self.classroom = classroom
        self.submissions = []  # Initialize an empty list to store submissions

    def add_submission(self, student_id):
        self.submissions.append(student_id)


def main():
    # Initialize a list to hold classrooms
    classrooms = []

    # Initialize a logging system
    logging.basicConfig(filename="virtual_classroom.log", level=logging.INFO)

    while True:
        print("Options:")
        print("1. Add Classroom")
        print("2. Add Student to Classroom")
        print("3. List Students in Classroom")
        print("4. Schedule Assignment in Classroom")
        print("5. List Assignments in Classroom")
        print("6. Submit Assignment")
        print("7. Remove Classroom")
        print("8. List All Classrooms")
        print("9. Remove Student From a Classroom")
        print("10. View Assignment Submissions")
        print("11. View Class Details")
        print("12. Update Student Information")
        print("13. Update Assignment Details")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Classroom Name: ")
            classroom = Classroom(name)
            classrooms.append(classroom)
            print(f"Classroom {name} has been created.")

        elif choice == "2":
            name = input("Enter Student Name: ")
            student_id = input("Enter Student ID: ")
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                student = Student(name, student_id)
                classroom.add_student(student)
                print(f"Student {name} has been enrolled in {classroom_name}.")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "3":
            classroom_name = input("Enter Classroom Name: ")
            classroom = next((c for c in classrooms if c.name == classroom_name), None)
            if classroom:
                students = classroom.list_students()
                print(f"Students in {classroom_name}: {', '.join(students)}")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "4":
            name = input("Enter Assignment Name: ")
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                assignment = Assignment(name, classroom)
                classroom.schedule_assignment(assignment)
                print(f"Assignment for {classroom_name} has been scheduled.")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "5":
            classroom_name = input("Enter Classroom Name: ")
            classroom = next((c for c in classrooms if c.name == classroom_name), None)
            if classroom:
                assignments = classroom.list_assignments()
                print(f"Assignments in {classroom_name}: {', '.join(assignments)}")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "6":
            student_id = input("Enter Student ID: ")
            classroom_name = input("Enter Classroom Name: ")
            assignment_name = input("Enter Assignment Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                assignment = next((a for a in classroom.assignments if a.name == assignment_name), None)

                if assignment:
                    student = next((s for s in classroom.students if s.student_id == student_id), None)

                    if student:
                        student.submit_assignment(assignment)
                    else:
                        print(f"Student {student_id} is not enrolled in {classroom_name}.")
                else:
                    print(f"Assignment {assignment_name} does not exist in {classroom_name}.")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "7":
            # Option to remove a classroom
            classroom_name = input("Enter Classroom Name to remove: ")
            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                classrooms.remove(classroom)
                print(f"Classroom {classroom_name} has been removed.")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "8":
            # Option to list all classrooms
            if classrooms:
                print("List of Classrooms:")
                for classroom in classrooms:
                    print(classroom.name)
            else:
                print("No classrooms exist.")

        elif choice == "9":
            # Option to remove a student from a classroom
            student_id = input("Enter Student ID to remove: ")
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                student = next((s for s in classroom.students if s.student_id == student_id), None)

                if student:
                    classroom.students.remove(student)
                    print(f"Student {student.name} with ID {student_id} has been removed from {classroom_name}.")
                else:
                    print(f"Student with ID {student_id} is not enrolled in {classroom_name}.")

        elif choice == "10":
            # Option to view assignment submissions for a classroom
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                if classroom.assignments:
                    print(f"Assignment Submissions in {classroom_name}:")
                    for assignment in classroom.assignments:
                        submissions = [student.name for student in classroom.students if
                                       student.student_id in assignment.submissions]
                        print(f"Assignment: {assignment.name}, Submissions: {', '.join(submissions)}")
                else:
                    print(f"No assignments scheduled in {classroom_name}.")

        elif choice == "11":
            # Option to view class details
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                print(f"Class Details for {classroom_name}:")
                print(f"Classroom Name: {classroom.name}")
                print(f"Students Enrolled: {', '.join(classroom.list_students())}")
                print(f"Assignments Scheduled: {', '.join(classroom.list_assignments())}")
            else:
                print(f"Classroom {classroom_name} does not exist.")


        elif choice == "12":
            # Option to update student information
            student_id = input("Enter Student ID to update: ")
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                student = next((s for s in classroom.students if s.student_id == student_id), None)

                if student:
                    new_name = input("Enter new student name: ")
                    student.name = new_name
                    print(f"Student {student_id} has been updated with the new name: {new_name}.")
                else:
                    print(f"Student with ID {student_id} is not enrolled in {classroom_name}.")
            else:
                print(f"Classroom {classroom_name} does not exist.")

        elif choice == "13":
            # Option to update assignment details
            assignment_name = input("Enter Assignment Name to update: ")
            classroom_name = input("Enter Classroom Name: ")

            classroom = next((c for c in classrooms if c.name == classroom_name), None)

            if classroom:
                assignment = next((a for a in classroom.assignments if a.name == assignment_name), None)

                if assignment:
                    new_name = input("Enter new assignment name: ")
                    assignment.name = new_name
                    print(
                        f"Assignment {assignment_name} in {classroom_name} has been updated with the new name: {new_name}.")
                else:
                    print(f"Assignment {assignment_name} does not exist in {classroom_name}.")
            else:
                print(f"Classroom {classroom_name} does not exist.")


        elif choice == "14":
            # Option to exit
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
