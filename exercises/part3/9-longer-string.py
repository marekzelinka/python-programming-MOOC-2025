"""
Programming exercise:
The longer string

Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output

Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output

Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output

Please type in string 1: hey
Please type in string 2: bye
The strings are equally long
"""

first_word = input("Please type in string 1: ")
second_word = input("Please type in string 2: ")

if len(first_word) > len(second_word):
    print(f"{first_word} is longer")
elif len(second_word) > len(first_word):
    print(f"{second_word} is longer")
else:
    print("The strings are equally long")
