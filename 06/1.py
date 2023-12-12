from dataclasses import dataclass

filename = "input.txt"


def get_races() -> list["Race"]:
    with open(filename, "r") as f:
        times = [int(time) for time in f.readline().split(":")[1].strip().split(" ") if time]
        records = [int(record) for record in f.readline().split(":")[1].strip().split(" ") if record]
        return [Race(time, record) for time, record in zip(times, records)]
    
    
@dataclass(frozen=True)
class Race:
    time: int
    record: int
    
    @property
    def num_ways_to_win(self) -> int:
        num_ways_to_win = 0
        for i in range(1, self.time):
            remain_time = self.time - i
            distance = i * remain_time
            if distance > self.record:
                num_ways_to_win += 1
        return num_ways_to_win
                
              
races = get_races()
total = 1
for race in races:
    total *= race.num_ways_to_win
    
print("TOTAL: ", total)
