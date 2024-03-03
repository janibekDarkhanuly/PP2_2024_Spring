import os

path = input("Enter a path: ")
if os.path.exists(path):
    with os.scandir(path) as entries:
        for entry in entries:
            print(f"Entry: {entry.name}")
            print(f"Exists: {os.path.exists(entry.path)}")
            print(f"Readable: {os.access(entry.path, os.R_OK)}")
            print(f"Writable: {os.access(entry.path, os.W_OK)}")
            print(f"Executable: {os.access(entry.path, os.X_OK)}")
else:
    print("Path does not exist.")
