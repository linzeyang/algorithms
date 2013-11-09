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


def get_index_of_min(lis, start_idx):
    minimum = min(lis[start_idx:])
    idx = lis[start_idx:].index(minimum) + start_idx

    return idx