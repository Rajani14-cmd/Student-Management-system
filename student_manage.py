students = {}

def main():
    print("Student Management System")

if __name__ == "__main__":
    main()
    students = {}

def add_student(student_id, name):
    students[student_id] = {"name": name, "marks": None}

def view_students():
    for sid, data in students.items():
        print(sid, data["name"])

def main():
    add_student(1, "Rahul")
    add_student(2, "Ananya")
    view_students()

if __name__ == "__main__":
    main()
