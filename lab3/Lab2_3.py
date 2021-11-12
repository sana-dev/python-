import sys


def read_lines(filename):
    file = open(filename, 'r')
    lists = file.read().split('\n')
    lists.pop()
    return lists


def parse_cars(list_of_strings):
    result = []
    for row in list_of_strings:
        name, distance = row.split(':')
        distance = int(distance)
        result.append((name, distance))
    return result


def calculate_percentage(distance, cars):
    result = []
    for row in cars:
        percentage = distance / row[1] * 100
        result.append((row[0], percentage))

    return result


def display_result(percentages):
    print('To drive the specified distance would correspond to this many\npercent of each cars specified max range.')
    for row in percentages:
        line = str(round(row[1])) + '%'
        if (row[1]) > 100:
            line = 'Distance exceeds max range (' + str(round(row[1])) + '%)'
        print(row[0].ljust(36, ' '), '--> ', line)


def main():

    arg = sys.argv[1]
    try:
        lists = read_lines(arg)
        cars = parse_cars(lists)
        distance = int(input('How far do you want to drive (kilometers)? \n'))
        percentages = calculate_percentage(distance, cars)
        display_result(percentages)
    except FileNotFoundError:
        print('An error occurred while trying to read the file.')


if __name__ == '__main__':
    main()
