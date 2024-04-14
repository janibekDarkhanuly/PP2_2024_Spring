import os
filepath = os.getcwd() + "\line.txt"
inp = input()
lays = inp.split()
with open(filepath,'w') as file:
    for i in lays:
        file.write(str(i) + '\n')


    
