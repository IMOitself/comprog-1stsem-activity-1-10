# Programmed By: █████
# Date Programmed: 10/14/2024
# Date Submitted: 10/18/2024
# Activity Title: Activity 6 Vowel or Consonant

print("VOWEL OR CONSONANT\n")

char = input("Enter a letter: ")

if char == "a":
    print("%r is a vowel." % (char))
elif char == "e":
    print("%r is a vowel." % (char))
elif char == "i":
    print("%r is a vowel." % (char))
elif char == "o":
    print("%r is a vowel." % (char))
elif char == "u":
    print("%r is a vowel." % (char))
elif char == "b":
    print("%r is a consonant." % (char))
elif char == "c":
    print("%r is a consonant." % (char))
elif char == "d":
    print("%r is a consonant." % (char))
elif char == "f":
    print("%r is a consonant." % (char))
elif char == "g":
    print("%r is a consonant." % (char))
elif char == "h":
    print("%r is a consonant." % (char))
elif char == "j":
    print("%r is a consonant." % (char))
elif char == "k":
    print("%r is a consonant." % (char))
elif char == "l":
    print("%r is a consonant." % (char))
elif char == "m":
    print("%r is a consonant." % (char))
elif char == "n":
    print("%r is a consonant." % (char))
elif char == "p":
    print("%r is a consonant." % (char))
elif char == "q":
    print("%r is a consonant." % (char))
elif char == "r":
    print("%r is a consonant." % (char))
elif char == "s":
    print("%r is a consonant." % (char))
elif char == "t":
    print("%r is a consonant." % (char))
elif char == "v":
    print("%r is a consonant." % (char))
elif char == "w":
    print("%r is a consonant." % (char))
elif char == "x":
    print("%r is a consonant." % (char))
elif char == "y":
    print("%r is a consonant." % (char))
elif char == "z":
    print("%r is a consonant." % (char))

else:
    isNumber = char.isnumeric()

    if isNumber:
        print("%r is a number not a letter." % (char))
    else:
        print("%r contains more than one character." % (char))