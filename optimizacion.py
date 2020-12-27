def bag(size, weights, values, n):
    if n == 0 or size == 0:
        return 0

    if weights[n - 1] > size:
        return bag(size, weights, values, n - 1)

    result_1 = values[n - 1] + bag(size - weights[n - 1], weights, values, n - 1)
    result_2 = bag(size, weights, values, n - 1)
    
    print(f'Tomar el valor actual: {result_1}')
    print(f'No tomar el actual y validar el siguiente: {result_2}')
    return max(result_1, result_2)


if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    peso_maximo = 30
    n = len(valores)

    result = bag(peso_maximo, pesos, valores, n)
    print(result)