from dataclasses import dataclass
from itertools import product

filename = "input.txt"


@dataclass(frozen=True)
class Record:
    springs: list[str]
    group_sizes: list[int]
    num_damaged: int
    
    def get_num_unknown(self) -> int:
        return sum([1 for spring in self.springs if spring == "?"])
    
    def satisfies_sizes_using(self, comb: tuple[str, ...]) -> bool:
        springs = []
        num_unknown_replaced = 0
        for spring in self.springs:
            if spring == "?":
                springs.append(comb[num_unknown_replaced])
                num_unknown_replaced += 1
            else:
                springs.append(spring)

        springs2 = []
        prev = "."
        for spring in springs:
            if prev == spring == ".":
                continue
            springs2.append(spring)
            prev = spring
            
        if springs2[-1] == ".":
            springs2 = springs2[:-1]
            
        group_sizes = [len(group) for group in "".join(springs2).split(".")]
        return group_sizes == self.group_sizes
    
    
def read_records() -> list[Record]:
    records = []
    with open(filename, "r") as f:
        for line in f:
            part1, part2 = line.split(" ")
            springs = [c for c in part1]
            group_sizes = [int(size) for size in part2.split(",")]
            num_damaged = part1.count("#")
            records.append(Record(springs, group_sizes, num_damaged))
    return records


records = read_records()
total = 0
for record in records:
    num_unknown = record.get_num_unknown()
    combs = list(product(["#", "."], repeat=num_unknown))
    for comb in combs:
        if record.num_damaged + comb.count("#") != sum(record.group_sizes):
            continue
        elif record.satisfies_sizes_using(comb):
            total += 1

print("TOTAL: ", total)
