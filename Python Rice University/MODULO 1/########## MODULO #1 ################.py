########## MODULO #1 ################

print("Hello World!")


############################################ NUMBERSSSSS ####################################################

"""
Demonstration of numbers in Python
"""

# Python has an integer type called int
print("int")
print("---")
print(0)
print(1)
print(-3)
print(70383028364830)

print("")

# Python has a real number type called float
#es diferente un 0 a un 0.0, el primero es un int el segundo un float
print("float")
print("-----")
print(0.0)
print(7.35)
print(-43.2)

print("")

# Limited precision  
# no muestra todos los numeros, los simplifica debido a la extension del numero hace una aproximacion.
print("Precision")
print("---------")
print(4.56372883832331773)
print(1.23456789012345678)

print("")

# Scientific/exponential notation
print("Scientific notation")
print("-------------------")
print(5e32)
print(999999999999999999999999999999999999999.9)

print("")

# Infinity
print("Infinity")
print("--------")
print(1e500)
print(-1e500)

print("")

# Conversions
print("Conversions between numeric types")
print("---------------------------------")
print(float(3))
print(float(99999999999999999999999999999999999999))
print(int(3.0))
print(int(3.7)) ##### no aproxima para arriba..... simplemente quita la parte decimal 
print(int(-3.7))

############################################ SIMPLE EXPRESSIONS ####################################################

"""
Demonstration of simple arithmetic expressions in Python
"""
print("")

print("-------------EXPRESIONES SIMPLES---------------")

print("")


# Unary + and -
print("Unary operators")
print(+3)
print(-5)
print(+7.86)
print(-3348.63)

print("")

# Simple arithmetic
print("Addition and Subtraction")
print(1 + 2)
print(48 - 89)
print(3.45 + 2.7)
print(87.3384 - 12.35)
print(3 + 6.7)
print(9.8 - 4)

print("")

print("Multiplication")
print(3 * 2)
print(7.8 * 27.54)
print(7 * 8.2)

print("")

print("Division")
print(8 / 2)
print(3 / 2)
print(7.538 / 14.3)
# Escribirlo de la siguiente forma lo que hace es que te arroje un resultado entero (integer)
print(8 // 2)
print(3 // 2)
# Al dividir floats o que ocurre es que primero saca el resutlado, despues lo vuelve integer y le quita los decimales 
# y despues lo vuelve a poner como un float
print(7.538 // 14.3)

print("")

print("Exponentiation")
print(3 ** 2)
print(5 ** 4)
print(32.6 ** 7)
print(9 ** 0.5)

############################################ COMPOUND EXPRESSIONS ####################################################

"""
Demonstration of compound arithmetic expressions in Python
"""

print("")

print("-------------COMPOUND EXPRESSIONS---------------")

print("")

# Expressions can include multiple operations
print("Compound expressions")
print(3 + 5 + 7 + 27)
print(18 - 6 + 4)

print("")

# Operator precedence defines how expressions are evaluated
# importancia primero exponenciales, despu[es division multiplicacion residuo y demmas y de ultimo esta el + y -
print("Operator precedence")
print(7 + 3 * 5)
print(5.5 * 6 // 2 + 8)
print(-3 ** 2)

print("")

# Use parentheses to change evaluation order
print("Grouping with parentheses")
print((7 + 3) * 5)
print(5.5 * ((6 // 2) + 8))
print((-3) ** 2)

############################################ VARIABLES AND ASSIGNMENT ####################################################

"""
Demonstration of the use of variables and how to assign values to
them.
"""

print("")

print("-------------VARIABLES AND ASSIGNMENT---------------")

print("")

# The = operator can be used to assign values to variables
bakers_dozen = 12 + 1
temperature = 93

# Variables can be used as values and in expressions
print(temperature, bakers_dozen)
print("celsius:", (temperature - 32) * 5 / 9)
print("fahrenheit:", float(temperature))

# You can assign a different value to an existing variable
temperature = 26
print("new value:", temperature)

# Multiple variables can be used in arbitrary expressions
offset = 32
multiplier = 5.0 / 9.0
celsius = (temperature - offset) * multiplier
print("celsius value:", celsius)