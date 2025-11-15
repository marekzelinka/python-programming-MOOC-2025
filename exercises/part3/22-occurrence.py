"""
Programming exercise:
The second occurrence

Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output

Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output

Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output

Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.
"""

# string = input("Please type in a string: ")
# query = input("Please type in a substring: ")

# first_start = string.find(query)
# first_end = first_start + len(query)

# if first_start == -1:
#     print("The substring does not occur twice in the string.")
# else:
#     string = string[first_end:]
#     # print(first_start, first_end, string)

#     second_start = string.find(query)

#     if second_start == -1:
#         print("The substring does not occur twice in the string.")

#     else:
#         print(
#             f"The second occurrence of the substring is at index {first_end + second_start}."
#         )

string = input("Please type in a string: ")
query = input("Please type in a substring: ")

first_start_index = string.find(query)
first_end_index = first_start_index + len(query)

second_start_index = -1

if first_start_index != -1:
    string = string[first_end_index:]
    second_start_index = string.find(query)

if second_start_index == -1:
    print("The substring does not occur twice in the string.")
else:
    print(
        f"The second occurrence of the substring is at index {first_end_index + second_start_index}."
    )
