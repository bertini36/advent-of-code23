import math

filename = "input2.txt"


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


def get_starting_and_ending_points(network: dict[str, tuple[str]]) -> tuple[set[str], set[str]]:
    starting_points = set()
    ending_points = set()
    for point in network.keys():
        if point.endswith("A"):
            starting_points.add(point)
        elif point.endswith("Z"):
            ending_points.add(point)

    return starting_points, ending_points


input, network = get_input_and_network()
starting_points, ending_points = get_starting_and_ending_points(network)
distances_from = {}

for point in starting_points:
    num_steps = 1
    command = input[num_steps-1]
    dest = network[point][command]
    while dest not in ending_points:
        num_steps += 1
        command = input[(num_steps-1) % len(input)]
        dest = network[dest][command]
    distances_from[point] = num_steps
    

min_steps = math.lcm(*distances_from.values())
print("TOTAL: ", min_steps)
