class Elemento(object):
    pass


class Agua(Elemento):
    # ataque = Fuego()
    # defensa = Tierra()

    def __repr__(self):
        return "Agua"


class Tierra(Elemento):
    # ataque = Aire()
    # defensa = Aire()

    def __repr__(self):
        return "Tierra"


class Fuego(Elemento):
    # ataque = Tierra()
    # defensa = Agua()

    def __repr__(self):
        return "Fuego"


class Aire(Elemento):
    # ataque = Agua()
    # defensa = Fuego()

    def __repr__(self):
        return "Aire"