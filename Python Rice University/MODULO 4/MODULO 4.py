##################################### MODULO 4   ##########################################


############ PYTHON MODULES

"""
Demonstration of importing modules.
"""

# Import the math module (look in the Docs for help)
import math

# Constants
print("Math constants")
print("==============")
print(math.pi)
print(math.e)
print("")

# Functions
print("Math functions")
print("==============")
print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))
print("")

# Dir
print("Dir")
print("===")
print(dir(math))
print("")


print(math.__name__)



####################################### DATETIME MODULE

"""
Demonstration of some of the features of the datetime module.
"""

import datetime

# Create some dates
print("Creating Dates")
print("==============")

date1 = datetime.date(1999, 12, 31)
date2 = datetime.date(2000, 1, 1)
date3 = datetime.date(2016, 4, 15)
# date4 = datetime.date(2012, 8, 32)

# Today's date
today = datetime.date.today()

print(date1)
print(date2)
print(date3)

print("")

# Compare dates
print("Comparing Dates")
print("===============")

print(date1 < date2)
print(date3 <= date1)
print(date2 == date3)

print("")

# Subtracting dates
print("Subtracting Dates")
print("=================")

diff = date2 - date1
print(diff)
print(diff.days)

diff2 = date3 - date2
print(diff2)
print(diff2.days)

print("")












# ############################## PRACTICA PARA EL PROYECTO

# """"
# en el presente archivo se hace un ejemplo de un ejercicio puesto como tarea
# el objetivo es crear un programa para prepararnos a nuestro proyecto final
# """

# import random
# """
# Implementing RPSLS for Practice Project
# """

# def name_to_number(name):
#     """
#     Take string name as input (rock-Spock-paper-lizard-scissors)
#     and returns integer (0-1-2-3-4)
#     """
#     if name == "rock":
#         return 0
#     elif name == "Spock":
#         return 1
#     elif name == "paper":
#         return 2
#     elif name == "lizard":
#         return 3
#     elif name == "scissors":
#         return 4
#     else :
#         return "Error = Wrong Name Choice"
    
# print(name_to_number("rock"))		# output - 0
# print(name_to_number("Spock"))		# output - 1
# print(name_to_number("paper"))		# output - 2
# print(name_to_number("lizard"))		# output - 3
# print(name_to_number("scissors"))	# output - 4

# def number_to_name(number):
#     """
#     Take string name as input (rock-Spock-paper-lizard-scissors)
#     and returns integer (0-1-2-3-4)
#     """
#     if number == 0:
#         return "Rock"
#     elif number == 1:
#         return "Spock"
#     elif number == 2:
#         return "paper"
#     elif number == 3:
#         return "lizard"
#     elif number == 4:
#         return "scissors"
#     else :
#         return "Error = Wrong Name Choice"
    

# print(number_to_name(0))
# print(number_to_name(1))
# print(number_to_name(2))
# print(number_to_name(3))
# print(number_to_name(4))

# def rpsls(player_choice):
#     """
#     Given string player_choice, play a game of RPSLS 
#     and print results to console
#     """
#     # print a blank line to separate consecutive games
#     print()
#     # print out the message for the player's choice
#     print("Player chooses", player_choice)
#     # convert the player's choice to player_number using the function name_to_number()
#     player_number = name_to_number(player_choice)
#     # compute random guess for comp_number using random.randrange()
#     comp_number = random.randrange(5)
#     # convert comp_number to comp_choice using the function number_to_name()
#     comp_choice = number_to_name(comp_number)
#     # print out message for computer's choice
#     print("Computer chooses", comp_choice)
#     # compute difference of player_number and comp_number modulo five
#     diff = (comp_number - player_number) % 5
#     # use if/elif/else to determine winner and print winner message
#     if diff == 0:
#         print("Player and computer tie!")
#     elif (diff == 1) or (diff == 2):
#         print("Computer Wins!")
#     elif (diff == 3) or (diff == 4):
#         print("Player Wins!")


#     # test your code
# rpsls("rock")
# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")

# diff = (0 - 1) % 5

# print(1 % 5)