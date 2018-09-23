from TPLuchaMoustrosPython.Juego.Jugador import Jugador
from TPLuchaMoustrosPython.Juego.Elementos import Agua, Aire, Fuego, Tierra, Elemento


import csv
import os
import fnmatch

from TPLuchaMoustrosPython.Juego.Monstruo import Monstruo


class Menu:

    def abrir_menu(self):
        while True:
            print("\n\n\nBienvenido a Lucha de Monstruos!\n\nMenú Principal")

            try:
                opcion = int(input("1. Nueva partida\n2. Cargar partida\n3. Salir\n"))
                if opcion is 1:
                    self.jugador0 = Jugador(1, self.nombre_jugador(1),
                                            Monstruo(self.monstruo_primer_elemento(), self.monstruo_segundo_elemento()))
                    self.jugador1 = Jugador(2, self.nombre_jugador(2),
                                            Monstruo(self.monstruo_primer_elemento(), self.monstruo_segundo_elemento()))
                    self.jugar(self.jugador0, self.jugador1)
                    """acá rompe cuando llamo a jugar"""
                elif opcion is 2:
                    self.asignar_jugadores(self.cargar_partida())
                elif opcion is 3:
                    exit()
            except ValueError:
                print("Debe introducir una opción valida")
                self.abrir_menu()

    def jugar(self, jugador0, jugador1):
        self.partidas = []


        """rompe cuando voy a atacar"""
        while jugador0.monstruo.vida_moustro() > 0 and jugador1.monstruo.vida_moustro() > 0:
            jugador0.atacar(jugador1, self.jugador_elegir_elemento(jugador0),
                            self.jugador_elegir_tipo_ataque())
            self.elegir_guardar()
            jugador1.atacar(jugador0, self.jugador_elegir_elemento(jugador1),
                            self.jugador_elegir_tipo_ataque())
            self.elegir_guardar()
        else:
            print("El juego ha finalizado")

    def elegir_guardar(self):
        opcion = int(input("Desea guardar la partida?\n1. Si \n2. No"))
        try:
            if opcion is 1:
                self.guardar_partida()
            else:
                pass
        except ValueError:
            print("Opcion incorrecta. Reintente")

    def nombre_jugador(self, numero):
        inprint = "Jugador " + str(numero) + ", introduzca su nombre\n"
        inpot = input(inprint)
        return inpot

    def guardar_partida(self):
        print("Partida guardada")
        '''import csv guardar jugador numero monstruos elementos, salud '''
        nombre_partida = "Partidas\\" + "Partida" + self.jugador0.nombre + self.jugador1.nombre + ".csv"
        self.partidas.append(nombre_partida)
        savegame = open(nombre_partida, "w", newline="")
        csv_writer = csv.writer(savegame, delimiter=";")
        csv_writer.writerow(
            ("NombreJugador", "NumeroJugador", "MonstruoElementoX", "MonstruoElementoY", "MonstruoSalud"))
        csv_writer.writerow(
            (self.jugador0.nombre, self.jugador0.numero, self.jugador0.monstruo.elemento_x,
             self.jugador0.monstruo.elemento_y,
             self.jugador0.monstruo.salud))
        csv_writer.writerow(
            (self.jugador1.nombre, self.jugador1.numero, self.jugador1.monstruo.elemento_x,
             self.jugador1.monstruo.elemento_y,
             self.jugador1.monstruo.salud))
        savegame.close()

    def cargar_partida(self):
        archivo = open(("Partidas\\" + self.mostrar_partidas()), "r")
        reader = csv.reader(archivo, delimiter=";")
        jugadores = []
        next(reader, None)
        for row in reader:
            jugadores.append(row)
        archivo.close()
        return jugadores

    def asignar_jugadores(self, jugadores):
        # Se asignan los datos de los archivos a los jugadores de la partida
        self.jugador0 = Jugador(int(jugadores[0][1]), jugadores[0][0], Monstruo(self.asignar_elemento(jugadores[0][2]),
                                                                                self.asignar_elemento(jugadores[0][3])))
        self.jugador0.monstruo.salud = float(jugadores[0][4])
        self.jugador1 = Jugador(int(jugadores[1][1]), jugadores[1][0],
                                Monstruo(self.asignar_elemento(jugadores[1][2]),
                                         self.asignar_elemento(jugadores[1][3])))
        self.jugador1.monstruo.salud = float(jugadores[1][4])
        print("Se han cargado los jugadores " + self.jugador0.nombre + " y " + self.jugador1.nombre)
        print("Salud del monstruo de " + self.jugador0.nombre + ": " +
              str(self.jugador0.monstruo.salud))
        print("Salud del monstruo de " + self.jugador1.nombre + ": " +
              str(self.jugador1.monstruo.salud) + "\n")
        self.jugar(self.jugador0, self.jugador1)

    def asignar_elemento(self, string):
        elemento = Elemento()
        if string == "Agua":
            elemento = Agua()
        elif string == "Tierra":
            elemento = Tierra()
        elif string == "Fuego":
            elemento = Fuego()
        elif string == "Aire":
            elemento = Aire()
        return elemento

    def mostrar_partidas(self):
        str_partidas = ""
        list_files = os.listdir("Partidas")
        pattern = "Partida*.csv"
        archivos = []
        r = 0
        for entry in list_files:
            if fnmatch.fnmatch(entry, pattern):
                archivos.append(entry)
        for x in archivos:
            r += 1
            str_partidas += str(r) + ". " + x + "\n"
        opcion = int(input("Elija una partida\n" + str_partidas))
        return archivos[opcion - 1]

    def jugador_elegir_elemento(self, jugador):
        inprint = jugador.nombre + ", elija su elemento de ataque \n1. " \
                  + jugador.monstruo.elemento_x.__repr__() + "\n" \
                                                             "2. " + jugador.monstruo.elemento_y.__repr__()
        o_elemento = int(input(inprint))
        return o_elemento

    def jugador_elegir_tipo_ataque(self):
        o_ataque = int(input("Seleccione su tipo de ataque:\n1.Simple\n2.Especial\n"))
        return o_ataque

    def monstruo_primer_elemento(self):
        try:
            opcion1 = int(input("Elija su primer elemento\n1.Agua\n2.Tierra\n3.Fuego\n4.Aire\n"))
            return self.asignar(opcion1)
        except ValueError:
            print("Opcion incorrecta. Reintente")
            self.monstruo_primer_elemento()

    def monstruo_segundo_elemento(self):
        while True:
            try:
                elemento = Elemento()
                opcion = int(input("Elija su segundo elemento\n1.Agua\n2.Tierra\n3.Fuego\n4.Aire\n"))
                return self.asignar(opcion)
            except ValueError:
                print("Opcion incorrecta. Reintente")
                self.monstruo_primer_elemento()

    def asignar(self, opcion):
        if opcion is 1:
            return Agua()
        elif opcion is 2:
            return Tierra()
        elif opcion is 3:
            return Fuego()
        elif opcion is 4:
            return Aire()


# CRED = '\033[91m'
# CEND = '\033[0m'
# print(CRED + "Error, does not compute!" + CEND)


menu = Menu()
menu.abrir_menu()
#print(menu.monstruo_segundo_elemento())
