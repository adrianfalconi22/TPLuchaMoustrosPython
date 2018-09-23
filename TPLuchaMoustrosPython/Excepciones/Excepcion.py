
class Error(Exception):
    pass


class OpcionIncorrectaError(Error):
    pass



class ExcepcionElementosIguales(Error):
    def __init__(self, message):
        super().__init__()
        self.message = message

class LimiteAtaquesEspecialesException(Error):
    pass