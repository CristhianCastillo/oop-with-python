import random


def line_search(_list_search, _goal):
    for element in _list_search:
        if element == _goal:
            return True
    return False


if __name__ == "__main__":
    size_list = int(input("De que tamaño sera la lista: "))
    goal = int(input("¿Que numero quieres encontrar?: "))
    
    list_numbers_random = [random.randint(0, 100) for i in range(size_list)]
    
    found = line_search(list_numbers_random, goal)
    print(f'El elemento {str(goal)} {"no esta" if not found else "esta"} en la lista')
