import random

# Define card values for Blackjack (For Forty-Two Showdown)
cartas = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}
baraja = list(cartas.keys()) * 4  # 4 suits for each card

# Function to draw a random card
def repartir_carta():
    return random.choice(baraja)

# Function to calculate the score of a hand
def calcular_puntaje(mano):
    puntaje = sum(cartas[carta] for carta in mano)
    num_ases = mano.count('A')
    
    # Adjust the Ace value if the total exceeds 42
    while puntaje > 42 and num_ases:
        puntaje -= 10
        num_ases -= 1

    return puntaje

# Wild Rules for chaos events
def activar_regla_aleatoria():
    eventos = [
        "Lucky Seven", "Reverse Chaos", "Joker’s Gamble", "Double Trouble", "Mystery Draw", "Chaos Boost"
    ]
    return random.choice(eventos)

# Handle special events
def aplicar_evento(evento, jugadores, jugador_actual):
    print(f"Evento Aleatorio Activado: {evento}")
    if evento == "Lucky Seven":
        # Player steals a random card from another player
        jugador_destino = random.choice([jug for jug in jugadores if jug != jugador_actual])
        carta_robada = random.choice(jugador_destino['mano'])
        jugador_destino['mano'].remove(carta_robada)
        jugador_actual['mano'].append(carta_robada)
        print(f"{jugador_actual['nombre']} robó una carta de {jugador_destino['nombre']}: {carta_robada}")
    elif evento == "Reverse Chaos":
        # The lowest total wins
        return True
    elif evento == "Joker’s Gamble":
        # If face card is drawn, roll a die to reset score
        if any(carta in ['J', 'Q', 'K'] for carta in jugador_actual['mano']):
            if random.randint(1, 6) in [1, 2]:
                print(f"{jugador_actual['nombre']} tuvo un mal golpe y su total se reseteó a 20.")
                jugador_actual['puntaje'] = 20
    elif evento == "Double Trouble":
        # Two players with the same total must draw an extra mystery card
        if len(jugadores) == 2 and jugadores[0]['puntaje'] == jugadores[1]['puntaje']:
            carta_extra = repartir_carta()
            jugadores[0]['mano'].append(carta_extra)
            jugadores[1]['mano'].append(carta_extra)
            print(f"{jugadores[0]['nombre']} y {jugadores[1]['nombre']} tomaron una carta extra misteriosa: {carta_extra}")
    elif evento == "Mystery Draw":
        # All players take a random card
        for jugador in jugadores:
            carta_misteriosa = repartir_carta()
            jugador['mano'].append(carta_misteriosa)
            print(f"{jugador['nombre']} tomó una carta misteriosa: {carta_misteriosa}")
    elif evento == "Chaos Boost":
        # If player hits exactly 21, double their total
        if calcular_puntaje(jugador_actual['mano']) == 21:
            print(f"{jugador_actual['nombre']} acertó un 21 y su total se duplicó.")
            jugador_actual['puntaje'] *= 2

    return False

# Game modes
def jugar_forty_two_showdown():
    print("\n¡Bienvenido a Forty-Two Showdown!\n")

    # Initialize players
    jugadores = [
        {'nombre': 'Jugador 1', 'mano': [repartir_carta(), repartir_carta()], 'puntaje': 0},
        {'nombre': 'Jugador 2', 'mano': [repartir_carta(), repartir_carta()], 'puntaje': 0}
    ]

    # Calculate initial scores
    for jugador in jugadores:
        jugador['puntaje'] = calcular_puntaje(jugador['mano'])
        print(f"{jugador['nombre']} tiene: {jugador['mano']} (Puntaje: {jugador['puntaje']})")

    # Players' turns to decide Hit or Stand
    for jugador in jugadores:
        while jugador['puntaje'] < 42:
            accion = input(f"\n{jugador['nombre']}, ¿quieres otra carta? (s/n): ").lower()
            if accion == 's':
                carta = repartir_carta()
                jugador['mano'].append(carta)
                jugador['puntaje'] = calcular_puntaje(jugador['mano'])
                print(f"{jugador['nombre']} ahora tiene: {jugador['mano']} (Puntaje: {jugador['puntaje']})")
            else:
                break

    # Trigger a random event
    if random.random() < 0.3:  # 30% chance to trigger a random event
        evento = activar_regla_aleatoria()
        reverso = aplicar_evento(evento, jugadores, jugadores[0])  # Apply event to the first player

        # If the event is "Reverse Chaos", reverse the win condition
        if reverso:
            jugadores = sorted(jugadores, key=lambda j: j['puntaje'])  # Lowest score wins
            print("\n¡La ronda ha sido invertida! Ahora el jugador con el menor puntaje gana.")

    # Determine the winner
    jugadores = sorted(jugadores, key=lambda j: j['puntaje'], reverse=True)  # Highest score wins

    print("\nResultados finales:")
    for jugador in jugadores:
        print(f"{jugador['nombre']} tiene: {jugador['mano']} (Puntaje: {jugador['puntaje']})")

    if jugadores[0]['puntaje'] > 42:
        print(f"{jugadores[0]['nombre']} ¡se pasó de 42 y perdió!")
    elif jugadores[0]['puntaje'] == jugadores[1]['puntaje']:
        print("¡Es un empate!")
    else:
        print(f"{jugadores[0]['nombre']} ¡es el ganador!")

# Main function to select game mode
def main():
    print("Selecciona un modo de juego:")
    print("1. Forty-Two Showdown")
    print("2. Twisted Poker")

    opcion = input("Elige una opción (1/2): ")

    if opcion == '1':
        jugar_forty_two_showdown()
    else:
        print("El modo Twisted Poker no está implementado aún. ¡Pronto habrá más sorpresas!")

if __name__ == "__main__":
    main()
