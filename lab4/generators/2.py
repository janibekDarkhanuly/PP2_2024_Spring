def genn(n):
    for i in range(0,n+1):
        if i%2 == 0:
            yield i
        else:
            continue
n = int(input())
a = genn(n)
list = []
for i in a:
    list.append(str(i))
print(",".join(list))
