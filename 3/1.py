from collections import defaultdict


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def has_symbol(line: list[str], positions: list[int]) -> bool:
    for idx in positions:
        if is_symbol(line[idx]):
            return True
    return False


with open("input.txt", "r") as file:
    grid = defaultdict(list)
    for idy, line in enumerate(file):
        grid[idy] = list(line.strip())


part_numbers = []
number = ""
for idy, chars in grid.items():
    for idx, char in enumerate(chars):
        if not char.isdigit() and not number:
            continue
            
        if char.isdigit():
            number += char
            continue

        has_symbol_before = is_symbol(chars[idx - len(number) - 1]) if idx - len(number) - 1 >= 0 else False
        has_symbol_after = is_symbol(char)
        number_idxs_w_offset = list(filter(lambda x: x >= 0, range(idx - len(number) - 1, idx + 1)))
        has_symbol_above = idy - 1 >= 0 and has_symbol(grid[idy - 1], number_idxs_w_offset)
        has_symbol_below = idy + 1 < len(grid) and has_symbol(grid[idy + 1], number_idxs_w_offset)

        if any([has_symbol_before, has_symbol_after, has_symbol_above, has_symbol_below]):
            part_numbers.append(int(number))
        
        number = ""

print("TOTAL", sum(part_numbers))
