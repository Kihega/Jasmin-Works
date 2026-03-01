name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 20:
    print("Pass")
else:
    print("Fail")

classmates = []

for i in range(4):
    m = int(input("Enter marks of classmate: "))
    classmates.append(m)

average = sum(classmates) / len(classmates)

if marks > average:
    print(name, "is above average")
else:
    print(name, "is below average")
