from dataclasses import dataclass
from functools import cached_property
from queue import Queue


@dataclass(frozen=True)
class Card:
    id: int
    winning_numbers: set[int]
    my_numbers: set[int]
    
    @cached_property
    def matching_numbers(self) -> set[int]:
        return self.winning_numbers.intersection(self.my_numbers)
    
    @cached_property
    def num_matching_numbers(self) -> int:
        return len(self.matching_numbers)


original_cards = []
queue = Queue()
num_cards = 0
with open("input2.txt", "r") as file:
    for idx, line in enumerate(file):
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
        card = Card(idx, winning_numbers, my_numbers)
        original_cards.append(card)
        queue.put(card)
        num_cards += 1


while not queue.empty():
    card = queue.get()
    if card.id >= len(original_cards) - 1:
        continue
        
    for card_id in range(card.id + 1, min(card.id + 1 + card.num_matching_numbers, len(original_cards))):
        queue.put(original_cards[card_id])
        num_cards += 1

print("NUM CARDS: ", num_cards)
