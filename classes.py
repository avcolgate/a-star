import heapq
from typing import List


class Point:
    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.coords = (x, y)


class Matrix:
    def __init__(self, width: int, height: int, sources: List[Point], targets: List[Point], walls: List[tuple]) -> None:
        self.width = width
        self.height = height
        self.sources = sources
        self.targets = targets
        self.walls = walls
        self.path = list()


class Graph:
    def __init__(self, width: int, height: int, wall_list: List[tuple]) -> None:
        self.width = width
        self.height = height
        self.walls = wall_list

    def in_borders(self, id: tuple) -> bool:  # is inside graph
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def not_wall(self, id: tuple) -> bool:  # is not in wall
        return id not in self.walls

    def neighbors(self, id: tuple) -> List[tuple]:  # list of neighbors excluding unavailable ones
        (x, y) = id
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        results = filter(self.in_borders, neighbors)
        results = filter(self.not_wall, results)
        return results


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = list()

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: tuple, priority: int) -> None:  # puts a (priority, id) in queue
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> None:  # gets an id of the element
        return heapq.heappop(self.elements)[1]
