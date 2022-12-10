from funcs import *
from diagrams import *

def main(graph):
    came_from, cost_so_far = do_algo(graph, (1, 4), (7, 8))

    draw_grid(graph, start=(1, 4), goal=(7, 8))
    print()
    draw_grid(graph, start=(1, 4), goal=(7, 8), cost=cost_so_far)
    print()

    path = get_path(came_from, start=(1, 4), goal=(7, 8))
    draw_grid(graph, start=(1, 4), goal=(7, 8), path=path)

main (graph_1)
main (graph_nopath)


import numpy as np
import matplotlib.pyplot as plt

plt.imshow(np.random.random((50,50)))
plt.colorbar()
plt.show()