############################       EJERCICIOS MODULO 3    ###################################

########## EJERCICIO 1

"""
Template - Compute whether an integer is even.
"""

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(number) : 
    """
    Returns wether number is even.
    """
    return (number % 2 ) == 0   

###################################################
# Tests
# Student should not change this code.

number = 8
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 3
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 12
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.




print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 2")
print(" ")

####################################################### EJERCICIO 2

"""
Template - Compute whether a person is cool.
"""

###################################################
# Is cool formula
# Student should enter function on the next lines.

def is_cool(name): 
    """
    Returns wether the person with specified name is cool
    """
    return (name == "Joe") or (name == "John") or (name == "Stephen")

###################################################
# Tests
# Student should not change this code.

name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.




print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 3")
print(" ")

####################################################### EJERCICIO 3

"""
Template - Compute whether the given time is lunchtime.
"""

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.

def is_lunchtime(hour, is_am):
    return(hour == 11 and is_am) or (hour == 12 and not is_am)


###################################################
# Tests
# Student should not change this code.

def is_lunchtime_test(hour, is_am):
    """Tests the is_lunchtime function."""
    print(hour, end = "")
    if is_am:
        print("AM", end = "")
    else:
        print("PM", end = "")
    if is_lunchtime(hour, is_am):
        print(" is lunchtime.")
    else:
        print(" is not lunchtime.")

is_lunchtime_test(11, True)
is_lunchtime_test(12, True)
is_lunchtime_test(11, False)
is_lunchtime_test(12, False)
is_lunchtime_test(10, False)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 4")
print(" ")

####################################################### EJERCICIO 4

"""
Template - Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year (year) :
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))


###################################################
# Tests
# Student should not change this code.

year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
##################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.





print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 5")
print(" ")

####################################################### EJERCICIO 5

"""
Template - Compute whether two intervals intersect.
"""

###################################################
# Interval intersection formula
# Student should enter function on the next lines.

def interval_intersect (int1_lower,int1_upper,int2_lower,int2_upper) : 
    return (int2_lower <= int2_upper) and (int1_lower <= int2_upper)


###################################################
# Tests
# Student should not change this code.

int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 1, 2, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 2, 3
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 2, 3, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 3, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.


print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 6")
print(" ")

####################################################### EJERCICIO 6

"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age (name, age) :
    if age >= 0 :
      name_and_age = name + " is " + str(age) + " years old."
    else:
        name_and_age = "Error: Invalid age"
    return name_and_age 


###################################################
# Tests
# Student should not change this code.

name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", -46
print(name_and_age(name, age))



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 56 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 7")
print(" ")

####################################################### EJERCICIO 7

"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.

def print_digits(number) :
    if number >= 0 and number <= 100:
        print("The tens digit is " + str(number // 10) + ", and the ones digit is " + str(number % 10))
    else  :
        print("Error: Input is not a two-digit number.")
    
###################################################
# Tests
# Student should not change this code.
    
print_digits(42)
print_digits(99)
print_digits(5)
print_digits(459)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.
#Error: Input is not a two-digit number.


print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 8")
print(" ")

####################################################### EJERCICIO 8

"""
Template - Compute instructor's last name, given the first name.
"""

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name) : 
    if first_name == "Joe":
        return "Warren"
    if first_name == "Scott":
        return "Rixner"
    if first_name == "John":
        return "Greiner"
    if first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"


###################################################
# Tests
# Student should not change this code. 
    
first_name = "Joe"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Scott"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "John"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Stephen"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Mary"
print(first_name + "'s last name is", name_lookup(first_name))
      

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe's last name is Warren
#Scott's last name is Rixner
#John's last name is Greiner
#Stephen's last name is Wong
#Mary's last name is Error: Not an instructor

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 9")
print(" ")

####################################################### EJERCICIO 9

"""
Template - Compute a (simplified) Pig Latin version of a word.
"""

###################################################
# Pig Latin function
def pig_latin(word):
    """
    Returns the (simplified) Pig Latin version of the word.
    """

    # Partial code for body
    first_letter = word[0]
    rest_of_word = word[1 : ]

    # Student should complete function on the next lines
    if (first_letter == "a" or first_letter == "e" or first_letter == "i," or first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"
    

###################################################
# Tests
# Student should not change this code.
    
word = "pig"
print(pig_latin(word))

word = "owl"
print(pig_latin(word))

word = "python"
print(pig_latin(word))

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay

print(" ")
print("---------------------------------------")
print(" ")
print("ejercicio 10")
print(" ")

####################################################### EJERCICIO 10

"""
Template - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(coeff_a, coeff_b, coeff_c):
    discri = (coeff_b**2) - (4 * coeff_a * coeff_c)
    if discri >= 0:
        quadra1 = (-coeff_b + (discri)**0.5) / (2 * coeff_a)
        quadra2 = (-coeff_b - (discri)**0.5) / (2 * coeff_a)
        return min(quadra1, quadra2)
    if discri < 0:
        return "Error: No real solutions"


###################################################
# Tests
# Student should not change this code.

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None