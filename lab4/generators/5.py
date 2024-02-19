def genn(n):
    for i in reversed(range(n+1)):
        yield i
n = int(input())
a = genn(n)
for i in a:
    print(i)