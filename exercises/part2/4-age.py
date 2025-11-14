"""
Programming exercise:
Age of maturity


Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

Some examples of expected behaviour:
Sample output

How old are you? 12
You are not of age!
Sample output

How old are you? 32
You are of age!
"""

age_of_maturity = 18

age = int(input("How old are you? "))

is_mature = age >= age_of_maturity

if is_mature:
    print("You are of age!")
else:
    print("You are not of age!")
