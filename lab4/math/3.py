import math

n = int(input())
l = int(input())
p = n * l
ap = l/2 * math.tan(math.radians(180 / n))
print(round(p*ap/2))
