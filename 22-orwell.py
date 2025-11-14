"""
Programming exercise: Orwell

Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

Sample output

Please type in a number: 2020

Sample output

Please type in a number: 1984
Orwell
"""

n = int(input("Please type in a number: "))

novel_published_date = 1984

if n == novel_published_date:
    print("Orwell")
