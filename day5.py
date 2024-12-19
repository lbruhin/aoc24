from collections import defaultdict

def day5_riddle1(input_file):
    with open(input_file, 'r') as file:
        rules, updates = file.read().split('\n\n')

    orders = defaultdict(list)
    for order in rules.split('\n'):
        page, after = order.split('|')
        orders[int(page)].append(int(after))

    sum = 0
    correct_updates = []
    for update in updates.split('\n'):
        fullfilled = []
        update = list(map(int, update.split(',')))
        for i, page in enumerate(update):
            if set(update[i+1:]).issubset(set(orders[page])):
                fullfilled.append(True)
            else:
                fullfilled.append(False)
        if all(fullfilled):
            sum += int(update[len(update)//2])

    print('middle page sum : ', sum)

def day5_riddle2(input_file):
    with open(input_file) as file:
        lines = [line.strip() for line in file.readlines()]
        idx = lines.index("")

        is_before_rules = defaultdict(lambda: [])
        is_after_rules = defaultdict(lambda: [])

        rules = lines[:idx]
        for rule in rules:
            before, after = rule.split("|")
            is_before_rules[before].append(after)
            is_after_rules[after].append(before)

        updates = lines[idx + 1:]
        updates = [update.split(",") for update in updates]

    # find improper updates
    improper_updates = []
    for update in updates:
        okay = True
        for idx in range(len(update)):
            before, current, after = update[:idx], update[idx], update[idx + 1:]
            forwards_check = all([a in is_before_rules[current] for a in after])
            if not forwards_check:
                okay = False
                break

        if not okay:
            improper_updates.append(update)

    # re-order
    sorted_updates = []
    for improper_update in improper_updates:
        sorted_update = [improper_update[0]]
        # iterate from the right to the left, use rules specifying what is after using the current page and find the
        # last page that was properly placed in front of us, given the current ordering.
        for page in improper_update[1:]:
            insert_pos = -1
            for idx, s in enumerate(reversed(sorted_update)):
                pos = len(sorted_update) - idx - 1
                if s in is_after_rules[page]:
                    pass
                else:
                    insert_pos = pos

            if insert_pos == -1:
                sorted_update.append(page)
            else:
                # insert in-between
                sorted_update = sorted_update[:insert_pos] + [page] + sorted_update[insert_pos:]

        sorted_updates.append(sorted_update)

    # compute checksum
    middle_page_numbers = [int(improper_update[int(len(improper_update) / 2)]) for improper_update in
                           sorted_updates]
    print("Part 2: ", sum(middle_page_numbers))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day5_riddle1('input_day5.txt')
    day5_riddle2('input_day5.txt')
    #day4_riddle2('input_day4.txt', masks_part2, ['MASMS', 'SAMSM', 'MASSM', 'SAMMS'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
