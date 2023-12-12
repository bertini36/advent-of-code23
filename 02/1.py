with open("input.txt", "r") as file:
    total = 0
    for line in file:
        parts = line.split(":")
        colors = parts[1].replace(";", ",").split(",")
        colors = [color.replace(" ", "") for color in colors]

        invalid = False
        for color in colors:
            if "red" in color:
                number = color.split("red")[0]
                if int(number) > 12:
                    invalid = True
                    break
            elif "green" in color:
                number = color.split("green")[0]
                if int(number) > 13:
                    invalid = True
                    break
            elif "blue" in color:
                number = color.split("blue")[0]
                if int(number) > 14:
                    invalid = True
                    break

        if not invalid:
            total += int(parts[0].split(" ")[1])

    print("TOTAL", total)
