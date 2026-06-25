print(
"====================")
print(
"PERSONAL PROFILE")
print("====================")
print()
print()
print()

name = input("Enter your name: ")
country = input("Where are you from? ")
fav_language = input("What's your favorite language: ")
height = float(input("Your height(in m):"))


birth_year = int(input("What is your Birth year? "))
age = 2026 - birth_year

weight = float(input("How much do you weigh? "))

BMI = weight / (height * height)
BMI = round(BMI, 2)

print()
print()

print("Name:",  name)
print("Country:", country)
print("Your fav. language is:", fav_language)
print("Your height is:", str(height)+ "m")
print("Your age is:", age)
print("Your weight is: " + str(weight) + "kg")
print("Your BMI is:", BMI)

