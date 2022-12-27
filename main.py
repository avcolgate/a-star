import matplotlib.pyplot as plt
import networkx as nx
from reader import matrix_from_file
from funcs import Graph, main, dict_from_list
from typing import List
import sys


SHOW_COORDS = False

# file = str(input('Enter name of file: '))
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    print('fatal: no input file')
    exit()

matrix = matrix_from_file(filename=file)
my_graph = Graph(matrix.width, matrix.height, matrix.walls)

grid_coords: List[tuple] = list()
main_coords: List[tuple] = list()
wall_coords: List[tuple] = list()
path_coords: List[tuple] = list()

grid_dict = dict()
main_dict = dict()
wall_dict = dict()
path_dict = dict()

for i in range(0, matrix.width):
    for j in range(0, matrix.height):
        grid_coords.append((i, j))
main_coords = [matrix.start, matrix.goal]
wall_coords = matrix.walls
path_coords = main(my_graph, matrix.start, matrix.goal)

grid_dict = dict_from_list(grid_coords)
path_dict = dict_from_list(path_coords)
main_dict = dict_from_list(main_coords)
wall_dict = dict_from_list(wall_coords)

# print(all_coords)
# print(main_coords)
# print(path_coords)
# print(wall_coords)

node_size = 1000
fig = plt.figure("A-star " + file, figsize=([matrix.width * node_size / 2150, matrix.height * node_size / 2150]))

nx.draw_networkx_nodes(my_graph, grid_coords, nodelist=grid_dict, node_color="tab:gray", node_shape='s',
                       node_size=node_size, alpha=0.1)
nx.draw_networkx_nodes(my_graph, wall_coords, nodelist=wall_dict, node_color="black", node_shape='s',
                       node_size=node_size, alpha=0.9)
nx.draw_networkx_nodes(my_graph, path_coords, nodelist=path_dict, node_color="orange", node_shape='s',
                       node_size=node_size, alpha=0.7)

labels = {0: 'start', 1: 'goal'}
nx.draw_networkx_nodes(my_graph, main_coords,
                       nodelist=[0], node_color="tab:green", node_shape='o', node_size=node_size * 2, alpha=0.9)
nx.draw_networkx_nodes(my_graph, main_coords,
                       nodelist=[1], node_color="tab:red", node_shape='o', node_size=node_size * 2, alpha=0.9)

nx.draw_networkx_labels(my_graph, main_coords, labels, font_size=16, font_color="whitesmoke", font_family="sans-serif")

if SHOW_COORDS:
    nx.draw_networkx_labels(my_graph, grid_coords, grid_dict, font_size=6, font_color="whitesmoke", font_family="sans-serif", alpha=0.7)

plt.tight_layout()
plt.axis("off")
plt.gca().invert_yaxis()
plt.show()
