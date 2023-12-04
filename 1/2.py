replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_multiple(s: str) -> str:
    for old_str, new_str in replacements.items():
        s = s.replace(old_str, old_str[0] + new_str + old_str[-1])
    return s


with open("input2.txt", "r") as file:
    total = 0
    for line in file:
        first, last = None, None
        for c in replace_multiple(line):
            if c.isdigit() and not first:
                first = c
            if c.isdigit():
                last = c

        total += int(first + last)

    print("TOTAL: ", total)
