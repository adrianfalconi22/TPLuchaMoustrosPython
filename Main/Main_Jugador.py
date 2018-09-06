from Main.Monstruo import Monstruo

class Jugador(object):

    maximoAtaquesEspeciales = 4;

    #se crea el constructor
    def __init__(self):
        self.nombre = input("Introduzca su nombre: \n")
        self.monstruo = Monstruo()

    #que es este metodo?
    def __repr__(self):
        return self.nombre


    def set_nombre(self,nombre):
        if(nombre == ("")  ):
            """lanzar exepcion"""
        self.nombre = nombre

    def get_monstruo(self):
        return monstruo



