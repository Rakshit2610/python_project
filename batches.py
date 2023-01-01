@@ -1,192 +1,194 @@
import json
import csv
import pandas
from batch import createBatch
import json
from matplotlib import pyplot
from department import createDepartment

def createStudent(student_id, name):
    class_roll_number = int(student_id[5:7])
    batch_id = student_id[:5]
    data = [student_id, name, class_roll_number, batch_id]
def createBatch(batch_name):
    batch_id = batch_name[:3] + batch_name[6:8]
    department_id = batch_id[:3]
    csv_reader = []
    with open("student.csv", "r", newline = "\n") as f:
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    with open("student.csv", "a", newline = "\n") as f:
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == student_id):
                print("Student ID already exists")
                return
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == batch_id):
            print("Batch ID already exists")
            return
    data = [batch_id, batch_name, department_id, "", ""]
    with open("batch.csv", "a", newline = "\n") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
    with open("batch.csv", "r", newline = "\n") as f:
    print("Enter courses in batch: ")
    while(True):
        course_id = input("Enter course ID (to stop enter STOP): ")
        with open("batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        if(csv_reader[len(csv_reader) - 1][3] != ""):
            check = 0
            temp = csv_reader[len(csv_reader) - 1][3].split(":")
            for x in temp:
                if(x == course_id):
                    print("Course already added")
                    check = 1
            if(check == 1):
                continue
        if(course_id.upper() == "STOP"):
            break
        else:
            with open("course.csv", "r", newline = "\n") as f:
                csv_reader = list(csv.reader(f, delimiter=","))
            check = 0
            for i in range(0, len(csv_reader)):
                if(csv_reader[i][0] == course_id):
                    with open("batch.csv", "r", newline = "\n") as f:
                        csv_reader = list(csv.reader(f, delimiter=","))
                    check = 1
                    if(csv_reader[len(csv_reader) - 1][3] == ""):
                        csv_reader[len(csv_reader) - 1][3] = csv_reader[len(csv_reader) - 1][3] + course_id
                    else:
                        csv_reader[len(csv_reader) - 1][3] = csv_reader[len(csv_reader) - 1][3] + ":" + course_id
                    df = pandas.read_csv("batch.csv")
                    df.loc[len(csv_reader) - 2, "list_of_courses"] = csv_reader[len(csv_reader) - 1][3]
                    df.to_csv("batch.csv", index = False)
            if(check == 0):
                print("Course does not exist. Please create course first.")
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == batch_id):
        if(csv_reader[i][0] == department_id):
            check = 1
            if(csv_reader[i][4] == ""):
                csv_reader[i][4] = csv_reader[i][4] + student_id
            if(csv_reader[i][2] == ""):
                csv_reader[i][2] = csv_reader[i][2] + batch_id
            else:
                csv_reader[i][4] = csv_reader[i][4] + ":" + student_id
            df = pandas.read_csv("batch.csv")
            df.loc[i-1, "list_of_students"] = csv_reader[i][4]
            df.to_csv("batch.csv", index = False)
                csv_reader[i][2] = csv_reader[i][2] + ":" + batch_id
            df = pandas.read_csv("department.csv")
            df.loc[i-1, "list_of_batches"] = csv_reader[i][2]
            df.to_csv("department.csv", index = False)
    if(check == 0):
        print("Batch does not exist.... Creating new batch")
        batch_name = batch_id[:3] + " 20" + batch_id[3:] + "-" + str(int(batch_id[3:]) + 4)
        createBatch(batch_name)
        print("Department does not exist.... Creating new department")
        department_name = input("Enter department name: ")
        createDepartment(department_id, department_name)
        with open("department.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        csv_reader[len(csv_reader) - 1][2] = csv_reader[len(csv_reader) - 1][2] + batch_id
        df = pandas.read_csv("department.csv")
        df.loc[len(csv_reader) - 2, "list_of_batches"] = csv_reader[len(csv_reader) - 1][2]
        df.to_csv("department.csv", index = False)

def viewStudents(batch_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    courses = []
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == batch_id):
            courses = list(csv_reader[i][3].split(":"))
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        for j in range(0, len(courses)):
            if(csv_reader[i][0] == courses[j]):
                if(csv_reader[i][2] == ""):
                    temp = {}
                    temp[student_id] = 0
                    csv_reader[i][2] = json.dumps(temp)
                else:
                    temp = json.loads(csv_reader[i][2])
                    temp[student_id] = 0
                    csv_reader[i][2] = json.dumps(temp)
                df = pandas.read_csv("course.csv")
                df.loc[i-1, "marks_obtained"] = csv_reader[i][2]
                df.to_csv("course.csv", index = False)
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("Batch ID does not exist")
        return
    print("Students in " + batch_id + ":")
    for student in students:
        print(student)

def updateStudent(ostudent_id):
    csv_reader = []
    with open("student.csv", "r", newline = "\n") as f:
def viewCourses(batch_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    courses = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == ostudent_id):
        if(csv_reader[i][0] == batch_id):
            check = 1
            courses = csv_reader[i][3].split(":")
            break
    if(check == 0):
        print("Student ID does not exist")
        print("Batch ID does not exist")
        return
    while(True):
        print("Press 1 to update name")
        print("Press 2 to update student ID")
        print("Press 0 to exit")
        x = int(input("Enter your choice: "))
        if(x == 0):
            break
        elif(x == 1):
            name = input("Enter updated name: ")
            df = pandas.read_csv("student.csv")
            df.loc[i-1, "Name"] = name
            df.to_csv("student.csv", index = False)
        elif(x == 2):
            nstudent_id = input("Enter updated student ID: ")
            df = pandas.read_csv("student.csv")
            df.loc[i-1, "Student_ID"] = nstudent_id
            df.to_csv("student.csv", index = False)
            removeStudent(ostudent_id)
            createStudent(nstudent_id, csv_reader[i][1])
            ostudent_id = nstudent_id
            with open("student.csv", "r", newline = "\n") as f:
                csv_reader = list(csv.reader(f, delimiter=","))
        else:
            print("Invalid input. Try again.")
    print("Courses in " + batch_id + ":")
    for course in courses:
        print(course)

def removeStudent(student_id):
    csv_reader = []
    with open("student.csv", "r", newline = "\n") as f:
def viewPerformance(batch_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == student_id):
        if(csv_reader[i][0] == batch_id):
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("Student ID does not exist")
        print("Batch ID does not exist")
        return
    df = pandas.read_csv("student.csv")
    df.set_index("Student_ID")
    df = df.drop(df.index[i-1])
    df.to_csv("student.csv", index = False)
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        if(i == 0):
            continue
        temp = csv_reader[i][2]
        temp = json.loads(temp)
        if student_id in temp:
            del temp[student_id]
        csv_reader[i][2] = json.dumps(temp)
    df = pandas.read_csv("course.csv")
    for i in range(1, len(csv_reader)):
        df.loc[i-1, "marks_obtained"] = csv_reader[i][2]
    df.to_csv("course.csv", index = False)
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        if(i == 0):
            continue
        temp = list(csv_reader[i][4].split(":"))
        if student_id in temp:
            temp.remove(student_id)
        a = ":"
        csv_reader[i][4] = a.join(temp)
    df = pandas.read_csv("batch.csv")
    for i in range(1, len(csv_reader)):
        df.loc[i-1, "list_of_students"] = csv_reader[i][4]
    df.to_csv("batch.csv", index = False)
    for student in students:
        with open("student.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(student == csv_reader[i][0]):
                print("Student ID: " + student)
                print("Student Name: " + csv_reader[i][1])
                print("Student Roll Number: " + csv_reader[i][2])
        with open("course.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        all_marks = []
        for i in range(1, len(csv_reader)):
            all_marks.append(json.loads(csv_reader[i][2]))
        total_marks = 0
        divs = 0
        for subjects in all_marks:
            if(isinstance(subjects.get(student), int)):
                total_marks += subjects.get(student)
                divs += 1
        print("Percentage obtained: " + str(total_marks/divs))
        print()

def reportCard(student_id):
    name = ""
    csv_reader= []
    with open("student.csv", "r", newline = "\n") as f:

def pieChart(batch_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == student_id):
        if(csv_reader[i][0] == batch_id):
            check = 1
            name = csv_reader[i][1]
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("Student ID does not exist")
        print("Batch ID does not exist")
        return
    f = open((student_id + ".txt"), "w")
    a = "Student ID: " + student_id + "\n"
    b = "Name: " + name + "\n"
    f.writelines([a, b])
    with open("course.csv", "r", newline = "\n") as fx:
        csv_reader = list(csv.reader(fx, delimiter=","))
    marks = []
    subjects = []
    for i in range(1, len(csv_reader)):
        marks.append(json.loads(csv_reader[i][2]))
        subjects.append(csv_reader[i][1])
    total_marks = 0
    divs = 0
    for i in range(0, len(subjects)):
        temp = marks[i]
        if(isinstance(temp.get(student_id), int)):
            subject_marks = "Marks in " + subjects[i] + ": " + str(temp.get(student_id)) + "% \n"
            divs += 1
            total_marks += temp.get(student_id)
            f.write(subject_marks)
    grade = "Grade obtained: " + gradeCheck(total_marks/divs) + " \n"
    f.write(grade)
    f.close()

def gradeCheck(a):
    if(a >= 90):
        return "A"
    elif(a >= 80):
        return "B"
    elif(a >= 70):
        return "C"
    elif(a >= 60):
        return "D"
    elif(a >= 50):
        return "E"
    else:
        return "F"
    percentages = [">=90", ">=80", ">=70", ">=60", ">=50", "Failed"]
    numbers = [0, 0, 0, 0, 0, 0]
    for student in students:
        with open("course.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        all_marks = []
        for i in range(1, len(csv_reader)):
            all_marks.append(json.loads(csv_reader[i][2]))
        total_marks = 0
        divs = 0
        for subjects in all_marks:
            if(isinstance(subjects.get(student), int)):
                total_marks += subjects.get(student)
                divs += 1
        percentage = total_marks/divs
        if(percentage >= 90):
            numbers[0] += 1
        elif(percentage >= 80):
            numbers[1] += 1
        elif(percentage >= 70):
            numbers[2] += 1
        elif(percentage >= 60):
            numbers[3] += 1
        elif(percentage >= 50):
            numbers[4] += 1
        else:
            numbers[5] += 1
    for i in range(len(numbers) - 1, -1, -1):
        if(numbers[i] == 0):
            del numbers[i]
            del percentages[i]
    pyplot.pie(numbers, labels = percentages)
    pyplot.show()
