import random


def bubble_sort(_list_search):
    size = len(_list_search)

    for i in range(size):
        for j in range(0, size - i - 1):
            if _list_search[j] > _list_search[j + 1]:
                _list_search[j], _list_search[j + 1] = _list_search[j + 1], _list_search[j]
    
    return _list_search


if __name__ == "__main__":
    size_list = int(input("De que tamaño sera la lista: "))
    
    list_numbers_random = [random.randint(0, 100) for i in range(size_list)]
    print(list_numbers_random)

    list_sorted = bubble_sort(list_numbers_random)
    print(f'Esta es la lista ordenada con el Algoritmo de Burbuja: {list_sorted}')
