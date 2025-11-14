"""
Programming exercise:Food expenditure

Please write a program which estimates a user's typical food expenditure.

The program asks the user how many times a week they eat at the student
cafeteria. Then it asks for the price of a typical student lunch, and for money
spent on groceries during the week.

Based on this information the program calculates the user's typical food
expenditure both weekly and daily.

The program should function as follows:

How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros
"""

days_in_week = 7


lunch_count = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_weekly_cost = float(
    input("How much money do you spend on groceries in a week? ")
)

weekly_average_food_cost = grocery_weekly_cost + lunch_count * lunch_price
daily_average_food_cost = weekly_average_food_cost / days_in_week

print("Average food expenditure:")
print(f"Daily: {daily_average_food_cost} euros")
print(f"Weekly: {grocery_weekly_cost + lunch_count * lunch_price} euros")
