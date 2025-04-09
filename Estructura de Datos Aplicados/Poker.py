import random

# Función para inicializar el mazo de cartas para el póker
def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [rank + " of " + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Función para repartir cartas a los jugadores
def deal_poker_cards(num_players, deck):
    hands = {}
    for i in range(num_players):
        player_name = input(f"Nombre del jugador {i+1}: ")
        hands[player_name] = [deck.pop() for _ in range(5)]
    return hands

# Función para evaluar la mano de póker
def evaluate_hand(hand):
    # Convertir las cartas a una lista de rangos (numeros)
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_values = [card.split(" ")[0] for card in hand]
    values = [ranks[value] for value in hand_values]
    
    # Verificar si hay un par, trío, etc.
    values.sort()
    
    # Evaluar la mano (simple, para demostración: solo revisa la mayor carta)
    return max(values)

# Función para el modo de juego
def play_poker_madness():
    deck = initialize_deck()
    num_players = int(input("¿Cuántos jugadores hay en Poker Madness? "))
    
    # Repartir las cartas
    hands = deal_poker_cards(num_players, deck)
    
    # Mostrar manos iniciales
    for player_name, hand in hands.items():
        print(f"{player_name} tiene: {hand}")
    
    # Rondas de intercambio de cartas (simples para la demo)
    for player_name in hands:
        swap_count = random.randint(0, 3)
        print(f"{player_name} va a cambiar {swap_count} cartas.")
        for _ in range(swap_count):
            hands[player_name].append(deck.pop())
            print(f"{player_name} recibe una nueva carta.")
    
    # Mostrar manos finales
    print("\nManos finales después de los intercambios:")
    for player_name, hand in hands.items():
        print(f"{player_name} tiene ahora: {hand}")
    
    # Evaluar las manos
    rankings = {}
    for player_name, hand in hands.items():
        hand_value = evaluate_hand(hand)
        rankings[player_name] = hand_value
        print(f"{player_name} tiene una mano con valor de {hand_value}")
    
    # Determinar al ganador (el que tiene el valor más alto)
    winner = max(rankings, key=rankings.get)
    print(f"\nEl ganador es {winner} con una mano de valor {rankings[winner]}.")

# Función para los eventos aleatorios
def random_events():
    event = random.choice(["Card Swap Roulette", "Wild Jokers", "The Bluff Challenge", "All-In Madness", "Hidden Winner"])
    print(f"¡Evento aleatorio activado: {event}!")
    if event == "Card Swap Roulette":
        print("Se realizará un intercambio de cartas al azar.")
    elif event == "Wild Jokers":
        print("Se ha designado un comodín para el juego.")
    elif event == "The Bluff Challenge":
        print("¡Un jugador intentará hacer un farol!")
    elif event == "All-In Madness":
        print("¡Todos los jugadores deben ir 'All-In'!")
    elif event == "Hidden Winner":
        print("¡El sistema determinará al ganador de manera oculta!")

# Iniciar el juego de Póker
def start_poker_game():
    random_events()
    play_poker_madness()

# Iniciar el juego
start_poker_game()