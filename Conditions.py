'''
You forgot to put the check for "e" in vowel checker.

'''

#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.

percent_grade = int(input("Enter your grade as a percent: "))
if percent_grade > 100 or percent_grade < 0:
    print("ERROR")
elif percent_grade >= 97 and percent_grade <= 100:
    print("Your grade is: A+")
elif percent_grade >= 93 and percent_grade <= 96:
    print("Your grade is: A")
elif percent_grade >= 90 and percent_grade <= 92:
    print("Your grade is: A-")
elif percent_grade >= 87 and percent_grade <= 89:
    print("Your grade is: B+")
elif percent_grade >= 83 and percent_grade <= 86:
    print("Your grade is: B")
elif percent_grade >= 80 and percent_grade <= 82:
    print("Your grade is: B-")
elif percent_grade >= 77 and percent_grade <= 79:
    print("Your grade is: C+")
elif percent_grade >= 73 and percent_grade <= 76:
    print("Your grade is: C")
elif percent_grade >= 70 and percent_grade <= 72:
    print("Your grade is: C-")
elif percent_grade >= 67 and percent_grade <= 69:
    print("Your grade is: D+")
elif percent_grade >= 65 and percent_grade <= 66:
    print("Your grade is: D")
else:
    print("You failed")

# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.
user = input(str("Type anything: "))
count_a = 0
count_i = 0
count_o = 0
count_u = 0
count = 0
for i in range(len(user)):
    if user[i].lower() == "a":
        count_a += 1
    elif user[i].lower() == "i":
        count_i += 1
    elif user[i].lower() == "o":
        count_o += 1
    elif user[i].lower() == "u":
        count_u += 1
if count_a != 0:
    count += 1
if count_i != 0:
    count += 1
if count_o != 0:
    count += 1
if count_u != 0:
    count += 1
print("You have " + str(count) + " different vowels in your string")


# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if (b**2 + (4*a*c)) < 0 or a == 0:
    print("No solution")
else:
    quadratic_1 = (-b + (((b**2) + (4*a*c))**0.5))/(2*a)
    quadratic_2 = (-b - (((b**2) + (4*a*c))**0.5))/(2*a)

    if (b**2 + (4*a*c)) == 0:
        print("There is one solution")
        print(round(quadratic_1,2), round(quadratic_2,2))
    else:
        print("There are two solutions")
        print(round(quadratic_1,2), round(quadratic_2,2))