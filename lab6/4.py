import os
sum = 0
filepath = os.getcwd() + "\line.txt"
with open(filepath,'r') as file:
    for i in file:
        sum  = sum + 1
print(sum)