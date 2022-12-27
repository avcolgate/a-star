from classes import Matrix


def matrix_from_file(filename: str) -> Matrix:
    start = goal = wall = tuple()
    width = height = -1
    wall_list = list()

    with open(file='src/{0}'.format(filename), mode='rt') as file:
        lines = file.read().split('\n')
        file.close()

        for line_num, line in enumerate(lines):
            if 'size' in line:
                x, y = line.replace('size', '').split()
                x, y = int(x), int(y)
                if x <= 0 or y <= 0:
                    print('fatal: incorrect size values (line {})'.format(line_num + 1))
                    exit()
                width, height = x, y
            if 'start' in line and width != 0 and height != 0:
                x, y = line.replace('start', '').split()
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect start coordinates (line {})'.format(line_num + 1))
                    exit()
                start = (x, y)
            if 'goal' in line and width != 0 and height != 0:
                x, y = line.replace('goal', '').split()
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect goal coordinates (line {})'.format(line_num + 1))
                    exit()
                goal = (x, y)
            if 'wall' in line and width != 0 and height != 0:
                x, y = line.replace('wall', '').split()
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect wall coordinates (line {})'.format(line_num + 1))
                    exit()
                wall = (x, y)
                wall_list.append(wall)

        if width == -1 or height == -1:
            print('fatal: no size values')
            exit()
        if not start:
            print('fatal: no start coords')
            exit()
        if not goal:
            print('fatal: no goal coords')
            exit()

        matrix = Matrix(width=width, height=height, start=start, goal=goal, walls=wall_list)

    return matrix
