class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


    def avanzar(self):
        print('Esta caminando...')


class Ciclista(Persona):


    def __init__(self, nombre):
        super().__init__(nombre)


    def avanzar(self):
        print('Esta pedaleando...')


def main():
    persona = Persona("Cristhian")
    persona.avanzar()

    ciclista = Ciclista("Eduardo")
    ciclista.avanzar()

if __name__ == "__main__":
    main()