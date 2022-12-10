import heapq

def draw_point(graph, id, start, goal, cost, path):
    r = " . "
    if id in cost:
        r = " %-2d" % cost[id]
    if id in path:
        r = " @ "
    if id == start:
        r = " A "
    if id == goal:
        r = " B "
    if id in graph.walls:
        r = "###"
        
    return r

def draw_grid(graph, start = (), goal = (), cost = {}, path = {}):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print("%s" % draw_point(graph, (x, y), start, goal, cost, path), end="")
        print()
    print("___" * graph.width)


class Graph:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_borders(self, id): # is inside graph
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def not_wall(self, id): # is not in wall
        return id not in self.walls
    
    def neighbors(self, id): # list of neighbors excluding unavailable ones
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        results = filter(self.in_borders, neighbors)
        results = filter(self.not_wall, results)
        return results


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return not self.elements
    
    def put(self, item, priority): # puts a (priority, id) in queue
        heapq.heappush(self.elements, (priority, item)) 
    
    def get(self): # gets an id of the element 
        return heapq.heappop(self.elements)[1]


def get_path(came_from, start, goal):
    current = goal
    path = []
    if goal not in came_from: # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)

def do_algo(graph, start, goal):
    pQueue = PriorityQueue()
    pQueue.put(start, 0)
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0
    
    while not pQueue.empty():
        current = pQueue.get() # gets an id
        
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
