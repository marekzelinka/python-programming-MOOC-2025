"""
Programming exercise:
The elder

Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

Some examples of expected behaviour:

Sample output

Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada

Sample output

Person 1:
Name: Bill
Age: 1
Person 2:
Name: Jean
Age: 1
Bill and Jean are the same age
"""

print("Person 1:")

person_a_name = input("Name: ")
person_a_age = int(input("Age: "))

print("Person 2:")

person_b_name = input("Name: ")
person_b_age = int(input("Age: "))

if person_a_age > person_b_age:
    print(f"The elder is {person_a_name}")
elif person_b_age > person_a_age:
    print(f"The elder is {person_b_name}")
else:
    print(f"{person_a_name} and {person_b_name} are the same age")
