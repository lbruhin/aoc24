def run_part1():
    with open("input_day10.txt") as file:
        map = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    start_positions = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                start_positions.append((i, j))

    print(start_positions)

    def visit(i, j, current_height, counter):
        if current_height == 9:
            counter.add((i, j))

        next_height = current_height + 1
        if 0 < i and map[i - 1][j] == next_height:
            visit(i - 1, j, next_height, counter)
        if 0 < j and map[i][j - 1] == next_height:
            visit(i, j - 1, next_height, counter)
        if i < len(map) - 1 and map[i + 1][j] == next_height:
            visit(i + 1, j, next_height, counter)
        if j < len(map[0]) - 1 and map[i][j + 1] == next_height:
            visit(i, j + 1, next_height, counter)

    list_of_counters = []
    for start_position in start_positions:
        counter = set()
        ci, cj = start_position
        visit(ci, cj, 0, counter)
        list_of_counters.append(counter)

    print(sum([len(i) for i in list_of_counters]))
def run_part2():
    with open("input_day10.txt") as file:
        map = [[int(i) for i in list(line.strip())] for line in file.readlines()]

    start_positions = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                start_positions.append((i, j))

    print(start_positions)

    def visit(i, j, current_height, counter):
        if current_height == 9:
            counter.append((i, j))

        next_height = current_height + 1
        if 0 < i and map[i - 1][j] == next_height:
            visit(i - 1, j, next_height, counter)
        if 0 < j and map[i][j - 1] == next_height:
            visit(i, j - 1, next_height, counter)
        if i < len(map) - 1 and map[i + 1][j] == next_height:
            visit(i + 1, j, next_height, counter)
        if j < len(map[0]) - 1 and map[i][j + 1] == next_height:
            visit(i, j + 1, next_height, counter)

    list_of_counters = []
    for start_position in start_positions:
        counter = []
        ci, cj = start_position
        visit(ci, cj, 0, counter)
        list_of_counters.append(counter)

    print(sum([len(i) for i in list_of_counters]))


def main():
    #run_part1()
    run_part2()


if __name__ == '__main__':
    main()
