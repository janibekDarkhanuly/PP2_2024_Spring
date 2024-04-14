import re

def main(s : str):
    subRE = r"a.*b$"

    if re.match(subRE, s):
        return "Match Found"
    else:
        return "Not Found"

with open('row.txt', 'r', encoding='utf8') as f:
    txt = f.read()

print(main(txt))