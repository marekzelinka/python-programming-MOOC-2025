"""
Programming exercise:
Alphabetically in the middle

Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

You may assume the letters will be either all uppercase, or all lowercase.

Some examples of expected behaviour:

Sample output

1st letter: x
2nd letter: c
3rd letter: p
The letter in the middle is p

Sample output

1st letter: C
2nd letter: B
3rd letter: A
The letter in the middle is B
"""

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3
elif letter2 > letter3:
    if letter3 > letter1:
        middle = letter3
    else:
        middle = letter1
else:
    if letter2 > letter1:
        middle = letter2
    else:
        middle = letter1

print(f"The letter in the middle is {middle}")
