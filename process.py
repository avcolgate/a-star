from funcs import *
from diagrams import *

def main(graph, start, goal) -> list:
    came_from, cost_so_far = do_algo(graph, start, goal)

    draw_grid(graph, start, goal)
    draw_grid(graph, start, goal, cost=cost_so_far)

    path = get_path(came_from, start, goal)
    draw_grid(graph, start, goal, path=path)

    return path
