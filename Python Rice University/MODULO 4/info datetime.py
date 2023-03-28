## se puede imprimir cada elemento por separado
import datetime

date1 = datetime.date(2016, 1, 7)

print(date1)
print(date1.year)
print(date1.month)
print(date1.day)

print()

#se pueden hacer comparaciones entre fehcas
date2 = datetime.date(2009, 4, 30)
date1 = datetime.date(2006, 3, 15)

print(date1 != date2)
print(date1 > date2)

# Se pueden sacar diferencias entre fechas y esta es arrojada en numero de dias
date1 = datetime.date(2009, 5,1)
date2 = datetime.date(2009, 6, 1)
difference = (date1 - date2) * -1

print(difference)
print(difference.days)

# No se pueden sumar fechas, pero se le puede sumar a una fecha el resultado de la diferencia entre dos fechas
# date3 = date1 + difference
# print(date2 == date3)

print()

# Se puede traer la fecha de hoy

# todays_date = datetime.date.today()

# print(todays_date)
# print(todays_date.year)
# print(todays_date.month)
# print(todays_date.day)


MIN_YEAR = datetime.date.min.year - 1
MAX_YEAR = datetime.date.max.year

print(MIN_YEAR)