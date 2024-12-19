from collections import defaultdict

def day8_riddle1(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]

    rows = len(data)
    cols = len(data[0])

    #create dict with positions for each character
    general_map = dict()
    antenna_types = defaultdict(list)
    for y, line in enumerate(data):
        for x, character in enumerate(line):
            general_map[(x,y)] = character
            if character!='.':
                antenna_types[character].append((x,y))



    antinodes = set()
    for current_type in antenna_types:

        freq = len(antenna_types[current_type])

        for i in range(0, freq-1):
            first_antenna = antenna_types[current_type][i]

            for j in range(i+1, freq):
                second_antenna = antenna_types[current_type][j]

                dx = first_antenna[0]-second_antenna[0]
                dy = first_antenna[1]-second_antenna[1]
                antinode1 = (first_antenna[0]+dx, first_antenna[1]+dy)
                antinode2 = (second_antenna[0] - dx, second_antenna[1] - dy)

                #make sure that antinode is inside grid
                if antinode1 in general_map:
                    antinodes.add(antinode1)
                if antinode2 in general_map:
                    antinodes.add(antinode2)

    print("Part 1: ", len(antinodes))

def day8_riddle2(input_file):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]

    rows = len(data)
    cols = len(data[0])
    x_bound = 0
    #create dict with positions for each character
    general_map = dict()
    antenna_types = defaultdict(list)
    for y, line in enumerate(data):
        if not x_bound:
            x_bound = len(line)
        for x, character in enumerate(line):
            general_map[(x,y)] = character
            if character!='.':
                antenna_types[character].append((x,y))



    antinodes = set()
    for current_type in antenna_types:

        freq = len(antenna_types[current_type])

        for i in range(0, freq-1):
            first_antenna = antenna_types[current_type][i]

            for j in range(i+1, freq):
                second_antenna = antenna_types[current_type][j]
                antinodes.add(first_antenna)
                antinodes.add(second_antenna)

                x1,y1 = first_antenna
                x2,y2 = second_antenna

                dx = x1-x2
                dy = y1-y2
                while x1+dx in range(0,x_bound) and y1+dy in range(0, rows): #(x1+dx, y1+dy) in general_map:
                    antinodes.add((x1+dx,y1+dy))
                    x1+=dx
                    y1+=dy
                while x2-dx in range(0,x_bound) and y2-dy in range(0, rows): #(x2-dx, y2-dy) in general_map:
                    antinodes.add((x2-dx, y2-dy))
                    x2-=dx
                    y2-=dy

    print("Part 2: ", len(antinodes))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #day8_riddle1('input_day8.txt')
    day8_riddle2('input_day8.txt')
    #day4_riddle2('input_day4.txt', masks_part2, ['MASMS', 'SAMSM', 'MASSM', 'SAMMS'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
