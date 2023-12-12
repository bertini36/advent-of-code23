import sys
from dataclasses import dataclass
from collections import deque

filename = "input2.txt"


def build_map(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [[c for c in line if c != "\n"] for line in f]


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def get_connected_points(self, map_: list[list[str]]) -> list["Point"]:
        connected_points = []
        if self.x > 0 and map_[self.y][self.x - 1] in ("-", "L", "F", "S"):
            connected_points.append(Point(self.x - 1, self.y))
        if self.x < len(map_[0]) - 1 and map_[self.y][self.x + 1] in ("-", "J", "7", "S"):
            connected_points.append(Point(self.x + 1, self.y))
        if self.y > 0 and map_[self.y - 1][self.x] in ("|", "7", "F", "S"):
            connected_points.append(Point(self.x, self.y - 1))
        if self.y < len(map_) - 1 and map_[self.y + 1][self.x] in ("|", "J", "L", "S"):
            connected_points.append(Point(self.x, self.y + 1))
        return connected_points


def find_start(map_: list[list[str]]) -> "Point":
    for y, line in enumerate(map_):
        for x, c in enumerate(line):
            if c == "S":
                return Point(x, y)
    raise ValueError("No start found")


def get_longest_cycle(map_: list[list[str]]) -> list["Point"]:
    start = find_start(map_)
    stack = deque()
    stack.append((start, [start]))
    longest_cycle = []
    while stack:
        point, path = stack.pop()
        connected_points = point.get_connected_points(map_)
        for connected_point in connected_points:
            if connected_point == start:
                if len(path) > len(longest_cycle):
                    longest_cycle = path
            elif connected_point not in path:
                stack.append((connected_point, path + [connected_point]))
    return longest_cycle


def is_inside_of(cycle: list["Point"], point: "Point") -> bool:
    n = len(cycle)
    inside = False
    p1x, p1y = cycle[0].x, cycle[0].y
    for i in range(n + 1):
        p2x, p2y = cycle[i % n].x, cycle[i % n].y
        if min(p1y, p2y) < point.y <= max(p1y, p2y) and point.x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (point.y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or point.x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def get_limits_of(cycle: list["Point"]) -> tuple[int, int, int, int]:
    min_x = min_y = sys.maxsize
    max_x = max_y = 0
    for point in cycle:
        min_x = min(min_x, point.x)
        min_y = min(min_y, point.y)
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)
    return min_x, min_y, max_x, max_y
    

map_ = build_map(filename)
cycle = get_longest_cycle(map_)
min_x, min_y, max_x, max_y = get_limits_of(cycle)
count = 0
for y in range(len(map_)):
    for x in range(len(map_[0])):
        point = Point(x, y)
        if (
            point not in cycle
            and min_x <= point.x <= max_x
            and min_y <= point.y <= max_y
            and is_inside_of(cycle, point)
        ):
            count += 1
            
print("TOTAL: ", count)






