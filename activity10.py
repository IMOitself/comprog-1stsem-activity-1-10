# Programmed By: █████
# Date Programmed: 10/14/2024
# Date Submitted: 10/18/2024
# Activity Title: Activity 10 - College Grade Computation (with equivalent)

print("COLLEGE GRADE COMPUTATION\n")

firstName = input("Student's First Name: ")
lastName = input("Student's Last Name: ")
course = input("Course Title: ")

print()

midterm = eval(input("\tMidterm Grade: "))
finals = eval(input("\tFinals Grade: "))

print("\n*---*---*--- FINAL GRADE ---*---*---*")

total = (midterm + finals) / 2
equivalent = 0.0

if total <= 74.49:
    equivalent = 5
elif total <= 75.49:
    equivalent = 3
elif total <= 79.49:
    equivalent = 2.75
elif total <= 81.49:
    equivalent = 2.5
elif total <= 84.49:
    equivalent = 2.25
elif total <= 87.49:
    equivalent = 2
elif total <= 90.49:
    equivalent = 1.75
elif total <= 93.49:
    equivalent =  1.5
elif total <= 96.49:
    equivalent =  1.25
elif total <= 100:
    equivalent =  1

print(f"Student:\t\t{lastName}, {firstName}")
print(f"Course Title:\t{course}")
print(f"Final Grade:\t{total}")
print(f"Equivalent:\t\t{equivalent}")

