# Programmed By: █████
# Date Programmed: 9/25/2024
# Date Submitted: 9/25/2024
# Activity Title: Activity 4 - input() method

print("GRADE COMPUTATION\n")
first_name = input("Student's first name: ")
last_name = input("Student's last name: ")
program = input("Program: ")
year_level = input("Year level: ")

print("\nEnter the student's grade for each term:")

prelim = float(input("Prelim: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))

grade = (prelim * 0.30) + (midterm * 0.30) + (final * 0.40)
   
print("\n*---*---*---*---*---*---*---*---*\n")

print("Name: " + last_name + ", " + first_name)
print("Program Code:", program + year_level)
print("Computed Grade:", grade)

print("\n*---*---*---*---*---*---*---*---*\n")


