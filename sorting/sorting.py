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