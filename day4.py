import re

masks_part1 = [
    [[0, 0], [1, 0], [2, 0], [3, 0]], # horizontal
    [[0, 0], [0, 1], [0, 2], [0, 3]], # vertical
    [[0, 0], [1, 1], [2, 2], [3, 3]], # diagonal
    [[0, 3], [1, 2], [2, 1], [3, 0]], # other diagonal
]

masks_part2 = [
    [[0,0], [1, 1],[2, 2], [0, 2], [2, 0]]
]

def day4_riddle1(input_file, masks, target):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]

    wordcount = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for mask in masks:
                try:
                    word = ''.join([data[y + dy][x + dx] for dx,dy in mask])

                    if word in target:
                        wordcount += 1

                except:
                    pass

    print('wordcount number 1 : ', wordcount)

def day4_riddle2(input_file, masks, target):
    with open(input_file, 'r') as file:
        data = [line.strip() for line in file]

    wordcount = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for mask in masks:
                try:
                    word = ''.join([data[y + dy][x + dx] for dx, dy in mask])

                    if word in target:
                        wordcount += 1

                except:
                    pass

    print('wordcount number 2 : ', wordcount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4_riddle1('input_day4.txt', masks_part1, ['XMAS', 'SAMX'])
    day4_riddle2('input_day4.txt', masks_part2, ['MASMS', 'SAMSM', 'MASSM', 'SAMMS'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
