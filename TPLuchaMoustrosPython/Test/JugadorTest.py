import unittest

from TPLuchaMoustrosPython.Juego.Elementos import Agua, Fuego, Aire, Tierra
from TPLuchaMoustrosPython.Juego.Jugador import Jugador
from TPLuchaMoustrosPython.Juego.Monstruo import Monstruo


class JugadorTest(unittest.TestCase):
    """este anda bien, pero no sé porque tira el tipos iguales del init de moustro"""
    def test_nombre(self):
        jugador = Jugador(1, "adrian", Monstruo(Agua(), Fuego()))
        nombre = jugador.__repr__()
        print(nombre)
        self.assertEqual("adrian", nombre)
    """compara mal?"""








if __name__ == '__main__':
    unittest.main()