class Elemento:
    def __repr__(self):
        return "Elemento"

    def calculo_daño(self, daño, elemento_atacante, monstruo_atacado):
        c = 0
        d = 0
        if elemento_atacante.ataque is monstruo_atacado.elemento_x.__repr__():
            c = daño * 0.2
        elif elemento_atacante.ataque is monstruo_atacado.elemento_y.__repr__():
            c = daño * 0.2
        elif monstruo_atacado.elemento_x.defensa is elemento_atacante.__repr__():
            d = daño * 0.2
        elif monstruo_atacado.elemento_y.defensa is elemento_atacante.__repr__():
            d = daño * 0.2
        return daño + c - d


class Agua(Elemento):

    def __init__(self):
        self.ataque = "Fuego"
        self.defensa = "Tierra"

    def __repr__(self):
        return "Agua"


class Aire(Elemento):

    def __init__(self):
        self.ataque = "Agua"
        self.defensa = "Fuego"

    def __repr__(self):
        return "Aire"


class Fuego(Elemento):

    def __init__(self):
        self.ataque = "Tierra"
        self.defensa = "Agua"

    def __repr__(self):
        return "Fuego"


class Tierra(Elemento):

    def __init__(self):
        self.ataque = "Aire"
        self.defensa = "Aire"

    def __repr__(self):
        return "Tierra"


