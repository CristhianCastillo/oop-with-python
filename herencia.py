class Rectangulo:

    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    
    def area(self):
        return self._base * self._altura


class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)



if __name__ == "__main__":
    rectangulo = Rectangulo(3, 4)
    print(f'El area del rectangulo es: {rectangulo.area()}')

    cuadrado = Cuadrado(5)
    print(f'El area del cuadrado es: {cuadrado.area()}')