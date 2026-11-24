# Programmed By: █████
# Date Programmed: 10/14/2024
# Date Submitted: 10/18/2024
# Activity Title: Activity 7 - No. of days in a month

print("DAYS IN A MONTH")

input_number = int(input("Enter a number from 1 to 12: "))

if input_number == 1:
    print("January has 31 days.")
elif input_number == 2:
    print("February has 28 days (29 during a leap year).")
elif input_number == 3:
    print("March has 31 days.")
elif input_number == 4:
    print("April has 30 days.")
elif input_number == 5:
    print("May has 31 days.")
elif input_number == 6:
    print("June has 30 days.")
elif input_number == 7:
    print("July has 31 days.")
elif input_number == 8:
    print("August has 31 days.")
elif input_number == 9:
    print("September has 30 days.")
elif input_number == 10:
    print("October has 31 days.")
elif input_number == 11:
    print("November has 30 days.")
elif input_number == 12:
    print("December has 31 days.")
elif input_number >= 13:
    print("invalid text. Only numbers 1 to 12 is allowed.")