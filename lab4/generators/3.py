def genn(n):
    for i in range(0,n):
        if i%3 == 0 and i%4 == 0:
            yield i
        else:
            continue
n = int(input())
a = genn(n)
for i in a:
    print(i)