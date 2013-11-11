# Sorting Algorithms in Python

def bubble_sort(test_list):
    for i in range(0, len(test_list)-1):
        for j in range(0, len(test_list)-1-i):
            if test_list[j] > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]

    return test_list


def insertion_sort(test_list):
    for i in range(1, len(test_list)):
        for j in range(i-1, -1, -1):
            if test_list[j] > test_list[j + 1]:
                test_list[j], test_list[j + 1] = test_list[j + 1], test_list[j]
            else:
                break

    return test_list


def selection_sort(test_list):
    for i in range(0, len(test_list)-1):
        idx_of_minimum = get_index_of_min(test_list, i)
        if idx_of_minimum != i:
            test_list[i], test_list[idx_of_minimum] = test_list[idx_of_minimum], test_list[i]

    return test_list


def merge_sort(test_list):
    length = len(test_list)

    if length < 2:
        return test_list
    else:
        middle = int(length/2)
        left_list = test_list[:middle]
        right_list = test_list[middle:]
        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        new_list = []

        idx_left = 0
        idx_right = 0

        while idx_left < len(left_list) and idx_right < len(right_list):
            if left_list[idx_left] < right_list[idx_right]:
                new_list.append(left_list[idx_left])
                idx_left += 1
            else:
                new_list.append(right_list[idx_right])
                idx_right += 1

        if idx_left == len(left_list):
            new_list += right_list[idx_right:]
        else:
            new_list += left_list[idx_left:]

        return new_list


def get_index_of_min(lis, start_idx):
    minimum = min(lis[start_idx:])
    idx = lis[start_idx:].index(minimum) + start_idx

    return idx