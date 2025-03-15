from pathlib import Path
from math import sin

def spell_data():
    cur_dir = Path.cwd()
    file = cur_dir / "harry_potter_square" / "spells.txt"
    spell_dict = {}
    with file.open("r", encoding="UTF-8") as f:
        file_data = [line.strip() for line in f.readlines()]
    for item in file_data:
        key, condition = item.strip().split(".")
        spell_dict[key] = condition.strip()
    return spell_dict

def harry_potter_square(condition):
    i = 0
    while i < len(condition):
        symbol = condition[i]
        if symbol not in ["x", "y", "+", "-", "*", "=", ">", "<", "/", "%", " ", "(", ")"]+[str(x) for x in range(10)]:
            if i < len(condition)-3 and condition[i:i+3] in ["and", "abs", "sin", "cos"]:
                i += 2
            elif i < len(condition)-2 and condition[i:i+2] in ["or"]:
                i += 1
            else:
                return None
        i += 1
    if condition:
        result = ""
        for x in range(25):
            row=""
            for y in range(25):
                if eval(condition):
                    row += "# "
                else:
                    row += ". "
            result+=row[:-1]+"\n"
        return result[:-1]


def main():
    for spell in spell_data().values():
        print(harry_potter_square(spell))
        print()

if __name__ == "__main__":
    main()