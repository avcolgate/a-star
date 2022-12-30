from classes import Matrix, Point


def matrix_from_file(filename: str) -> Matrix:
    source_list = list()
    target_list = list()
    wall_list = list()
    wall = tuple()
    width = height = -1

    with open(file='{0}'.format(filename), mode='rt') as file:
        lines = file.read().split('\n')
        file.close()

        for line_num, line in enumerate(lines):
            if 'WIDTH' in line:
                width = int(line.replace('WIDTH', '').strip())
                if width <= 0:
                    print('fatal: incorrect width value (line {})'.format(line_num + 1))
                    exit()
            if 'HEIGHT' in line:
                height = int(line.replace('HEIGHT', '').strip())
                if height <= 0:
                    print('fatal: incorrect HEIGHT value (line {})'.format(line_num + 1))
                    exit()

            if 'SOURCE' in line and width != 0 and height != 0:
                name, x, y = line.replace('SOURCE', '').split()
                name = str(name)
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect SOURCE coordinates (line {})'.format(line_num + 1))
                    exit()
                source = Point(name=name, x=x, y=y)
                source_list.append(source)

            if 'TARGET' in line and width != 0 and height != 0:
                name, x, y = line.replace('TARGET', '').split()
                name = str(name)
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect TARGET coordinates (line {})'.format(line_num + 1))
                    exit()
                target = Point(name=name, x=x, y=y)
                target_list.append(target)

            if 'WALL' in line and width != 0 and height != 0:
                x, y = line.replace('WALL', '').split()
                x, y = int(x), int(y)
                if x > (width - 1) or y > (height - 1) or x < 0 or y < 0:
                    print('fatal: incorrect wall coordinates (line {})'.format(line_num + 1))
                    exit()
                wall = (x, y)
                wall_list.append(wall)

        if width == -1 or height == -1:
            print('fatal: no size values')
            exit()
        if not source_list:
            print('fatal: no sources')
            exit()
        if not target_list:
            print('fatal: no targets')
            exit()
        if len(target_list) != len(source_list):
            print('fatal: number of sources is not equal number of targets')
            exit()

        matrix = Matrix(width=width, height=height, sources=source_list, targets=target_list, walls=wall_list)

    return matrix
