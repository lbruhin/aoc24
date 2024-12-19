from collections import defaultdict

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}

def rotate_right(dir):
    if dir == '^':
        return '>'
    if dir == '>':
        return 'v'
    if dir == 'v':
        return '<'
    if dir == '<':
        return '^'

def find_path(data, start, dir, rows, cols, obs = None):
    x, y = start
    visited = set()
    pos_vectors = set()
    pos_vectors.add((x, y, dir))

    def is_inside(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while is_inside(x, y):
        visited.add((x, y))
        dx, dy = dirs[dir]
        new_x, new_y = x+dx, y+dy
        if is_inside(new_x, new_y) and (data[new_x][new_y]=='#' or (obs and (new_x, new_y) == obs)):
            dir = rotate_right(dir)
        else:
            x,y = new_x, new_y

        pos_vector = (x, y, dir)

        if pos_vector in pos_vectors:
            return True, visited
        pos_vectors.add(pos_vector)
    return False, visited

def day6_riddle1(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]
    rows=len(data)
    cols=len(data[0])

    for r, v in enumerate(data):
        for c, val in enumerate(v):
            if val == '^':
                start = (r, c)

    _,visited = find_path(data, start, '^', rows, cols)


    print('len visited: ', len(visited))

def day6_riddle2(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]
    rows = len(data)
    cols = len(data[0])

    for r, v in enumerate(data):
        for c, val in enumerate(v):
            if val == '^':
                start = (r, c)

    _, visited = find_path(data, start, '^', rows, cols)

    result = 0
    obstacles = visited - {start}
    for obs in obstacles:
        if find_path(data, start,'^', rows, cols, obs )[0]:
            result += 1
    print('part 2: ',result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day6_riddle1('input_day6.txt')
    day6_riddle2('input_day6.txt', )
    #day4_riddle2('input_day4.txt', masks_part2, ['MASMS', 'SAMSM', 'MASSM', 'SAMMS'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
