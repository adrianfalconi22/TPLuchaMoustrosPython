from Juego.Jugador import Jugador

class Juego:

     nombreDelJuego = "Lucha de Monstruos"
	 Jugador jugadores
	 juegoTerminado = false
	 turno = "jugador1"


	"""Constructor del juego se crea con 2 jugadores"""
	def __init__(self ,nombreJugador1, nombreJugador2):

        jugadores = ["Jugador1", "Jugador2"]
        for x in jugadores:

			jugadores[x] = new Jugador()
	    	jugadores[0].set_nombre(nombreJugador1)
	    	jugadores[1].set_nombre(nombreJugador2)



	def get_nombre_del_juego(self):
		print(nombreDelJuego)


	"""retorna el nombre del primer jugador"""
    def get_nombre_jugador_1(self):
		return jugadores[0].getNombre()

	"""retorna el nombre del segundo jugador """
    def get_nombre_jugador_2(self):
        return jugadores[1].getNombre()

	public Jugador getJugador(int posicion) {
		return jugadores[posicion];
	}

	"""verifica los turnos y da las prioridades para atacar"""
	def turno(self, opcionAtaque):

		if turno.equals("jugador1") && !juegoTerminado:

			if opcionAtaque.equals("1"):
				jugadores[0].getMonstruo().ataqueBasicoTipo1(
						jugadores[1].getMonstruo())

            elif opcionAtaque.equals("2")
					&& (jugadores[0].limiteAtaqueEspecial()):
				jugadores[0].getMonstruo().ataqueEspecialTipo1(
						jugadores[1].getMonstruo())

			elif opcionAtaque.equals("3"):
				jugadores[0].getMonstruo().ataqueBasicoTipo2(
						jugadores[1].getMonstruo())

			elif opcionAtaque.equals("4")
					&& (jugadores[0].limiteAtaqueEspecial()):
				jugadores[0].getMonstruo().ataqueEspecialTipo2(
						jugadores[1].getMonstruo());

		        else {
				throw new ErrorDeAtaque();
			}
			turno = "jugador2";
		} elif turno.equals("jugador2") && !juegoTerminado:
			if opcionAtaque.equals("1"):
				jugadores[1].getMonstruo().ataqueBasicoTipo1(
						jugadores[0].getMonstruo())

			    elif opcionAtaque.equals("2")
					&& (jugadores[1].limiteAtaqueEspecial()):
				jugadores[1].getMonstruo().ataqueEspecialTipo1(
						jugadores[0].getMonstruo());

                 elif opcionAtaque.equals("3"):
				jugadores[1].getMonstruo().ataqueBasicoTipo2(
						jugadores[0].getMonstruo());

			    elif opcionAtaque.equals("4")
					&& (jugadores[1].limiteAtaqueEspecial()):
				jugadores[1].getMonstruo().ataqueEspecialTipo2(
						jugadores[0].getMonstruo());


           else:
				throw new ErrorDeAtaque();

			turno = "jugador1";


	"""verifica cuando los puntos de algun monstruo llego a cero y termina el
	 * juego"""
	def is_juego_terminado(self):
		if jugadores[0].getMonstruo().getPuntosDeVida() <= 0:
			juegoTerminado = true
			ganador = jugadores[1].getNombre()
        elif jugadores[1].getMonstruo().getPuntosDeVida() <= 0:
			juegoTerminado = true
			ganador = jugadores[0].getNombre()

		return juegoTerminado


	def get_ganador(self):

		return ganador;


