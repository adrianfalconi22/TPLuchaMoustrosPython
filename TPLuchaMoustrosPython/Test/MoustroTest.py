import  unittest

from TPLuchaMoustrosPython.Juego.Elementos import Agua, Aire, Fuego, Tierra
from TPLuchaMoustrosPython.Juego.Monstruo import Monstruo


class MoustroTest(unittest.TestCase):

    """solo quiero probar la vida, anda bien pero no se porque siempre el tira el tipos iguales"""
    def test_vida(self):
        moustro = Monstruo(Agua(), Aire())
        vida = moustro.vida_moustro()
        self.assertEqual(vida, 100)

    """compara mal?"""
    def test_tipo_1(self):
        monstruo =  Monstruo(Agua, Fuego)
        elemento = monstruo.elemento_x()
        print(elemento)
        self.assertEqual(str(Agua), str(elemento))

    """compara mal?"""
    def test_tipo_2(self):
        monstruo = Monstruo(Tierra, Fuego)
        elemento = monstruo.elemento_y()
        print(elemento)
        self.assertEqual(Fuego, elemento)

    """no se como probar cuando espero un error, devuelve el mensaje tipos iguales pero lo está devolviendo siempre
    asi que no se si esta andando bien este test"""
    def test_tipos_iguales(self):
        moustro = Monstruo(Fuego, Fuego)

if __name__ == "__main__":
    unittest.main()