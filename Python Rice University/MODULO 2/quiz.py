
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)


###

def f(x) :
    solve = -5 * x**5 + 67 * x**2 -47
    return solve

print(f(0))
print(f(1))
print(f(2))
print(f(3))

#######

def future_value(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    value = present_value * (1 + rate_per_period)**periods
    return value


print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))

lado = 5
area = lado**2 * 3**0.5 / 4
print(area)