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
        print("ID:", sid, "Name:", data["name"])

def add_marks(student_id, marks):
    if student_id in students:
        students[student_id]["marks"] = marks
    else:
        print("Student not found")

def view_marks():
    for sid, data in students.items():
        print("ID:", sid, "Marks:", data["marks"])

def main():
    print("Student Management System")

    # ✅ FIRST add students
    add_student(1, "Rahul")
    add_student(2, "Ananya")

    # ✅ THEN add marks
    add_marks(1, 85)
    add_marks(2, 92)

    # ✅ Display data
    view_students()
    view_marks()

if __name__ == "__main__":
    main()
