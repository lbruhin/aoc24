def create_machine(machine, add_=0):
    output = {}
    a, b, prize = machine.splitlines()
    output['A'] = [int(item.split('+')[1]) for item in a.split(':')[1].split(', ')]
    output['B'] = [int(item.split('+')[1]) for item in b.split(':')[1].split(', ')]
    output['Prize'] = [add_ + int(item.split('=')[1]) for item in prize.split(':')[1].split(', ')]
    return output


def solve(machines):
    output = []
    for machine in machines:
        ax, ay = machine['A']
        bx, by = machine['B']
        tx, ty = machine['Prize']
        b = (ty * ax - tx * ay) // (by * ax - ay * bx)
        a = (ty * bx - tx * by) // (bx * ay - by * ax)
        if ax * a + bx * b == tx and ay * a + by * b == ty:
            output.append(3 * a + b)
    return output


def part1():
    with open('day13.txt') as file:
        machines = file.read().split('\n\n')
    machines = [create_machine(machine) for machine in machines]
    answer = 0
    for machine in machines:
        ax, ay = machine['A']
        bx, by = machine['B']
        tx, ty = machine['Prize']
        outputs = []
        for a in range(100):
            for b in range(100):
                if ax * a + bx * b == tx and ay * a + by * b == ty:
                    outputs.append(3 * a + b)
        if outputs:
            answer += min(outputs)

    print('Part 1:', answer)
    outputs = solve(machines)
    print('Part 1 solve function:', sum(outputs))


def part2():
    with open('day13.txt') as file:
        machines = file.read().split('\n\n')
    machines = [create_machine(machine, add_=10000000000000) for machine in machines]
    output = solve(machines)
    print('Part 2:', sum(output))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
