class Lugar:
    def __init__(self,  nombre: str, fundacion: str):


        self.nombre = nombre
        self.fundacion = fundacion

    def __str__(self):
        return f" Nombre: {self.nombre},Fundacion : {self.fundacion}"