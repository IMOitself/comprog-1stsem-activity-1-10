# Programmed By: █████
# Date Programmed: 10/14/2024
# Date Submitted: 10/18/2024
# Activity Title: Activity 8 - Classifying Triangles

print("CLASSIFYING TRIANGLES\n")

print("Enter the measurement of each side of the triangle:\n")

firstSide = int(input("First Side: "))
secondSide = int(input("Second Side: "))
thirdSide = int(input("Third Side: "))


if firstSide == secondSide == thirdSide:
    print("It is an equilateral triangle.")
elif firstSide == secondSide or firstSide == thirdSide or secondSide == thirdSide:
    print("It is an isosceles triangle.")
else:
    print("It is an scalene triangle.")
