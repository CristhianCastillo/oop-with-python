import random


def insertion_sort(_list_search):
    size = len(_list_search)

    for i in range(size):
        less_value = _list_search[i]
        current_position_change = i
        
        for j in range(i + 1, size):
            if less_value > _list_search[j]:
                current_position_change = j
                less_value = _list_search[j]
        
        _list_search[i], _list_search[current_position_change] = _list_search[current_position_change], _list_search[i]

    return _list_search


if __name__ == "__main__":
    size_list = int(input("De que tamaño sera la lista: "))
    
    list_numbers_random = [random.randint(0, 100) for i in range(size_list)]
    print(list_numbers_random)

    list_sorted = insertion_sort(list_numbers_random)
    print(f'Esta es la lista ordenada con el Algoritmo de Inserción: {list_sorted}')
