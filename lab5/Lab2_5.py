import sys


def read_file(filename):
    file = open(filename, 'r')
    lists = file.read().strip().replace('\n', ' ').split(' ')
    lists = [int(item) for item in lists]
    return lists


def filter_odd_or_even(numbers, odd):
    result = []
    if odd:
        for num in numbers:
            if num % 2 != 0:
                result.append(num)

    else:
        for num in numbers:
            if num % 2 == 0:
                result.append(num)

    return result


def reversed_bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def main():
    file_1 = sys.argv[1]
    file_2 = sys.argv[2]
    lists1 = read_file(file_1)
    lists2 = read_file(file_2)
    filtered_1 = filter_odd_or_even(lists1, True)
    filtered_2 = filter_odd_or_even(lists2, False)
    numbers = filtered_1 + filtered_2
    numbers = reversed_bubble_sort(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
