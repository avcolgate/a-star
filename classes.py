class Matrix():
    def __init__(self, size = 0, start = (), goal = (), walls = []) -> None:
        self.size = size
        self.start = start
        self.goal = goal
        self.walls = walls
        self.path = list()
