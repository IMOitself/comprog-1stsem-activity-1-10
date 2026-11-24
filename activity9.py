# Programmed By: █████
# Date Programmed: 10/14/2024
# Date Submitted: 10/18/2024
# Activity Title: Activity 9 - What is the color of the square

print("CHESSBOARD: What is the color of the square?\n")

print("Each square on the chessboard has a designated input_position.")
print("The chessboard has 8 columns and 8 rows.")
print("Columns are represented by letters and rows and represented by numbers")

input_position = input("\nEnter the input_position of the square: ")

color = ""

column_A = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
column_B = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"]
column_C = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
column_D = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
column_E = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
column_F = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
column_G = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]
column_H = ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]

columns = [column_A, column_B, column_C, column_D, column_E, column_F, column_G, column_H]

reverseList = False
isBlack = True

for column in columns:
    if reverseList:
        column.reverse() # start at the end :D

    for value in column:
        if isBlack:
            if input_position == value:
                color = "black"
        else:
            if input_position == value:
                color = "white"

        isBlack = not isBlack # alternate :D

    reverseList = not reverseList

if color == "":
    print("invalid input.")
else:
    print("\nThe color of %s is %s." % (input_position, color))