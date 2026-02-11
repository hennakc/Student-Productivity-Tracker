
college_name = "SCMS College of Technology"
college_address = input("Enter College Address: ")

stud_name = input("Enter Student Name: ")
degree = input("Enter Degree: ")
reg_no = input("Enter Register Number: ")
branch = input("Enter Branch: ")


n = int(input("Enter number of subjects: "))

subjects = []
total_marks = 0

for i in range(n):
    print(f"\nEnter details for Subject {i+1}")
    code = input("Subject Code: ")
    name = input("Subject Name: ")
    marks = int(input("Marks Scored: "))

    if marks >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    subjects.append([code, name, marks, result])
    total_marks += marks

average = total_marks / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n\t\tSCMS College of Technology")
print("\t\t" + college_address)

print("\n\t\t\tMARK STATEMENT")
print("\t\t------------------------------------\n")

print(f"Stud Name:\t{stud_name}\t\tDegree:\t{degree}")
print(f"Reg No   :\t{reg_no}\t\tBranch:\t{branch}")

print("\n" + "-" * 75)
print("Subject Code\tSubject\t\tMarks Scored\tResult")
print("-" * 75)

for sub in subjects:
    print(f"{sub[0]}\t\t{sub[1]}\t\t{sub[2]}\t\t{sub[3]}")

print("-" * 75)
print(f"\tTotal Marks : {total_marks}")
print(f"\tGrade Obtained: {grade}")
