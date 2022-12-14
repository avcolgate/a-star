from classes import *
from typing import List


def get_path(came_from: dict, start: tuple, goal: tuple) -> List[tuple]:
    current = goal
    path = []
    if goal not in came_from:  # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


def heuristic(a: tuple, b: tuple) -> int:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(graph: Graph, start: tuple, goal: tuple) -> List[dict]:
    pQueue = PriorityQueue()
    pQueue.put(start, 0)
    came_from = {}
    cost: dict[tuple, int] = {}
    came_from[start] = None
    cost[start] = 0

    while not pQueue.empty():
        current = pQueue.get()  # gets an id

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost[current] + 1
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                pQueue.put(next, priority)
                came_from[next] = current

    return came_from, cost


def main(graph: Graph, start: tuple, goal: tuple) -> List[tuple]:
    came_from, cost = a_star(graph, start, goal)
    path = get_path(came_from, start, goal)

    return path


def dict_from_list(coord_list: List[tuple]) -> dict:
    coord_dict = dict()
    for num, item in enumerate(coord_list):
        coord_dict[num] = item

    return coord_dict
