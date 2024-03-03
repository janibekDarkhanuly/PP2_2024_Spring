import os
def create(name):
    with open(name,'w') as file:
        pass

dir = os.getcwd()
for i in range(65,91):
    xd = os.path.join(dir,f"{chr(i)} .txt")
    create(xd)
