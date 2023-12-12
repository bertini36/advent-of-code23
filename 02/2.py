with open("input2.txt", "r") as file:
    total = 0
    for line in file:
        colors = line.split(":")[1].replace(";", ",").split(",")
        colors = [color.replace(" ", "") for color in colors]

        max_red, max_green, max_blue = 0, 0, 0
        for color in colors:
            if "red" in color:
                number = int(color.split("red")[0])
                if number > max_red:
                    max_red = number
            elif "green" in color:
                number = int(color.split("green")[0])
                if number > max_green:
                    max_green = number
            elif "blue" in color:
                number = int(color.split("blue")[0])
                if number > max_blue:
                    max_blue = number

        total += max_red * max_green * max_blue

    print("TOTAL", total)
