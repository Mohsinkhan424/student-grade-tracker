import json
students = []
def add_student(name,grade):
    students.append({"name" : name, "grade" : grade})
    print(f" Added {name} Succesfully")

def view_students():
    if not students:
        print("No students found")
        return
    for i in students:
        print(i["name"], i["grade"])


def top_student():
    if not students:
        print("No students available to evaluate.")
        return
    top_grade = max(students, key = lambda p:p["grade"])
    print(f"{top_grade['name']} is the topper with {top_grade['grade']} grade")


def save_to_file():
    with open ("students.json", "w") as f:
        json.dump(students,f)
        print("Data saved to students.json successfully!")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Top Students")
    print("4. Save To File")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if choice == 1:
        name = input("Enter Student name: ")
        try:
            grade = int(input("Enter grade: "))
            add_student(name,grade)
        except ValueError:
            print("Enter a valid grade number")
    elif choice == 2:
        view_students()
    elif choice == 3:
        top_student()
    elif choice == 4:
        save_to_file()
    elif choice == 5:
        break