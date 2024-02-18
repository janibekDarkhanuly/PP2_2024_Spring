from datetime import datetime

t = input("Enter time: year, month, day, hour, minute, second (comma separated): ")
t = t.split(",")

x = datetime(int(t[0]), int(t[1]), int(t[2]), int(t[3]), int(t[4]), int(t[5]))
t2 = input("Enter time: year, month, day, hour, minute, second (comma separated): ")
t2 = t2.split(",")

x2 = datetime(int(t2[0]), int(t2[1]), int(t2[2]), int(t2[3]), int(t2[4]), int(t2[5]))
print(abs(x2.timestamp() - x.timestamp()))

