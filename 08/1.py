filename = "input.txt"


def get_input_and_network() -> tuple[list[int], dict[str, tuple[str]]]:
    with open(filename) as f:
        chars = [char for char in f.readline() if char != "\n"]
        input = [0 if char == "L" else 1 for char in chars]
        network = {}
        for line in f:
            if "=" in line:
                parts = line.split("=")
                source = parts[0].strip()
                dests = (
                    parts[1]
                    .replace("(", "")
                    .replace(")", "")
                    .replace(" ", "")
                    .strip()
                    .split(",")
                )
                network[source] = tuple(dests)

    return input, network


input, network = get_input_and_network()
num_steps = 1
point = "AAA"
command = input[num_steps-1]
dest = network[point][command]

while dest != "ZZZ":
    num_steps += 1
    point = dest
    command = input[(num_steps-1) % len(input)]
    dest = network[point][command]


print("TOTAL: ", num_steps)
