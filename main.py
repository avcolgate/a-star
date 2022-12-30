import matplotlib.pyplot as plt
import networkx as nx
from reader import matrix_from_file
from classes import Point
from funcs import Graph, main, dict_from_list
from typing import List
import sys
import numpy as np

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
main_coords: List[Point] = list()
wall_coords: List[tuple] = list()
path_coords: List[tuple] = list()
node_color_list: List[tuple] = list()

main_coords_list: List[List[tuple]] = list()
path_coords_list: List[List[tuple]] = list()

grid_dict = dict()
main_dict = dict()
wall_dict = dict()
path_dict = dict()
main_dict_list: List[dict] = list()
path_dict_list: List[dict] = list()

for i in range(0, matrix.width):
    for j in range(0, matrix.height):
        grid_coords.append((i, j))

wall_coords = matrix.walls

for num in range(len(matrix.sources)):
    main_coords = [matrix.sources[num].coords, matrix.targets[num].coords]
    main_coords_list.append(main_coords)
    main_dict = dict_from_list(main_coords)
    main_dict_list.append(main_dict)
    del main_dict, main_coords

    path_coords = main(my_graph, matrix.sources[num].coords, matrix.targets[num].coords)
    path_coords_list.append(path_coords)
    path_dict = dict_from_list(path_coords)
    path_dict_list.append(path_dict)
    del path_dict, path_coords

    node_color_list.append((np.random.random(), np.random.random(), np.random.random()))

grid_dict = dict_from_list(grid_coords)
wall_dict = dict_from_list(wall_coords)

node_size = 1000
fig = plt.figure("A-star " + file, figsize=([matrix.width * node_size / 2150, matrix.height * node_size / 2150]))
 
nx.draw_networkx_nodes(my_graph, grid_coords, nodelist=grid_dict, node_color="tab:gray", node_shape='s',
                       node_size=node_size, alpha=0.1)
nx.draw_networkx_nodes(my_graph, wall_coords, nodelist=wall_dict, node_color="black", node_shape='s',
                       node_size=node_size, alpha=0.9)

for num in range(len(path_coords_list)):
    labels = {0: matrix.sources[num].name, 1: matrix.targets[num].name}

    nx.draw_networkx_nodes(my_graph, path_coords_list[num], nodelist=path_dict_list[num], node_color=node_color_list[num], node_shape='s',
                       node_size=node_size, alpha=0.7)
    nx.draw_networkx_nodes(my_graph, main_coords_list[num],
                       nodelist=[0], node_color="tab:green", node_shape='o', node_size=node_size * 1.5, alpha=0.9)
    nx.draw_networkx_nodes(my_graph, main_coords_list[num],
                       nodelist=[1], node_color="tab:red", node_shape='o', node_size=node_size * 1.5, alpha=0.9)
    nx.draw_networkx_labels(my_graph, main_coords_list[num], 
                       labels, font_size=13, font_color="whitesmoke", font_family="sans-serif")


if SHOW_COORDS:
    nx.draw_networkx_labels(my_graph, grid_coords, grid_dict, font_size=6, font_color="red", font_family="sans-serif", alpha=0.7)

plt.tight_layout()
plt.axis("off")
plt.gca().invert_yaxis()
plt.show()
