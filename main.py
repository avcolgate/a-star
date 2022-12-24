import matplotlib.pyplot as plt
import networkx as nx
from reader import matrix_from_file
from funcs import Graph, main

file = str(input('Enter name of file: '))

matrix = matrix_from_file(filename=file)
my_graph = Graph(matrix.width, matrix.height, matrix.walls)

all_coords = list()
main_coords = list()
wall_coords = list()
path_coords = list()

grid_dict = dict()
main_dict = dict()
wall_dict = dict()
path_dict = dict()

for i in range(0, matrix.width):
    for j in range(0, matrix.height):
        all_coords.append((i, j))
main_coords = [matrix.start, matrix.goal]
wall_coords = matrix.walls
path_coords = main(my_graph, matrix.start, matrix.goal)

for num, cord in enumerate(all_coords):
    grid_dict[num] = cord
for num, cord in enumerate(path_coords):
    path_dict[num] = cord
for num, cord in enumerate(main_coords):
    main_dict[num] = cord
for num, cord in enumerate(wall_coords):
    wall_dict[num] = cord

# print(all_coords)
# print(main_coords)
# print(path_coords)
# print(wall_coords)

fig = plt.figure(figsize =([matrix.width*0.51, matrix.height*0.51]) )

nx.draw_networkx_nodes(my_graph, all_coords, nodelist=grid_dict, node_color="tab:gray", node_shape='s', node_size=1200, alpha=0.1)
nx.draw_networkx_nodes(my_graph, wall_coords, nodelist=wall_dict, node_color="black", node_shape='s', node_size=1200, alpha=0.9)
nx.draw_networkx_nodes(my_graph, path_coords, nodelist=path_dict, node_color="orange", node_shape='s', node_size=1200, alpha=0.7)

labels = {0: 'start', 1: 'goal'}
nx.draw_networkx_nodes(my_graph, main_coords, nodelist=[0], node_color="tab:green", node_shape='o', node_size=1200, alpha=0.9)
nx.draw_networkx_nodes(my_graph, main_coords, nodelist=[1], node_color="tab:red", node_shape='o', node_size=1200, alpha=0.9)

nx.draw_networkx_labels(my_graph, main_coords, labels, font_size=14, font_color="whitesmoke", font_family="sans-serif")

plt.tight_layout()
plt.axis("off")
plt.gca().invert_yaxis()
plt.show()