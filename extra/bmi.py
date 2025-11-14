units = input("Pick a units type, metric (cm, kgs) or imperial (in, lbs): ")

if units == "":
    print("Defaulting to metric (cm, kgs)")
elif units != "metric" and units != "imperial":
    print("Invalid unit type, defaulting to metric (cm, kgs)")

units = "metric" if units != "metric" and units != "imperial" else units

height_unit = "cm" if units == "metric" else "in"
height = float(input(f"What is your height? (in {height_unit}) "))
# If we are using metric units, the height is converted into metres in the formula
height = (height / 100) if units == "metric" else height

weight_unit = "kg" if units == "metric" else "lbs"
weight = float(input(f"What is your weight? (in {weight_unit}) "))

# The Body Mass Index, or BMI, is calculated by dividing body mass with the square of height
bmi = weight / height**2

# If we are using imperial units, multiply the result by the conversion factor
if units == "imperial":
    conversion_factor = 703
    bmi *= conversion_factor

print(f"Your BMI is {bmi}")
