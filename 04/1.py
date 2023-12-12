points = 0
with open("input.txt", "r") as file:
    for line in file:
        card_numbers = line.split(":")[1]
        winning_numbers = {
            int(number) 
            for number in card_numbers.split("|")[0].strip().split(" ")
            if number
        }
        my_numbers = {
            int(number) 
            for number in card_numbers.split("|")[1].strip().split(" ")
            if number
        }

        num_matching_numbers = len(winning_numbers.intersection(my_numbers))
        if num_matching_numbers == 0:
            continue

        points += 2 ** (num_matching_numbers - 1)
        
print("POINTS: ", points)
        
        
        
