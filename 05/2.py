import sys
from itertools import repeat
from multiprocessing import Pool, freeze_support

filename = "input2.txt"


def get_seed_ranges() -> list[range]:
    with open(filename, "r") as f:
        numbers = [int(seed) for seed in f.readline().split(":")[1].strip().split(" ")]
        pairs = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
        return [range(pair[0], pair[0] + pair[1]) for pair in pairs]


class Map:
    def __init__(self):
        self.source_ranges = []
        self.targets = []

    def add_ranges_in(self, line: str):
        numbers = [int(number) for number in line.strip().split(" ")]
        self.source_ranges.append(range(numbers[1], numbers[1] + numbers[2]))
        self.targets.append(numbers[0])

    def get_target(self, source: int) -> int:
        for idx, source_range in enumerate(self.source_ranges):
            if source in source_range:
                pos = source_range.index(source)
                target = self.targets[idx] + pos
                return target

        return source


def build_map(map_name: str) -> "Map":
    map_ = Map()
    with open(filename, "r") as file:
        map_rules_found = False
        for line in file:
            if line.startswith(map_name):
                map_rules_found = True
                continue

            if not line.strip() and map_rules_found:
                break

            if map_rules_found: 
                map_.add_ranges_in(line)
                continue

    return map_
    

def find_min_in(seed_range: range, maps: list["Map"]) -> int:
    print(f"PROCESSING RANGE {seed_range}")
    minimum = sys.maxsize
    progress_map = {25: False, 50: False, 75: False}
    for idx, seed in enumerate(seed_range):
        progress_percentage = int(idx / len(seed_range)) * 100
        if progress_percentage in progress_map and not progress_map[progress_percentage]:
            print(f"\tProgress: {progress_percentage}% of {seed_range}")
            progress_map[progress_percentage] = True
            
        number = seed
        for map_ in maps:
            number = map_.get_target(number)
        
        if number < minimum:
            minimum = number
            
    print(f"FINISHED RANGE {seed_range}")
    return minimum


def main():
    seed_ranges = get_seed_ranges()
    maps = [
        build_map("seed-to-soil"),
        build_map("soil-to-fertilizer"),
        build_map("fertilizer-to-water"),
        build_map("water-to-light"),
        build_map("light-to-temperature"),
        build_map("temperature-to-humidity"),
        build_map("humidity-to-location"),
    ]
    
    minimum = sys.maxsize
    with Pool(5) as pool:
        for range_minimum in pool.starmap(find_min_in, zip(seed_ranges, repeat(maps))):
            if range_minimum < minimum:
                minimum = range_minimum
        
    print("RESULT", minimum)


if __name__ == "__main__":
    freeze_support()
    main()
