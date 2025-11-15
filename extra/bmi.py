# Units can either be "metric", "imperial" or an empty string ""
units = input("Pick a units type, metric (cm, kgs) or imperial (in, lbs): ")

# UX Decision: We want to print out different messages based on user input, so
# if the user presses enter or inputs a unknown unit type
if units == "":
    print("Defaulting to metric (cm, kgs)")
elif units != "metric" and units != "imperial":
    print("Invalid unit type, defaulting to metric (cm, kgs)")

# Default to metric if units is different from "metric" or "imperial"
units = "metric" if units != "metric" and units != "imperial" else units

height_unit = "cm" if units == "metric" else "in"
height = float(input(f"What is your height? (in {height_unit}) "))
# If we are using metric units, the height is converted into metres
height = (height / 100) if units == "metric" else height

weight_unit = "kg" if units == "metric" else "lbs"
weight = float(input(f"What is your weight? (in {weight_unit}) "))

# The Body Mass Index, or BMI, is calculated by dividing body mass with the
# square of height (in meters, if using metric)
bmi = weight / height**2

# If we are using imperial units, multiply the result by the conversion factor
if units == "imperial":
    conversion_factor = 703
    bmi *= conversion_factor

print(f"Your BMI is {bmi}")
