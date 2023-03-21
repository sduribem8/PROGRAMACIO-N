######################################## EJERCICIOS      ##################################

######################################### PARTE 1 #########################################

####################### EJERCICIO 1

"""
Template - Compute the number of feet corresponding to a number of miles.
"""

###################################################
# Miles to feet conversion formula
# Student should enter statement on the next line.

Feet_In_Miles = 5280
miles = 13
Total_feets = Feet_In_Miles * miles

print(Total_feets)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#68640

######################### EJERCICIO 2

"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
###### Write a Python statement that calculates and prints the number of seconds in 7 hours, 21 minutes and 37 seconds
# Student should enter statement on the next line.

seconds_inMinutes = 60
seconds_inHours = 60 * 60

number_of_hours = 7
numer_of_minutes = 21

print(number_of_hours * seconds_inHours + numer_of_minutes * seconds_inMinutes + 37)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497

################### EJERCICIO 3

"""
Template - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Rectangle perimeter formula
# Student should enter statement on the next line.

print(4 * 2 + 7*2)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#22

################### EJERCICIO 4

"""
Template - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula
# Student should enter statement on the next line.

print(4 * 7)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#28

################### EJERCICIO 5

"""
Compute the circumference of a circle, given the length of its radius.
"""

###################################################
# Circle circumference formula
# Student should enter statement on the next line.

print(2 * 3.14 * 8)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#50.24

################### EJERCICIO 6

"""
Template - Compute the area of a circle, given the length of its radius.
"""

###################################################
# Circle area formula
# Student should enter statement on the next line.

print (3.14 * 8**2)
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#200.96

################### EJERCICIO 7

"""
Template - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
# Student should enter statement on the next line.

print(1000 * (1 + (0.01 * 7))**10)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729

################### EJERCICIO 8

"""
Template - Compute a name tag, given the first and last name.
"""

###################################################
# Name tag formula
# Student should enter statement on the next line.

greeding = "My name is"
name1 = " Joe"
name2 = " Warren"

full_statement = greeding + name1 + name2

print(full_statement)

greeding = "My name is"
name1 = "Joe"
name2 = "Warren"
print(greeding, name1, name2)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.

################### EJERCICIO 9

"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""
###################################################
# Name and age formula
# Student should enter statement on the next line.

name = "Joe Warren is"
age = 56
statement = "years old"

print(name, str(age), statement)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 56 years old.

################### EJERCICIO 10

"""
Template - Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula
# Student should enter statement on the next line.

# Hint: You need to use the power operation ** .

print(((2-5)**2 + (2 - 6)**2)**0.5)

#OR

x0_x1 = 2-5
y0_y1 = 2-6

print(((x0_x1)**2 + (y0_y1)**2)**0.5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0




######################################### PARTE 2 #########################################


################################################ EJERCICIO 1

# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
miles = 13
feet = miles*5280

print(str(miles) + " miles equals " + str(feet) + " feet")


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
miles = 57
feet = miles*5280

print(str(miles) + " miles equals " + str(feet) + " feet")

# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.

miles = 82.67
feet = miles*5280

print(str(miles) + " miles equals " + str(feet) + " feet")


###################################################
# Test output
# Student should not change this code.

##print(str(miles) + " miles equals " + str(feet) + " feet.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.





############################################### EJERCICIO 2

"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines using the mouse, use ctrl+k to uncomment.
# hours = 7
# minutes = 21
# seconds = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# hours = 10
# minutes = 1
# seconds = 7


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
hours = 1
minutes = 0
seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.

total_seconds = ((hours*60 + minutes) * 60 + seconds)

###################################################
# Test output
# Student should not change this code.

print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds) + " seconds.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.





############################################### EJERCICIO 3



"""
Template - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 4
# height = 7


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 7
# height = 4


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
width = 10
height = 10


###################################################
# Rectangle perimeter formula
# Student should enter formula on the next line.

perimeter = (width + height)*2


###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(perimeter) + " inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.




############################################### EJERCICIO 4

"""
Template - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 4
# height = 7


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# width = 7
# height = 4


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
width = 10
height = 10


###################################################
# Rectangle area formula
# Student should enter formula on the next line.

area = width*height

###################################################
# Test output
# Student should not change this code.

print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(area) + " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.

# Test 2 output:
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.

# Test 3 output:
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.




############################################### EJERCICIO 5


