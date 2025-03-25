import random


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


if __name__ == "__main__":
    # Test
    for _ in range(5):
        newList = [random.randint(0, 30) for _ in range(random.randint(5, 20))]

        print()
        print(newList)
        print(merge_sort(newList))