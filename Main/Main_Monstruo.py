from Main.Elemento import Elemento, Agua, Aire, Tierra, Fuego




class Monstruo(object):
    elementos = [Elemento(), Elemento()]
    salud = 100
    daño_simple = 10
    daño_especial = 15

    def __init__(self):
        elemento_x = Elemento()
        elemento_y = Elemento()

        opcion1 = input("Elija su primer elemento\n1.Agua\n2.Tierra\n3.Fuego\n4.Aire\n")
        if opcion1 == "1":
            elemento_x = Agua()
        elif opcion1 == "2":
            elemento_x = Tierra()
        elif opcion1 == "3":
            elemento_x = Fuego()
        elif opcion1 == "4":
            elemento_x = Aire()

        opcion2 = input("Elija su segundo elemento\n1.Agua\n2.Tierra\n3.Fuego\n4.Aire\n")
        if opcion2 == "1":
            elemento_y = Agua()
        elif opcion2 == "2":
            elemento_y = Tierra()
        elif opcion2 == "3":
            elemento_y = Fuego()
        elif opcion2 == "4":
            elemento_y = Aire()

        self.elementos[0] = elemento_x
        self.elementos[1] = elemento_y
        print("El jugador", "Ha creado un monstruo de", self.elementos)
