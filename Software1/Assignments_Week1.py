#phase 1
import math
import random

character_name = input("What is your name? ")

print("Hello, " + character_name + "!")

#phase 2

radius = float(input("Give the radius? "))
print(f"Area is {math.pi * radius ** 2:.2f}")

#phase 3

length = float(input("Give the length of a rectangle: "))
width = float(input("Give the width of a rectangle: "))
print(f"Perimeter of a rectangle is {length * 2 + width * 2: 1f}")
print(f"Area of the rectangle is {length * width :.1f}")

#phase 4

num1 = int(input("Give a integer number: "))
num2 = int(input("Give a 2nd integer number: "))
num3 = int(input("Give a 3rd integer number: "))
print(f"The sum of the 3 numbers is {num1 + num2 + num3:.0f}")
print(f"The product of numbers is {num1 * num2 * num3:.0f}")
print(f"The average of your numbers is {(num1 + num2 + num3)/3.0:.2f}")

#phase 5

print("Enter weight in medieval talents, pounds and talents")
weight_talents = float(input("Enter talents "))
weight_pounds = float(input("Enter pounds "))
weight_lots = float(input("Enter lots "))
print("The weight in modern units are: ")
weight_total_in_grams = weight_talents * 20 * 32 * 13.3 + weight_pounds * 32 * 13.3 + weight_lots * 13.3
weight_kilos = int(weight_total_in_grams/1000)
print(weight_kilos)
weight_grams_left = weight_total_in_grams - weight_kilos * 1000
print(f"The weight in modern units is: {weight_kilos} kg and {weight_grams_left: .2f} grams")

#phase 6

print(str(random.randint(0,9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))
print(str(random.randint(1,6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1,6)))






