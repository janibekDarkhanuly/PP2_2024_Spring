import shutil,os
def copy(src,src2):
    with open(src,'r') as source:
        with open(src2,'w') as source2:
            source2.write(source.read())
src = os.getcwd() + "\line.txt"
src2 = os.getcwd() + "\line2.txt"
copy(src,src2)