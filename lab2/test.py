def myfunc(n):
    return n.upper()


txt = []
c = int(input())
for i in range(0,c):
    l = str(input())
    txt.append(l)
txt.sort(key = myfunc)
print(txt)

