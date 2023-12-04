with open("input.txt", "r") as file:
    total = 0
    for line in file:
        first, last = None, None
        for c in line:
            if c.isdigit() and not first:
                first = c
            if c.isdigit():
                last = c
        total += int(first + last)

    print("TOTAL: ", total)
