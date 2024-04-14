import re

def main (s : str) -> str:
    listOfStrings = re.split(r"\_", s)

    return "".join([x.capitalize() for x in listOfStrings])

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))