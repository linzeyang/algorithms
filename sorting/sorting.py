# Sorting Algorithms in Python

def bubble_sort(test_list):
    for i in range(0, len(test_list)-1):
        for j in range(0, len(test_list)-1-i):
            if test_list[j] > test_list[j + 1]:
                temp = test_list[j]
                test_list[j] = test_list[j + 1]
                test_list[j + 1] = temp

    return test_list
