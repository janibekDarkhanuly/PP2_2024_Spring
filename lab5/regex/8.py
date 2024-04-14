import re

def main(s : str) -> list:
    return re.findall("[A-Z][^A-Z]*", s)

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))