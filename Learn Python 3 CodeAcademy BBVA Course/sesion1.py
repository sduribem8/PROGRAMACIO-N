#se puede concatenar utilizando el signo +
#dentro del parentesis del print
my_name = "Sergio D Uribe"
print("Hellow and welcome " + my_name + "!")

#cuando se le dan valores a las variable
#si es un numero no necesita comillas
#si es un texto si necesita


message_string = "Hello there"
print(message_string)

#poner valores a las variables, estas se
#pueden cambiar a medida que avanza
#el codigo, ej:

meal = 'sandwich'

print('breackfast:')
print(meal)

meal = 'lasagna'

print('lunch:')
print(meal)

meal = 'arepa'

print('dinner:')
print(meal)



######### NUMBERS #############

#Integer son numeros enteros
#float son numeros decimales

an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5




########## CALCULOS   ###############

# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)

# Print 1700.464
print( 25 * 68 + 13 / 28)

##### variables que se le asignan numeros
#pueden ser tratadas como numeros
#pueden ser sumados, restados, multiblicados

coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)



##### EXPONENTES #############

# se usa ** debido a que no es facil en
# los teclados incluir el signo exponencial

# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)
## el resultado es 2.0 debido a que
# el programa vuelve el int un float
# para poder dividirlo



############# MODULO ###############

## UN MODULO DA COMO RESULTADO EL REMANENTE
# DE UNA DIVISION, SI EL REMANENETE ES CERO
# SE DEBE A QUE EL NUMERO ES DIVISIBLE

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

########### CONCATENATION #################

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)

## para hacer un espacio se concatena unas 
# #comillas con un espacio ej: " " 

full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)

# Para concatenar un numero toca volver el
#numero un string, esto se hace con la
#funcion str()

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is 
# possible if we turn the integer into a 
# string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

##ejemplo sergio
novia  = "Maps y "
novio = "Sergio "
meses_juntos = 3

Full_noviazgo = novia + novio + "llevan" + " " + str(meses_juntos) +  " meses juntos"

print(Full_noviazgo)

######## PLUS EQUALS ############

# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

# EJERCICIO

total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00

# Update total_price here:

total_price += nice_sweater + fun_books

## Se pueden poner igualmente los
# numeros 39.00 + 20.00 
# ejemprlo total_price += 39.00 + 20.00

print("The total price is", total_price)

######## STRING MULTILINEAA ######

# Para esta situacion toca comenzar el string 
# con tres comillas dobles """ y cerrar una 
# linea abajo con tres comillas dobles """


to_you = """
Stranger, if you passing meet me and desire to speak to me, why
should you not speak to me?
And why should I not speak to you?
"""

print(to_you)

######### EJERCICIO FINAL SESION #########

my_age = 28
half_my_age = 14
greeting = "Hola a todos, yo me llamo"
name = " sergio"
greeting_with_name = greeting + name

print(greeting_with_name + " y tengo " + str(my_age) + " anos " + "la mitad de mitad edad es " + str(half_my_age))

answer = "is this an error"