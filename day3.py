import re
def day3_riddle1(input_file):
    data = open(input_file).read().replace('\n', '')
    rule = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    result = re.findall(rule, data)
    number = 0
    for mul in result:
        number += int(mul[0])*int(mul[1])
    print('multiplication number: ', number)

def day3_riddle2(input_file):
    data = open(input_file).read().replace('\n', '')
    dos = data.split("do()")
    rule = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    number = 0
    for do in dos:
        subdo = do.split("don't()")
        result = re.findall(rule, subdo[0])
        for mul in result:
            number += int(mul[0]) * int(mul[1])

    print('multiplication do number: ', number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day3_riddle1('input_day3.txt')
    day3_riddle2('input_day3.txt')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
