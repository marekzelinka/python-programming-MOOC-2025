"""
Programming exercise: Seconds in a day

Please write a program which asks the user for a number of days. The program
then prints out the number of seconds in the amount of days given.

The program should function as follows:

How many days? 1
Seconds in that many days: 86400

Another example:

How many days? 7
Seconds in that many days: 604800
"""

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
seconds_in_day = hours_in_day * minutes_in_hour * seconds_in_minute


day_count = int(input("How many days? "))
seconds_in_days = seconds_in_day * day_count
print(f"Seconds in that many days: {seconds_in_days}")
