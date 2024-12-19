def extract_lists(input_file):
    with open(input_file, 'r') as file:
        # Read each line in the file
        reports = [list(map(int, line.strip().split(" "))) for line in file.readlines()]

    return reports


def check_sequence_jumps(report):
    return (
            all(0 < report[i + 1] - report[i] <= 3 for i in range(len(report) - 1)) or
            all(-3 <= report[i + 1] - report[i] < 0 for i in range(len(report) - 1))
    )


def day2_riddle1(input_file):
    reports = extract_lists(input_file)
    correct_reports = sum([check_sequence_jumps(report) for report in reports])
    print("correct reports: " , correct_reports)



def day2_riddle2(input_file):
    reports = extract_lists(input_file)
    correct_reports = sum([any([check_sequence_jumps(report[:i]+report[i+1:]) for i in range(len(report))]) for report in reports])
    print("correct reports v2: ", correct_reports)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2_riddle1('input_day2.txt')
    day2_riddle2('input_day2.txt')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
