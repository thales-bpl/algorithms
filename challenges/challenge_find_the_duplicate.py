def find_duplicate(array):
    sorted_array = bubble_sort(array)  # O(n²)
    n = len(array)
    any_dupe_number = False
    
    for i in range(n - 1): # O(n - 1)
        if type(sorted_array[i]) == str or sorted_array[i] < 0:
            break

        if sorted_array[i] == sorted_array[i + 1]:
            dupe_number = sorted_array[i]
            any_dupe_number = True

        if any_dupe_number:
            return dupe_number

    return any_dupe_number


def bubble_sort(array):  # O(n²)
    # src: https://realpython.com
    # /sorting-algorithms-python/#the-significance-of-time-complexity
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array
