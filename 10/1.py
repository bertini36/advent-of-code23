from dataclasses import dataclass
from collections import deque

filename = "input.txt"


def build_map(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [[c for c in line if c != "\n"] for line in f]
    

@dataclass(frozen=True)
class Point:
    x: int
    y: int
    
    def get_connected_points(self, map_: list[list[str]]) -> list["Point"]:
        connected_points = []
        if self.x > 0 and map_[self.y][self.x - 1] in ("-", "L", "F"):
            connected_points.append(Point(self.x - 1, self.y))
        if self.x < len(map_[0]) - 1 and map_[self.y][self.x + 1] in ("-", "J", "7"):
            connected_points.append(Point(self.x + 1, self.y))
        if self.y > 0 and map_[self.y - 1][self.x] in ("|", "7", "F"):
            connected_points.append(Point(self.x, self.y - 1))
        if self.y < len(map_) - 1 and map_[self.y + 1][self.x] in ("|", "J", "L"):
            connected_points.append(Point(self.x, self.y + 1))
        return connected_points


def find_start(map_: list[list[str]]) -> "Point":
    for y, line in enumerate(map_):
        for x, c in enumerate(line):
            if c == "S":
                return Point(x, y)
    raise ValueError("No start found")


map_ = build_map(filename)
distances: dict["Point", int] = {}
stack = deque()
stack.append((find_start(map_), 0))
while stack:
    point, distance = stack.pop()
    distances[point] = distance
    connected_points = point.get_connected_points(map_)
    for connected_point in connected_points:
        if (
            connected_point not in distances
            or connected_point in distances and distance + 1 < distances[connected_point]
        ):
            stack.append((connected_point, distance + 1))

print("TOTAL: ", max(distances.values()))
    



