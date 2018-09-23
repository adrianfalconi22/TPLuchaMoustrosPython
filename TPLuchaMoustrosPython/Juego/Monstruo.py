from TPLuchaMoustrosPython.Excepciones.Excepcion import ExcepcionElementosIguales
from TPLuchaMoustrosPython.Juego.Elementos import Agua


class Monstruo(object):


    def __init__(self, elemento_x, elemento_y):
        self.vida = 100
        try:
            if elemento_x != elemento_y:
                self.elementos = (elemento_x, elemento_y)
            else:
                raise ExcepcionElementosIguales("los elementos no pueden ser iguales")
        except ExcepcionElementosIguales as error:
            print(error.message)



    def vida_moustro(self):
        return self.vida

    def elemento_1(self):
        return self.elementos(0)

    def elemento_2(self):
        return self.elementos(1)

"""
moustro = Moustro(Agua, Agua)"""