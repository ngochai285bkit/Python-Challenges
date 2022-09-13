# Ask for the radius and the depth of a cylinder
# And work out the total volume (circle area * depth) rounded to three decimal places

import math

radius = float(input("Enter the radius of the circle: "))
depth = float(input("Enter the depth: "))
area = math.pi * (radius**2)
volume = area * depth
print("The total volume is: " + str(round(volume, 3)))
