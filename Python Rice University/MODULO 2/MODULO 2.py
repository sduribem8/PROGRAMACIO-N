############################################## MODULO 2 ###############################################
 
##########  FUNCTIONSSSS ################
#
"""
Demonstration of how to call functions.
"""

# Function that we can call
def useless(input1, input2, input3):
    """
    This function takes three arguments and always returns 3.
    """
    return 3

# Calling the function
useless(1, 2, 3)

# Calling the function and printing the result
print(useless(4, 5, 6))

# Calling the function and assigning the result to a variable
result = useless(7, 8, 9)
print(result)

# You must pass the right number of arguments, las siguiente funciones sin poner los argumentes necesarios, tira error.
# useless()
# useless(1)
# useless(1, 2)



############################# DEFINIR FUNCTIONSSS ###############

"""
Demonstration of defining functions.
"""

def sayhello():
    """
    Prints "hello".
    """
    print("hello")

# Call the function
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
result = double(6)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2
    prod = prod * value3
    return prod

# Call the function and assign the result to a variable
result = product(7, 13.3, -1.2)
print(result)



############ LOCAL VARIABLES #############

"""
Demonstration of parameters and variables within functions.
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Return celsius temperature that corresponds to fahrenheit
    temperature input.
    """
    offset = 32
    multiplier = 5 / 9
    celsius = (fahrenheit - offset) * multiplier
    print("inside function:", fahrenheit, offset, multiplier, celsius)
    return celsius

temperature = 95
converted = fahrenheit_to_celsius(temperature)
print("Fahrenheit temp:", temperature)
print("Celsius temp:", converted)

# Variables defined inside a function are local to that function
fahrenheit = 27
offset = 2
multiplier = 19
celsius = 77
print("before:", fahrenheit, offset, multiplier, celsius)
newtemp = fahrenheit_to_celsius(32)
print("after:", fahrenheit, offset, multiplier, celsius)
print("result:", newtemp)




########## UNDERSTANDING FUNCTION EVALUATION #################


####  La idea de esta punto es lograr y aprender a visualizar la ejecucion del programa en la mente
# PARA ESTO UTILIZAMOS LA HERRAMIENTA PYTHON TUTOR, QUE LO QUE HACE ES EJECUTAR L[INEA POR LINEA Y TIRARNOS EL RESULTADO
# DE FORMA INDIVIDUAL, DE ESTA MANERA PODEMOS VER QUE ES LO QUE HACE CADA LINEA

#######        https://pythontutor.com/           ##############

""" Define points (x0, y0) and (x1, y1) """



x_0, y_0 = 2, 2

x_1, y_1 = 5, 6



print("First point is", x_0, y_0)
print("Second point is", x_1, y_1)



####### SEGUNDO EJEMPLO PARA UTILIZAR EN PYTHON TUTOR    ###############


##### En este ejemplo lo que vemos es como la primera funcion sirve para crear las variables locales de la siguiente funcion


print(" ")
print("---------------------------------------")
print("ejemplo para incluir en el Python Tutor")
print(" ")

""" Compute the area of triangle with vertices (x0, y0), (x1, y1), and (x2, y2) """
	
def point_distance(x_0, y_0, x_1, y_1):
    """ Return distance between two points (x0,y0) and (x1,y1) """
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1
    return (x_dist ** 2 + y_dist ** 2) ** 0.5
	
	
def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    """ Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2). """	    

# Compute the lengths of the three sides.
    len_01 = point_distance(x_0, y_0, x_1, y_1)
    len_02 = point_distance(x_0, y_0, x_2, y_2)
    len_12 = point_distance(x_1, y_1, x_2, y_2)
	    
# Compute the semi-perimeter length, i.e., half of the perimeter length.
    semi_perim = (len_01 + len_02 + len_12) / 2
	    
# Compute the area according to Heron's formula.
    return (semi_perim * (semi_perim - len_01) * (semi_perim - len_02) * (semi_perim - len_12)) ** 0.5
	
	
# Compute area of triangle with vertices (10, 0), (0, 0), and (0, 10).
# Since triangle is right trianga, area should be 50.0
	
x_0, y_0 = 10, 0
x_1, y_1 = 0, 0
x_2, y_2 = 0, 10
print(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2))



###########  UTILIZACION COMANDO END = " "    ###################################

"""
Al usar end=" ", se está especificando que, en lugar de una nueva línea, 
se agregará un espacio en blanco después de la cadena que se está imprimiendo. 
Por ejemplo, el siguiente código imprimirá "Hola mundo" y luego "Hola de nuevo" 
en la misma línea, separados por un espacio
"""
#### ejemplo

print("Hola mundo", end=" ")
print("Hola de nuevo")

## el resultado sera: Hola mundo Hola de nuevo