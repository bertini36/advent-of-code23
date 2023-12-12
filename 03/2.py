from collections import defaultdict
from functools import reduce

with open("input2.txt", "r") as file:
    grid = defaultdict(list)
    for idy, line in enumerate(file):
        grid[idy] = list(line.strip())
        
        
def get_number_from(row: list[str], initial_idx: int) -> int:
    number = row[initial_idx]
    
    idx = initial_idx - 1
    while idx >= 0 and row[idx].isdigit():
        number = row[idx] + number
        idx -= 1
        
    idx = initial_idx + 1
    while idx < len(row) and row[idx].isdigit():
        number += row[idx]
        idx += 1
        
    return int(number)
        
        
total = 0
for idy, chars in grid.items():
    for idx, char in enumerate(chars):
        if char != "*":
            continue
            
        numbers = set()
        if idx > 0 and grid[idy][idx - 1].isdigit():
            numbers.add(get_number_from(grid[idy], idx - 1))
        if idx < len(chars) - 1 and grid[idy][idx + 1].isdigit():
            numbers.add(get_number_from(grid[idy], idx + 1))
        if idy - 1 >= 0 and grid[idy-1][idx].isdigit():
            numbers.add(get_number_from(grid[idy-1], idx))
        if idy + 1 < len(grid) and grid[idy+1][idx].isdigit():
            numbers.add(get_number_from(grid[idy+1], idx))
        if idx > 0 and idy - 1 >= 0 and grid[idy-1][idx - 1].isdigit():
            numbers.add(get_number_from(grid[idy-1], idx - 1))
        if idx < len(chars) - 1 and idy - 1 >= 0 and grid[idy-1][idx + 1].isdigit():
            numbers.add(get_number_from(grid[idy-1], idx + 1))
        if idx > 0 and idy + 1 < len(grid) and grid[idy+1][idx - 1].isdigit():
            numbers.add(get_number_from(grid[idy+1], idx - 1))
        if idx < len(chars) - 1 and idy + 1 < len(grid) and grid[idy+1][idx + 1].isdigit():
            numbers.add(get_number_from(grid[idy+1], idx + 1))

        if len(numbers) == 2:
            total += reduce(lambda x, y: x * y, numbers)
        
print("TOTAL", total)
            
