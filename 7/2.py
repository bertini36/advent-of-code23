from collections import defaultdict
from dataclasses import dataclass
from enum import Enum

filename = "input2.txt"


class HandType(Enum):
    REPOKER = 6
    POKER = 5
    FULL = 4
    TRIO = 3
    TWOPAIR = 2
    PAIR = 1
    NOTHING = 0


CARDS_PRIO = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


@dataclass(frozen=True)
class Hand:
    cards: list[str]
    bid: int

    def __gt__(self, other: "Hand") -> bool:
        if self.type.value > other.type.value:
            return True

        if other.type.value > self.type.value:
            return False

        i = 0
        while i < len(self.cards) and self.cards[i] == other.cards[i]:
            i += 1

        return CARDS_PRIO.index(self.cards[i]) > CARDS_PRIO.index(other.cards[i])

    def group_by_card(self) -> dict[int, int]:
        groups = defaultdict(int)
        num_jokers = 0
        for card in self.cards:
            if card == "J":
                num_jokers += 1
            else:
                groups[card] += 1
                
        if num_jokers == 5:
            groups["J"] = 5
        elif num_jokers > 0:
            card = max(groups, key=lambda k: groups[k])
            groups[card] += num_jokers
            
        return dict(groups)

    @property
    def type(self) -> "HandType":
        groups = self.group_by_card()
        if len(groups) == 1:
            return HandType.REPOKER
        if len(groups) == 2 and set(groups.values()) == {4, 1}:
            return HandType.POKER
        elif len(groups) == 2 and set(groups.values()) == {3, 2}:
            return HandType.FULL
        elif len(groups) == 3 and set(groups.values()) == {3, 1}:
            return HandType.TRIO
        elif len(groups) == 3 and set(groups.values()) == {2, 1}:
            return HandType.TWOPAIR
        elif len(groups) == 4:
            return HandType.PAIR
        return HandType.NOTHING


def get_hands() -> list[Hand]:
    with open(filename, "r") as f:
        hands = []
        for line in f.readlines():
            cards, bid = line.split(" ")
            hands.append(Hand([card for card in cards], int(bid)))
        return hands


hands = get_hands()
hands = sorted(hands)
total_winnings = 0
for idx, hand in enumerate(hands):
    rank = idx + 1
    total_winnings += hand.bid * rank

print("TOTAL: ", total_winnings)
