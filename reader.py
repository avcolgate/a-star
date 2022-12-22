from classes import Matrix


def read_from_file(filename : str) -> Matrix:
    start = goal = wall = tuple()
    wall_list = list()

    with open(file='src/' + filename + '.txt', mode='rt') as file:
        lines = file.read().split('\n')
        file.close()

        size = int(lines[0])
        for line_num, line in enumerate(lines):
            if 'start' in line:
                x, y = line.replace('start', '').split()
                x, y = int(x), int(y)
                if x > (size-1) or y > (size-1):
                    print('fatal: incorrect start coordinates (line {})'.format(line_num+1))
                    exit()
                start = (x, y)

            if 'goal' in line:
                x, y = line.replace('goal', '').split()
                x, y = int(x), int(y)
                if x > (size-1) or y > (size-1):
                    print('fatal: incorrect goal coordinates (line {})'.format(line_num+1))
                    exit()
                goal = (x, y)

            if 'wall' in line:
                x, y = line.replace('wall', '').split()
                x, y = int(x), int(y)
                if x > (size-1) or y > (size-1):
                    print('fatal: incorrect wall coordinates (line {})'.format(line_num+1))
                    exit()
                wall = (x, y)
                wall_list.append(wall)

            matrix = Matrix(size=size, start=start, goal=goal, walls=wall_list)

    return matrix