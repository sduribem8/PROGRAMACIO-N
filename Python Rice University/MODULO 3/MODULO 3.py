############################################# MODULO 2 ####################################################



#######################   BOOLEAN LOGIC

#### todo tiene que ser TRUE (T) or FALSE (F)
#### tiene 3 operadores NOT, OR, AND, que se comporta como la contraparte y todas las posibilidades de una variable

print(" BOOLEAN LOGIC")
print("------------------------")
print(" ")

"""
Demonstration of logical expressions.
"""

# Boolean values are True and False
value1 = True
value2 = False
print(value1, value2)

print("")

# Logical NOT
#imprime lo que no es la variable introducida
print("Logical NOT")
print("===========")
print(not value1)
print(not value2)

print("")

# Logical AND
#solo dara como true cuando ambas variables lo sean, dos false dan false asi sean iguales porque no son true]

print("Logical AND")
print("===========")
print(value1 and value1)
print(value1 and value2)
print(value2 and value2)

print("")

# Logical OR
# ACA MUESTRA TRUE SI ALGUNO DE LOS DOS ES POR LO MENOS TRUE, NO LOS DOS NECESARIAMENTE

print("Logical OR")
print("==========")
print(value1 or value1)
print(value1 or value2)
print(value2 or value2)

print("")

value3 = True
value4 = True

print(value2 or ((value1 and value4) or value3))

print(" ")




################################## ARITHMETIC COMPARISONS   #######################################


"""
Demonstration of arithmetic comparisons
"""

# Six different arithmetic comparison operators
print("Comparisons")
print("===========")
print(7 > 3) # es mayor que 3?
print(7 < 3) # es menor que 3?
print(7 >= 3) # es mayor o igual que 3?
print(7 <= 3) # es menor o igual que 3?
print(7 == 3) # es igual a 3?
print(7 != 3) # es distinto a 3?

print("")

# Using comparisons to get a boolean value
print("Comparing Variables")
print("===================")
num1 = 7.3
num2 = 8.6

greater = num1 > num2
print(greater)

print("")

# == and != are also useful for non-numeric types
print("Comparing Strings")
print("=================")
name = 'Scott'

# Beware of = and == confusion!
# un = es para asignar, dos == es para comparar

equal1 = name == "Joe"
equal2 = name != "Joe"
print(equal1)
print(equal2)

print("")
print("Comparing Boolean expressions")
print("=================")

print(greater or equal1)
print(greater or equal2)


print(" ")




################################## CONDITIONALS   #######################################

"""
Demonstration of if statements.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend and give them
    $20 if you have enough money.
    """
    if friend:
        print("Hi!")

    if money > 20:
        money = money - 20

    return money


money = 100

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()



print(" ")

################################## MORE CONDITIONALS   #######################################

### ELSE y ELIF

"""
Demonstration of else and elif.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend.  Give them
    $20 if they are your friend and you have enough money.  Steal
    $10 from them if they are not your friend.
    """
    if friend and (money > 20):
        print("Hi!")
        money = money - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        money = money + 10
    return money


money = 15

money = greet(True, money)
print("Money:", money)
print()

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()


####################### ARITHMETIC COMPARISONS IN CONDITIONALS

# if (value > -10) and (value < 10):
#     # do something
# elif (value <= -10):
#     # do something different
# elif (value >= 10):
#     # do another different thing

"""
This program has three possible paths, depending on the value of the variable 
value.  If it is between -10 and 10 (but not exactly -10 or 10), then the body on 
line 2 will be executed. If, instead, it is less than or equal to -10, the body on line 
4 will be executed. Finally, if it is greater than or equal to 10, the body on line 6 
will be executed.  No else clause is necessary here, since all possibilities have been 
covered.  Note, however, that the final elif clause could be replaced with an else 
clause, since if the code gets to that point, value must be greater than or equal to 10.
"""
