def palindrome(y):
    t = y
    x = ""
    y = list(y)
    y.reverse()
    for i in y:
        x+=i
    if t == x:
        return True
    return False
print(palindrome("cda"))
