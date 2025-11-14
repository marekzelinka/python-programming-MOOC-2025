"""
Programming exercise: Sum and product

Please write a program which asks the user for two numbers. The program will
then print out the sum and the product of the two numbers.

The program should function as follows:

Number 1: 3
Number 2: 7
The sum of the numbers: 10
The product of the numbers: 21
"""

a = int(input("Number 1: "))
b = int(input("Number 2: "))

sum_of_numbers = a + b
product_of_numbers = a * b

print(f"The sum of the numbers: {sum_of_numbers}")
print(f"The product of the numbers: {product_of_numbers}")
