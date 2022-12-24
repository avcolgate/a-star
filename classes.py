import heapq


class Matrix():
    def __init__(self, width = 0, height = 0, start = (), goal = (), walls = []) -> None:
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.walls = walls
        self.path = list()

class Graph:
    def __init__(self, width, height, wall_list):
        self.width = width
        self.height = height
        self.walls = wall_list
    
    def in_borders(self, id) -> bool: # is inside graph
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def not_wall(self, id) -> bool: # is not in wall
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
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item, priority): # puts a (priority, id) in queue
        heapq.heappush(self.elements, (priority, item)) 
    
    def get(self): # gets an id of the element 
        return heapq.heappop(self.elements)[1]