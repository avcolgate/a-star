from funcs import *


graph_1 = Graph(15, 15)
graph_1.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]


graph_nopath = Graph(10, 10)
graph_nopath.walls = [(5, row) for row in range(10)]
