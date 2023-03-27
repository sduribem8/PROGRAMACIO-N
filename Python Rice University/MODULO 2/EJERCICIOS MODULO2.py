############################       EJERCICIOS MODULO 2    ###################################

########## EJERCICIO 1

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 1")
print(" ")

"""
Template - Compute the number of feet corresponding to a number of miles.
"""

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.

def miles_to_feet(miles) :
    "devuelve el valor en pies de las millas"
    feet = miles * 5280
    return feet

###################################################
# Tests
# Student should not change this code.


miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 2")
print(" ")

################### EJERCICIO 2

"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.

def total_seconds(hours, minutes, seconds) :
    "Returns the total number of seconds for hours, minutes and seconds"
    seconds = (hours * 60 + minutes) * 60 + seconds
    return seconds

###################################################
# Tests
# Student should not change this code.

hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 3")
print(" ")

################### EJERCICIO 3

"""
Template - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.

def rectangle_perimeter(width, height) :
    "returns the perimeter of the rectangle in inches. "
    inches = 2 * (width + height)
    return inches


###################################################
# Tests
# Student should not change this code.


width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.


print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 4")
print(" ")

################### EJERCICIO 4

"""
Template - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width, height) :
    "returns the area of the rectangle in inches. "
    area = width * height
    return area


###################################################
# Tests
# Student should not change this code.

width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 5")
print(" ")

################### EJERCICIO 5

"""
Template - Compute the circumference of a circle, given the length of its radius.
"""

import math
PI = math.pi

###################################################
# Circle circumference formula
# Student should enter function on the next lines.

def circle_circumference(radius) :
    " returns the the circumference of a circle with radius in inches"
    circumference = 2 * PI * radius
    return circumference

###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
#A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
#A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 6")
print(" ")

################### EJERCICIO 6

"""
Template - Compute the area of a circle, given the length of its radius.
"""

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula
# Student should enter function on the next lines.

def circle_area(radius) :
    " returns the the area of a circle with radius in inches"
    area = PI * radius**2
    return area

###################################################
# Tests
# Student should not change this code.

radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 7")
print(" ")

################### EJERCICIO 7

"""
Template - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
# Student should enter function on the next lines.

def future_value(present_value, anual_rate, years) :
    "devuelve el valor futuro de los dolares invertidos en x cantidad de tiempo a una tasa de interes anual"
    value = present_value * ((1 + (0.01 * anual_rate))** years)
    return value


###################################################
# Tests
# Student should not change this code.


present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 8")
print(" ")

################### EJERCICIO 8

"""
Template - Compute a name tag, given the first and last name.
"""

###################################################
# Name tag formula
# Student should enter function on the next lines.

def name_tag(first_name, last_name) : 
    "returns a string of the form (My name is % %. where the percents are the strings first_name and last_name" 
    full_name = ("My name is " + first_name + " " + last_name) 
    return full_name
    
###################################################
# Tests
# Student should not change this code.
    
    
first_name, last_name = "Joe", "Warren"
print(name_tag(first_name, last_name))

first_name, last_name = "Scott", "Rixner"
print(name_tag(first_name, last_name))

first_name, last_name = "John", "Greiner"
print(name_tag(first_name, last_name))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.
#My name is Scott Rixner.
#My name is John Greiner.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 9")
print(" ")

################### EJERCICIO 9

"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age) :
    "devuelve el nombre junto a la edad"
    greetings = name +  (" is " + str(age) + " years old.")
    return greetings

###################################################
# Tests
# Student should not change this code.

    
name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", 46
print(name_and_age(name, age))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 56 years old.
#Scott Rixner is 40 years old.
#John Greiner is 46 years old.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 10")
print(" ")

################### EJERCICIO 10 y 11

"""
Template - Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .

def point_distance( x_0, y_0, x_1, y_1) :
    "en primera instancia sacaremos las distancias para sacar el perimetro y despues el area"
    dist_x = x_0 - x_1
    dist_y = y_0 - y_1
    return (dist_x**2 + dist_y**2)**0.5

def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2) : 
    "usa el resutlado de la funci[on anterior para devolver el valor del area utilizando esos valores para sacar el petimetro]"

    # definimos las variables disntancia para sacar el perimetro 
    distancia1 = point_distance(x_0, y_0, x_1, y_1)
    distancia2 = point_distance(x_0, y_0, x_2, y_2)
    distancia3 = point_distance(x_1, y_1, x_2, y_2)

    #sacamos el perimetro 
    perimetro = (distancia1 + distancia2 + distancia3)/2

    #sacamos el area
    area = (perimetro * (perimetro - distancia1) * (perimetro - distancia2) * (perimetro - distancia3))**0.5
    return area


###################################################
# Tests
# Student should not change this code.


x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 11")
print(" ")

x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The distance from (2, 2) to (5, 6) is 5.0.
#The distance from (1, 1) to (2, 2) is 1.41421356237.
#The distance from (0, 0) to (3, 4) is 5.0.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 12")
print(" ")


################### EJERCICIO 12

"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number):
    """
    Prints the tens and ones digit of an integer in [0,100).
    """
    
    print("The tens digit is " + str(number // 10) + ", and the ones digit is " + 
          str(number % 10) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.


print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 13")
print(" ")

################### EJERCICIO 13

"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    """
    Prints Powerball lottery numbers.
    """
    
    # Note that including the optional argument end = "" to print() cause
    # print to NOT generate a newline
    
    print("Today's numbers are " + str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "") 
    print(str(random.randrange(1, 60)) + ", and ", end = "")
    print(str(random.randrange(1, 60)) + ". The Powerball number is ",  end = "") 
    print(str(random.randrange(1, 36)) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.