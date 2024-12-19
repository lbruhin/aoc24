
# tail call recursion with memoization
memorized_stone_counts = {}


def stone_count(number, blink_count):
    """
    Idea: Perform a depth search with memoization
    :param number:
    :param blink_count:
    :return:
    """
    if (number, blink_count) in memorized_stone_counts:
        return memorized_stone_counts[(number, blink_count)]

    # base case: initially, the list of one element has length 1
    if blink_count == 0:
        return 1

    if number == 0:
        stones = stone_count(1, blink_count - 1)

    elif len(str(number)) % 2 == 0:
        sn = str(number)
        left_number, right_number = [int(sn[:int(len(sn) / 2)]), int(sn[int(len(sn) / 2):])]
        stones = stone_count(left_number, blink_count - 1) + stone_count(right_number, blink_count - 1)
    else:
        stones = stone_count(number * 2024, blink_count - 1)

    # update list for speeding up the recursion
    memorized_stone_counts[(number, blink_count)] = stones

    return stones


def run_part1():
    numbers = "0 89741 316108 7641 756 9 7832357 91"
    numbers = [int(number) for number in numbers.split()]

    stones = sum([stone_count(number, 25) for number in numbers])
    print("Part 1:", stones)

    stones = sum([stone_count(number, 75) for number in numbers])
    print("Part 2:", stones)


def main():
    run_part1()


if __name__ == "__main__":
    main()
