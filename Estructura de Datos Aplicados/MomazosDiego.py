import tkinter as tk
from tkinter import messagebox
import random

# Funciones para el Modo 1: Forty-Two Showdown

def draw_card():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_total(cards):
    total = 0
    for card in cards:
        if card in ['J', 'Q', 'K']:
            total += 10
        else:
            total += card
    return total

# Funciones para el Modo 2: Poker Madness

def initialize_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [rank + " of " + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def evaluate_hand(hand):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    hand_values = [card.split(" ")[0] for card in hand]
    values = [ranks[value] for value in hand_values]
    
    values.sort()
    
    return max(values)

# Interfaz Gráfica con Tkinter

class PokerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker Madness & Forty-Two Showdown")
        self.geometry("600x400")

        self.mode = None
        self.current_player = None
        self.players = {}

        # Instrucciones
        self.instruction_label = tk.Label(self, text="Selecciona un modo de juego:", font=("Helvetica", 14))
        self.instruction_label.pack(pady=20)

        # Botones para seleccionar modo de juego
        self.button_forty_two = tk.Button(self, text="Modo Forty-Two Showdown", width=30, command=self.start_forty_two)
        self.button_forty_two.pack(pady=10)

        self.button_poker_madness = tk.Button(self, text="Modo Poker Madness", width=30, command=self.start_poker_madness)
        self.button_poker_madness.pack(pady=10)

    def start_forty_two(self):
        self.mode = "forty_two"
        self.clear_window()
        self.forty_two_showdown()

    def start_poker_madness(self):
        self.mode = "poker_madness"
        self.clear_window()
        self.poker_madness()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def forty_two_showdown(self):
        self.instruction_label = tk.Label(self, text="Modo Forty-Two Showdown", font=("Helvetica", 14))
        self.instruction_label.pack(pady=20)

        # Repartir cartas y mostrar al jugador
        self.players["Jugador"] = [draw_card(), draw_card()]
        total = calculate_total(self.players["Jugador"])
        self.card_label = tk.Label(self, text=f"Cartas: {self.players['Jugador']} (Total: {total})", font=("Helvetica", 12))
        self.card_label.pack(pady=20)

        self.hit_button = tk.Button(self, text="Hit", command=self.hit)
        self.hit_button.pack(pady=10)

        self.stand_button = tk.Button(self, text="Stand", command=self.stand)
        self.stand_button.pack(pady=10)

    def hit(self):
        new_card = draw_card()
        self.players["Jugador"].append(new_card)
        total = calculate_total(self.players["Jugador"])
        self.card_label.config(text=f"Cartas: {self.players['Jugador']} (Total: {total})")
        if total > 42:
            messagebox.showinfo("Resultado", "¡Te has pasado de 42! Has perdido.")
            self.clear_window()
            self.start_forty_two()

    def stand(self):
        total = calculate_total(self.players["Jugador"])
        if total > 42:
            messagebox.showinfo("Resultado", "¡Te has pasado de 42! Has perdido.")
        else:
            messagebox.showinfo("Resultado", f"Tu total es {total}. El dealer jugará ahora.")
            self.dealer_play()

    def dealer_play(self):
        dealer_cards = [draw_card(), draw_card()]
        dealer_total = calculate_total(dealer_cards)
        while dealer_total < 30:
            new_card = draw_card()
            dealer_cards.append(new_card)
            dealer_total = calculate_total(dealer_cards)

        messagebox.showinfo("Resultado del Dealer", f"El dealer tiene: {dealer_cards} (Total: {dealer_total})")
        self.determine_winner(dealer_total)

    def determine_winner(self, dealer_total):
        player_total = calculate_total(self.players["Jugador"])
        if player_total > 42:
            messagebox.showinfo("Resultado Final", "¡Te has pasado de 42! Has perdido.")
        elif dealer_total > 42:
            messagebox.showinfo("Resultado Final", "¡El dealer se ha pasado de 42! Has ganado.")
        elif player_total > dealer_total:
            messagebox.showinfo("Resultado Final", "¡Has ganado!")
        elif player_total < dealer_total:
            messagebox.showinfo("Resultado Final", "¡El dealer gana!")
        else:
            messagebox.showinfo("Resultado Final", "¡Es un empate!")

    def poker_madness(self):
        self.instruction_label = tk.Label(self, text="Modo Poker Madness", font=("Helvetica", 14))
        self.instruction_label.pack(pady=20)

        self.deck = initialize_deck()
        num_players = int(input("¿Cuántos jugadores en Poker Madness? "))
        self.hands = {}
        
        for i in range(num_players):
            player_name = input(f"Nombre del jugador {i+1}: ")
            self.hands[player_name] = [self.deck.pop() for _ in range(5)]

        # Mostrar manos iniciales
        for player_name, hand in self.hands.items():
            hand_text = f"{player_name} tiene: {hand}"
            hand_label = tk.Label(self, text=hand_text, font=("Helvetica", 12))
            hand_label.pack(pady=5)

        self.swap_button = tk.Button(self, text="Intercambiar Cartas", command=self.swap_cards)
        self.swap_button.pack(pady=10)

    def swap_cards(self):
        for player_name, hand in self.hands.items():
            swap_count = random.randint(0, 3)
            for _ in range(swap_count):
                hand.append(self.deck.pop())
            hand_text = f"{player_name} tiene ahora: {hand}"
            hand_label = tk.Label(self, text=hand_text, font=("Helvetica", 12))
            hand_label.pack(pady=5)

        self.evaluate_poker_hands()

    def evaluate_poker_hands(self):
        rankings = {}
        for player_name, hand in self.hands.items():
            hand_value = evaluate_hand(hand)
            rankings[player_name] = hand_value

        winner = max(rankings, key=rankings.get)
        messagebox.showinfo("Resultado", f"El ganador es {winner} con una mano de valor {rankings[winner]}.")

if __name__ == "__main__":
    app = PokerApp()
    app.mainloop()