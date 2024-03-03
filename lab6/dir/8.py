import os
path = input()
os.chmod(path,0o222)
if os.path.exists(path):
    if os.access(path,os.R_OK) and os.access(path,os.W_OK) and os.access(path,os.X_OK):
        os.remove(path)
    else:
        print("file not accessible")
else:
    print("path does not exist")
