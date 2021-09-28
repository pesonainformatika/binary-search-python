import random
import time


def naive_search(data: list, target: int):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


# binary search
def binary_search(data: list, target: int, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(data) - 1
    if high < low:
        return -1

    # Get Midpoint
    midpoint = (low + high) // 2
    if data[midpoint] == target:
        return midpoint
    elif target < data[midpoint]:
        new_high = midpoint - 1
        return binary_search(data, target, low, new_high)
    else:
        new_low = midpoint + 1
        return binary_search(data, target, new_low, high)


def main():
    length: int = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    target_list = [random.randint(-3 * length, 3 * length) for _ in range(length)]

    # counting naive search
    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive Search Time: {(end - start)} Seconds')

    # counting binary search
    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary Search Time: {(end - start)} Seconds')


if __name__ == '__main__':
    main()
