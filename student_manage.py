students = {}

def main():
    print("Student Management System")

if __name__ == "__main__":
    main()

students = {}

def add_marks(student_id, marks):
    if student_id in students:
        students[student_id]["marks"] = marks
    else:
        print("Student not found")

def view_marks():
    for sid, data in students.items():
        print(sid, data.get("marks"))

def main():
    add_marks(1, 85)
    add_marks(2, 92)
    view_marks()

if __name__ == "__main__":
    main()
