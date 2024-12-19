def print_space(space):
    print("".join(space))


def find_last_right_most(seq):
    inv = list(seq)
    inv.reverse()
    for i in range(len(inv)):
        if inv[i] != ".":
            return len(inv) - i - 1

    return None


def calculate_checksum(space):
    sum = 0
    for idx in range(len(space)):
        if space[idx] == ".":
            continue

        sum += idx * int(space[idx])
    return sum


def extract_space(disk_map):
    space = []
    counter = 0
    for idx, digit in enumerate(list(disk_map)):
        if idx % 2 == 1:
            for _ in range(int(digit)):
                space.append(".")
        else:
            for _ in range(int(digit)):
                space.append(str(counter))
            counter += 1

    return space


def run_part1():
    with open("datasets/day9/input.txt") as file:
        disk_map = file.readlines()[0].strip()

    space = extract_space(disk_map)

    for idx in range(len(space)):
        right_idx = find_last_right_most(space)

        if right_idx < idx:
            break

        if space[idx] == ".":
            space[idx] = space[right_idx]
            space[right_idx] = "."

    chk_sum = calculate_checksum(space)
    print("Part 1:", chk_sum)


def run_part2():
    #disk_map = "2333133121414131402"
    with open("input_day9.txt") as file:
         disk_map = file.readlines()[0].strip()

    space = extract_space(disk_map)
    #print_space(space)

    def find_rr(space, end_idx):
        for i in range(end_idx):
            idx = end_idx - i
            if space[idx] != ".":
                return idx

    def find_rl(space, rr):
        id = space[rr]
        for i in range(rr):
            idx = rr - i - 1
            if space[idx] != id:
                return False, idx + 1

        return True, None

    def find_l(space, R):
        for idx in range(len(space)):
            len_counter = 0
            if space[idx] != ".":
                continue

            for jdx in range(idx, len(space)):
                if len_counter == R:
                    return idx, jdx, True

                if space[jdx] == ".":
                    len_counter += 1
                else:
                    break
        return None, None, False

    start_idx = len(space) - 1
    visited_numbers = []
    for idx in range(0, len(space)):
        rr = find_rr(space, start_idx)
        done, rl = find_rl(space, rr)

        if done:
            break

        R = (rr - rl) + 1
        ll, lr, okay = find_l(space, R)

        current_number = space[rr]
        if okay and not current_number in visited_numbers:
            L = (lr - ll)
            if L >= R and lr <= rl:
                space[ll:ll + R] = space[rl:rr + 1]
                space[rl:rr + 1] = list("." * R)
                visited_numbers.append(current_number)
                # print_space(space)

        start_idx = rl - 1

    chk_sum = calculate_checksum(space)
    print("Part 2:", chk_sum)


def main():
    # run_part1()
    run_part2()


if __name__ == "__main__":
    main()
