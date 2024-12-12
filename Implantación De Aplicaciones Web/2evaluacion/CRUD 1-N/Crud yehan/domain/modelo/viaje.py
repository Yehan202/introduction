from domain.modelo.lugar_iconico import Lugar

class Viaje:
    def __init__(self, cod_viaje: int, ciudad: str, coste: float, valoracion: int, transporte: str,lugar_iconico : list[Lugar]=[]):

        self.cod_viaje = cod_viaje
        self.ciudad = ciudad
        self.coste = coste
        self.valoracion = valoracion
        self.transporte = transporte
        self.lugar_iconico = lugar_iconico

    def __str__(self):
        lugar_iconico_str = ""
        for i in self.lugar_iconico:
            lugar_iconico_str += str(i) +"\n "
        return f"Ciudad: {self.ciudad}, Coste: {self.coste}, Valoración: {self.valoracion}, Transporte: {self.transporte},\nLugar_iconico :\n {lugar_iconico_str}"


