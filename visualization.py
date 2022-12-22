import matplotlib.pyplot as plt
import networkx as nx
from process import main
from reader import read_from_file
from funcs import Graph

G = nx.Graph()

file = str(input('Enter name of file: '))

matrix = read_from_file(filename=file)

my_graph = Graph(matrix.size, matrix.size, matrix.walls)

all_coords = list()
path_coords = list()
main_coords = list()
wall_coords = list()
grid_dict = dict()
path_dict = dict()
main_dict = dict()
wall_dict = dict()

for i in range(0, matrix.size):
    for j in range(0, matrix.size):
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

fig = plt.figure(figsize =([matrix.size*0.51, matrix.size*0.51]) )

nx.draw_networkx_nodes(G, all_coords, nodelist=grid_dict, node_color="tab:gray", node_shape='s', node_size=1200, alpha=0.1)
nx.draw_networkx_nodes(G, wall_coords, nodelist=wall_dict, node_color="black", node_shape='s', node_size=1200, alpha=0.9)
nx.draw_networkx_nodes(G, path_coords, nodelist=path_dict, node_color="orange", node_shape='s', node_size=1200, alpha=0.7)

labels = {0: 'start', 1: 'goal'}
nx.draw_networkx_nodes(G, main_coords, nodelist=[0], node_color="tab:green", node_shape='s', node_size=1200, alpha=0.9)
nx.draw_networkx_nodes(G, main_coords, nodelist=[1], node_color="tab:red", node_shape='s', node_size=1200, alpha=0.9)

nx.draw_networkx_labels(G, main_coords, labels, font_size=14, font_color="whitesmoke", font_family="sans-serif")


plt.tight_layout()
plt.axis("off")
plt.gca().invert_yaxis()
plt.show()