"""
Template - Compute the circumference of a circle, given the length of its radius.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
radius = 8


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# radius = 3


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
# radius = 12.9


###################################################
# Circle circumference formula
# Student should enter formula on the next line.

circumference = 2*PI*radius

###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circumference) + " inches.")


#####################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has a circumference of 50.24 inches.

# Test 2 output:
#A circle with a radius of 3 inches has a circumference of 18.84 inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has a circumference of 81.012 inches.




############################################### EJERCICIO 6


"""
Template - Compute the area of a circle, given the length of its radius.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.
PI = 3.14

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# radius = 8


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# radius = 3


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
radius = 12.9


###################################################
# Circle area formula
# Student should enter formula on the next line.

area = PI * radius**2

###################################################
# Test output
# Student should not change this code.

print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(area) + " square inches.")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A circle with a radius of 8 inches has an area of 200.96 square inches.

# Test 2 output:
#A circle with a radius of 3 inches has an area of 28.26 square inches.

# Test 3 output:
#A circle with a radius of 12.9 inches has an area of 522.5274 square inches.




############################################### EJERCICIO 7

"""
Template - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# present_value = 1000
# annual_rate = 7
# years = 10


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# present_value = 200
# annual_rate = 4
# years = 5


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
present_value = 1000
annual_rate = 3
years = 20


###################################################
# Future value formula
# Student should enter formula on the next line.

future_value = present_value * (1 + (0.01 * annual_rate))**years

###################################################
# Test output
# Student should not change this code.

print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.

# Test 2 output:
#The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.

# Test 3 output:
#The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.





############################################### EJERCICIO 8

"""
Template - Compute a name tag, given the first and last name.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# first_name = "Joe"
# last_name = "Warren"


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# first_name = "Scott"
# last_name = "Rixner"


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
first_name = "John"
last_name = "Greiner"


###################################################
# Name tag formula
# Student should enter formula on the next line.

name_tag = "My name is " + first_name + " " + last_name + "."

###################################################
# Test output
# Student should not change this code.

print(name_tag)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#My name is Joe Warren.

# Test 2 output:
#My name is Scott Rixner.

# Test 3 output:
#My name is John Greiner.



############################################### EJERCICIO 9

"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
name = "Joe Warren"
age = 56


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#name = "Scott Rixner"
#age = 40


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#name = "John Greiner"
#age = 46


###################################################
# Name and age formula
# Student should enter formula on the next line.

statement = name + " is " + str(age) + " years old."

###################################################
# Test output
# Student should not change this code.

print(statement)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#Joe Warren is 56 years old.

# Test 2 output:
#Scott Rixner is 40 years old.

# Test 3 output:
#John Greiner is 46 years old.




############################################### EJERCICIO 10


"""
Template - compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x_0 = 2
y_0 = 2
x_1 = 5
y_1 = 6


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0 = 1
#y_0 = 1
#x_1 = 2
#y_1 = 2


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#x_0 = 0
#y_0 = 0
#x_1 = 3
#y_1 = 4


###################################################
# Distance formula
# Student should enter formula on the next line.

# Hint: You need to use the power operation ** .

distance = ((x_0 - x_1)**2 + (y_0 - y_1)**2)**0.5

###################################################
# Test output
# Student should not change this code.

print("The distance from (" + str(x_0) + ", " + str(y_0) + 
      ") to (" + str(x_1) + ", " + str(y_1) + ") is " + str(distance) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#The distance from (2, 2) to (5, 6) is 5.0.

# Test 2 output:
#The distance from (1, 1) to (2, 2) is 1.41421356237.

# Test 3 output:
#The distance from (0, 0) to (3, 4) is 5.0.




############################################### EJERCICIO 11


"""
Template - Compute the area of a triangle (using Heron's formula),
       given its side lengths.
"""

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
# x_0, y_0 = 0, 0
# x_1, y_1 = 3, 4
# x_2, y_2 = 1, 1


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
# x_0, y_0 = -2, 4
# x_1, y_1 = 1, 6
# x_2, y_2 = 2, 1


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.

a = ((x_0 - x_1)**2 + (y_0 - y_1)**2) ** 0.5
b = ((x_0 - x_2)**2 + (y_0 - y_2)**2) ** 0.5
c = ((x_1 - x_2)**2 + (y_1 - y_2)**2) ** 0.5
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

###################################################
# Test output
# Student should not change this code.

print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + ")," + 
      "(" + str(x_1) + "," + str(y_1) + "), and" + 
      "(" + str(x_2) + "," + str(y_2) + ") has an area of " + str(area) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.0.