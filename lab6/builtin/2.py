str = input()
low = 0
up = 0
for i in str:
    if(i.islower()):
        low = low + 1
    elif(i.isupper()):
        up = up + 1
print(low,up)
