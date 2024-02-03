def celcius(farenheit):
    c = (5 / 9) * (farenheit - 32)
    return float(c)
f = float(input())
print(celcius(f))