from TPLuchaMoustrosPython.Juego.Monstruo import Monstruo


class Jugador(object):
    '''el constructor de jugador necesita un numero ya sean 1 o 2 para ser mencionados en el juego
    '''

    def __init__(self, numero, nombre, monstruo):
        self.numero = numero
        self.nombre = nombre
        self.monstruo = monstruo

    def __repr__(self):
        return self.nombre

    def atacar(self, jugador_atacado, o_elemento, o_ataque):
        '''Siendo o_elemento la opcion de elemento elegida y o_ataque la opcion de ataque elegida'''
        if o_elemento is 1:

            if o_ataque is 1:
                daño = self.monstruo.elemento_x.calculo_daño(10, self.monstruo.elemento_x, jugador_atacado.monstruo)
            elif o_ataque is 2:
                daño = self.monstruo.elemento_x.calculo_daño(15, self.monstruo.elemento_x, jugador_atacado.monstruo)

        elif o_elemento is 2:
            if o_ataque is 1:
                daño = self.monstruo.elemento_y.calculo_daño(10, self.monstruo.elemento_y, jugador_atacado.monstruo)
            elif o_ataque is 2:
                daño = self.monstruo.elemento_y.calculo_daño(15, self.monstruo.elemento_y, jugador_atacado.monstruo)

        jugador_atacado.monstruo.salud -= daño
        print(self.nombre, "ha atacado a", jugador_atacado.nombre, "provocandole", daño, "puntos de daño")
        print("Salud del monstruo de", self.nombre, ":", self.monstruo.salud)
        print("Salud del monstruo de", jugador_atacado.nombre, ":", jugador_atacado.monstruo.salud)
