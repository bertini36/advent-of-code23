from dataclasses import dataclass

filename = "input2.txt"


def get_race() -> "Race":
    with open(filename, "r") as f:
        time = int(f.readline().split(":")[1].replace(" ", ""))
        record = int(f.readline().split(":")[1].replace(" ", ""))
        return Race(time, record)


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


race = get_race()
print("TOTAL: ", race.num_ways_to_win)
