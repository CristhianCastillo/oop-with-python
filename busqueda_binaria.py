import random


def binary_search(_list_search, _goal, init, end):
        if init > end:
            return False
        pointer = (init + end) // 2 
        current_value = _list_search[pointer]
        if _goal == current_value:
            return True
        elif _goal > current_value:
            return binary_search(_list_search, _goal, pointer + 1, end)
        else:
            return binary_search(_list_search, _goal, init, pointer - 1)


if __name__ == "__main__":
    size_list = int(input("De que tamaño sera la lista: "))
    goal = int(input("¿Que numero quieres encontrar?: "))
    
    list_numbers_random = [random.randint(0, 100) for i in range(size_list)]
    list_numbers_sorted = sorted(list_numbers_random)

    found = binary_search(list_numbers_sorted, goal, 0, len(list_numbers_sorted) - 1)
    print(f'El elemento {str(goal)} {"no esta" if not found else "esta"} en la lista')
