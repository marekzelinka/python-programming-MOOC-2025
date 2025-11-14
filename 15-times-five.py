"""
Programming exercise: Name and age

Please write a program which asks the user for their name and year of birth. The
program then prints out a message as follows:

What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021
"""

name = input("What is your name? ")
year_born = int(input("Which year were you born? "))

selected_year = 2021
age_in_selected_year = selected_year - year_born

print(
    f"Hi {name}, you will be {age_in_selected_year} years old at the end of the year {selected_year}"
)
