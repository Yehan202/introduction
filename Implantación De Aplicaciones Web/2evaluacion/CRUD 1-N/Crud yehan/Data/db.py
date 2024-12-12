from domain.modelo.viaje import Viaje
from domain.modelo.lugar_iconico import Lugar

viajes: list[Viaje] = [
    Viaje(1,"Londres", 2000.91, 5, "avion",[
        Lugar("Big Ben" ,"XV"),
        Lugar("london Eye", "XVI"),
        Lugar("Palacio Real","XV")]),

    Viaje(2,"Paris", 1500.34, 4, "tren",[
        Lugar("Torre Eiffel","XVII"),
        Lugar("Museo del louvre","XII"),
        Lugar("Puerta de Alcala","XV")]),

    Viaje(3,"Roma", 1800.64, 4.5, "avion",[
        Lugar("Coliseo","XVII"),
        Lugar("Palacio Real","XX"),
        Lugar("Fontana di Trevi","XI")]),

    Viaje(4,"Tokio", 5000.54, 5, "avion",[
        Lugar("Akihabara","XIX"),
        Lugar("Palacio Real","XX"),
        Lugar("Torre Tokio","XIX"),
        Lugar("Montaña Fuji","X")]),

    Viaje(5,"Berlin", 1200.12, 3.5, "autobus",[
        Lugar("Muro de Berlin","XVIII"),
        Lugar("Puerta de Brandeburgo","XVIII")]),

    Viaje(6,"Madrid", 1000.13, 4, "coche",[
        Lugar("Puerta de Alcala","XIX"),
        Lugar("Palacio Real","XX"),
        Lugar("Parque de Retiro","XVIII")]),
]
