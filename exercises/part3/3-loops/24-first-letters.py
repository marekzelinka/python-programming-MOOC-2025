"""
Programming exercise:
First letters of words
Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

An example of expected behaviour:

Sample output

Please type in a sentence: Humpty Dumpty sat on a wall
H
D
s
o
a
w
"""

string = input("Please type in a sentence: ")

string = " " + string

index = 0

while index < len(string):
    before_char = string[index - 1]
    current = string[index]

    if before_char == " " and current != " ":
        print(current)

    index += 1
