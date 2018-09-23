import pickle


class Juego():

    def __init__(self):
        self.diccionario_de_partidas = {}

    def guardar(self):
        with open('persistencia.p', 'wb') as handle:
            pickle.dump(self.diccionario_de_partidas, handle)

    def abrir(self):
        with open('persistencia.p', 'rb') as handle:
            self.diccionario_de_partidas = pickle.load(handle)

    def listar(self):
        lista_nombres = []
        for partida in self.diccionario_de_partidas:
            lista_nombres.append(partida)
        if len(lista_nombres) == 0:
            return "No hay partidas disponibles"
        else:
            lista_nombres.sort()
            salida = str(lista_nombres)
            return salida[1:-1]
