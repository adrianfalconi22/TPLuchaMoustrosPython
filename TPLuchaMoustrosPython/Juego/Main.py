from TPLuchaMoustrosPython.Juego.Jugador import Jugador


def jugar():
    jugador0 = Jugador(1)
    jugador1 = Jugador(2)

    while jugador0.monstruo.salud > 0 and jugador1.monstruo.salud > 0:
        jugador0.atacar(jugador1)
        jugador1.atacar(jugador0)
    else:
        print("El juego ha finalizado")


def cargar_partida():
    pass
