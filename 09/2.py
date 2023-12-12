filename = "input2.txt"


def get_next_number(numbers: list[int]) -> int:
    if all(number == 0 for number in numbers):
        return 0

    new_numbers = [num2 - num1 for num1, num2 in zip(numbers, numbers[1:])]
    number = get_next_number(new_numbers)
    return number + numbers[-1]


lines = []   
with open(filename, "r") as f:
    for line in f:
        reversed_numbers = list(reversed([int(num) for num in line.split()]))
        lines.append(reversed_numbers)

total = sum([get_next_number(numbers) for numbers in lines])
print("TOTAL: ", total)
