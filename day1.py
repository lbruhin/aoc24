
def extract_lists(input_file):
    A = []
    B = []
    with open(input_file, 'r') as file:
        # Read each line in the file
        for line in file:
            a, b = line.split()
            A.append(int(a))
            B.append(int(b))
    return A,B
def day1_riddle1(input_file):
    list1, list2 = extract_lists(input_file)
    distance = sum([abs(a-b) for a,b in zip(sorted(list1), sorted(list2))])
    print("total distance: ", distance)

def day1_riddle2(input_file):
    A,B=extract_lists(input_file)
    similarity_score = 0
    for i in A:
        similarity_score += i*B.count(i)

    print("similarity score: ", similarity_score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1_riddle1('input.txt')
    day1_riddle2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
