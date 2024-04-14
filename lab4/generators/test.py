sum = 0
total = 0

while True:
    a = input()
    if a == "":
        break
    a = a.split()
    t = int(a[0])
    sum += 1
    total += t

print(total/sum)
