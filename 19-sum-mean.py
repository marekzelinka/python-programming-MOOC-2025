"""
Programming exercise: Sum and mean

Please write a program which asks the user for four numbers. The program then
prints out the sum and the mean of the numbers.

The program should function as follows:


Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""

numbers_count = 4

a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))

sum_of_numbers = a + b + c + d
mean_of_numbers = sum_of_numbers / numbers_count

print(f"The sum of the numbers is {sum_of_numbers} and the mean is {mean_of_numbers}")
