#№1
import math

t = 0
s = 3

a = math.cos(t) + s
b = 6*t + s

result = math.sqrt(a**2 + 3*abs(b)) - 1 / (abs(a) + abs(b))
print(result)
