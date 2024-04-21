#№1
import math

def solve_quadratic_equation(t):
    a = t + 2
    b = 3*t
    c = -(t-3)
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return "нет корней"

# Интервал перебора чисел
for t in range(-10, 11):
    roots = solve_quadratic_equation(t)
    print(f"При t = {t}, корни уравнения:", roots)
