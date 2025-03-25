import random
import time
import matplotlib.pyplot as plt


### DEFAULT MERGE SORT ###

def merge(list1, list2):
    final_list = []

    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            final_list.append(list1[i])
            i += 1 
        else:
            final_list.append(list2[j])
            j += 1
    
    return final_list + list1[i:] + list2[j:]


def merge_sort(_list):
    list_len = len(_list)
    if list_len == 1:
        return _list
    
    sub_list_1 = merge_sort(_list[:(list_len // 2)])
    sub_list_2 = merge_sort(_list[(list_len // 2):])

    return merge(sub_list_1, sub_list_2)


### MERGE SORT WITH N PARTITIONS ###

def merge_n(arrays: list[list[int] | list[float]]):
    n = len(arrays)
    if n == 0:
        return []
    if n == 1:
        return arrays[0]

    sorted_array = []

    indexes = [0] * len(arrays)
    values = [arrays[i][0] for i in range(n)]
    array_lens = [len(array) for array in arrays]

    while True:
        min_index, min_value = min(enumerate(values), key=lambda p: p[1])
        sorted_array.append(min_value)

        new_index = indexes[min_index] + 1
        indexes[min_index] = new_index
        if new_index == array_lens[min_index]:
            break
        
        values[min_index] = arrays[min_index][new_index]

    new_arrays = [arrays[i][indexes[i]:] for i in range(n) if indexes[i] < array_lens[i]]
    sorted_array.extend(merge_n(new_arrays))

    return sorted_array


def merge_sort_n(array: list[int] | list[float], n: int = 2) -> list[int] | list[float]:    # Why are there no built-in generics with no imports in Python
    array_len = len(array)
    if array_len <= 1:
        return array

    segment_len = array_len // n
    remainder = array_len % n
    sub_arrays = []

    for i in range(min(n, array_len)):
        start_remainder_correction = min(i, remainder)
        end_remainder_correction = 1 if i < remainder else 0

        start = i * segment_len + start_remainder_correction
        end = start + segment_len + end_remainder_correction

        sub_array = array[start:end]
        sorted_sub_array = merge_sort_n(sub_array, n)
        sub_arrays.append(sorted_sub_array)
    
    return merge_n(sub_arrays)


### PROGRAM ###

if __name__ == "__main__":
    # Test
    max_n = 30
    number_count = 200000
    newList = [random.randint(0, 2*number_count) for _ in range(number_count)]
    times = []

    # Default merge sort function (binary)
    newListCopy = newList[:]
    start_time = time.time()
    merge_sort(newListCopy)
    end_time = time.time()
    default_elapsed_time = end_time - start_time
    print(f"Function MergeSort with 2 numbers (DEFAULT) executed in {default_elapsed_time:.6f} seconds.")

    # n-th merge sort
    for n in range(2, max_n):
        newListCopy = newList[:]
        start_time = time.time()
        merge_sort_n(newList, n)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function MergeSort with {n} numbers executed in {elapsed_time:.6f} seconds.")
        times.append(elapsed_time)

    # Plot the results
    plt.plot(range(2, max_n), times)
    plt.ylim(0, max(times) + 0.5)

    plt.axhline(default_elapsed_time)
    plt.annotate("DEFAULT", (max_n // 2 + 0, default_elapsed_time + 0.015))

    plt.show()
