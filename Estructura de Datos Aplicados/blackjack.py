import random

# Definir la baraja de cartas con valores
cartas = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}
baraja = list(cartas.keys()) * 4  # 4 palos por cada carta

# Función para repartir una carta aleatoria
def repartir_carta():
    return random.choice(baraja)

# Función para calcular el puntaje de una mano
def calcular_puntaje(mano):
    puntaje = sum(cartas[carta] for carta in mano)
    num_ases = mano.count('A')
    
    # Ajustar el valor del As si el total excede 21
    while puntaje > 21 and num_ases:
        puntaje -= 10
        num_ases -= 1

    return puntaje

# Función principal del juego
def jugar_blackjack():
    print("\n¡Bienvenido a Blackjack!\n")

    # Inicializar manos
    mano_jugador = [repartir_carta(), repartir_carta()]
    mano_banca = [repartir_carta(), repartir_carta()]

    # Mostrar cartas del jugador y una de la banca
    print(f"Tus cartas: {mano_jugador} (Puntaje: {calcular_puntaje(mano_jugador)})")
    print(f"Carta de la banca: {mano_banca[0]}")

    # Turno del jugador
    while calcular_puntaje(mano_jugador) < 21:
        accion = input("\n¿Quieres otra carta? (s/n): ").lower()
        if accion == 's':
            mano_jugador.append(repartir_carta())
            print(f"Tu nueva mano: {mano_jugador} (Puntaje: {calcular_puntaje(mano_jugador)})")
        else:
            break

    puntaje_jugador = calcular_puntaje(mano_jugador)

    # Si el jugador se pasa de 21, pierde
    if puntaje_jugador > 21:
        print("\n¡Te pasaste de 21! La banca gana.")
        return

    # Turno de la banca (sigue hasta 17 puntos o más)
    print("\nTurno de la banca...")
    print(f"Cartas de la banca: {mano_banca} (Puntaje: {calcular_puntaje(mano_banca)})")

    while calcular_puntaje(mano_banca) < 17:
        mano_banca.append(repartir_carta())
        print(f"La banca toma una carta: {mano_banca} (Puntaje: {calcular_puntaje(mano_banca)})")

    puntaje_banca = calcular_puntaje(mano_banca)

    # Determinar el resultado final
    print("\nResultados:")
    print(f"Tus cartas: {mano_jugador} (Puntaje: {puntaje_jugador})")
    print(f"Cartas de la banca: {mano_banca} (Puntaje: {puntaje_banca})")

    if puntaje_banca > 21 or puntaje_jugador > puntaje_banca:
        print("¡Ganaste!")
    elif puntaje_jugador < puntaje_banca:
        print("La banca gana.")
    else:
        print("Es un empate.")

# Iniciar el juego
if __name__ == "__main__":
    jugar_blackjack()
