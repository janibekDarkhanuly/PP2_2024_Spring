def genn(n):
    for i in range(1,n+1):
        yield i*i
n = int(input())
a = genn(n)
for i in a:
    print(i)

