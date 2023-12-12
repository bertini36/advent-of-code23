filename = "input.txt"


def get_seeds() -> list[int]:
    with open(filename, "r") as f:
        return [int(seed) for seed in f.readline().split(":")[1].strip().split(" ")]


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
                return self.targets[idx] + pos
            
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
                

seed_to_soil_map = build_map("seed-to-soil")
soil_to_fertilizer_map = build_map("soil-to-fertilizer")
fertilizer_to_water_map = build_map("fertilizer-to-water")
water_to_light_map = build_map("water-to-light")
light_to_temperature_map = build_map("light-to-temperature")
temperature_to_humidity_map = build_map("temperature-to-humidity")
humidity_to_location_map = build_map("humidity-to-location")
seeds = get_seeds()

locations = []
for idx, seed in enumerate(seeds):
    soil = seed_to_soil_map.get_target(seed)
    fertilizer = soil_to_fertilizer_map.get_target(soil)
    water = fertilizer_to_water_map.get_target(fertilizer)
    light = water_to_light_map.get_target(water)
    temperature = light_to_temperature_map.get_target(light)
    humidity = temperature_to_humidity_map.get_target(temperature)
    location = humidity_to_location_map.get_target(humidity)
    locations.append(location)
    
print("RESULT", min(locations))

