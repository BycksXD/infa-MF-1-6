#№1

import math

x = 2
z = 1
y = 2
u = 3

result = math.pow(x, y) * math.pow(z, 2 * u) - math.exp(-(3 * u)) + math.pow(7, 2 * x)
print(result)

#№2

import math

x = 1.5
y = 1

result = math.log(math.cos(x))**2 + abs(x) - math.atan(x/(3*y))
print(result)

#№3

import math

x = 3
y = 2

result = 2*x + math.sqrt(x+4) - 0.3*math.sin(x**2) / 3 * math.sqrt(x-2)**3 * 2*x*y
print(result)
#№4

import math

x = 3

result = math.pow(x, 5) * math.pow(math.sin(x+4), 3) - 3*abs(x) / (x**2 - 3*x**3)
print(result)
