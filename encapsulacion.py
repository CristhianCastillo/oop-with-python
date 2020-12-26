class CasillaDeVotacion:

    def __init__(self, identificador, regiones):
        self._identificador = identificador
        self._regiones = regiones
        self._region = None

    
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._regiones:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida para las regiones: {self._regiones}.')


if __name__ == "__main__":
    casilla = CasillaDeVotacion(1, ['Bogota', 'Medellin', 'Cartagena'])
    casilla.region = 'Medellin'
    print(casilla.region)