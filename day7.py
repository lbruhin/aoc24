from collections import defaultdict

def is_valid(result, rest):
    if (len(rest) == 1):
        return rest[0] == result
    if is_valid(result, [rest[0] + rest[1]] + rest[2:]): return True
    if is_valid(result, [rest[0] * rest[1]] + rest[2:]): return True
    if is_valid(result, [int(str(rest[0]) + str(rest[1]))] + rest[2:]): return True
    return False


def day7_riddle1(input_file):
    with open(input_file, 'r') as file:
        data = [list(map(int, x.replace(":","").strip().split(' '))) for x in file.readlines()]

    count = 0
    for row in data:
        if (is_valid(row[0], row[1:])):
            count += row[0]
    print(count)

def day7_riddle2(input_file):
    with open(input_file, 'r') as file:
        data = [list(map(int, x.replace(":","").strip().split(' '))) for x in file.readlines()]

    count = 0
    for row in data:
        if (is_valid(row[0], row[1:])):
            count += row[0]

    print("Part 2: ", count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day7_riddle1('input_day7.txt')
    day7_riddle2('input_day7.txt')
    #day4_riddle2('input_day4.txt', masks_part2, ['MASMS', 'SAMSM', 'MASSM', 'SAMMS'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
