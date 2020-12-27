import random


def merge_sort(_list_search):
    if len(_list_search) > 1:
        medium = len(_list_search) // 2
        left = _list_search[:medium]
        right = _list_search[medium:]

        print(left, "*" * 5 , right)

        # Recursive call
        merge_sort(left)
        merge_sort(right)

        # Iterations
        i = 0
        j = 0
        # List principal iterator
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                _list_search[k] = left[i]
                i += 1
            else:
                _list_search[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            _list_search[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            _list_search[k] = right[j]
            j += 1
            k += 1

    return _list_search


if __name__ == "__main__":
    size_list = int(input("De que tamaño sera la lista: "))
    
    list_numbers_random = [random.randint(0, 100) for i in range(size_list)]
    print(list_numbers_random)
    print('--' * 20)

    list_sorted = merge_sort(list_numbers_random)
    print(f'Esta es la lista ordenada con el Algoritmo de Merge Sort: {list_sorted}')
