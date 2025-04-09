#Johan Bertrand Ponce, Karim Carlos - TIDBIS41M

import csv
import os

# Class to store player statistics
class PlayerStats:
    def __init__(self, name, matches_played, wins, losses, favorite_hero):
        self.name = name
        self.matches_played = int(matches_played)  
        self.wins = int(wins)  
        self.losses = int(losses)  
        self.favorite_hero = favorite_hero

# Class to store a dynamic list of players
class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0

    def add_player(self, name, matches_played, wins, losses, favorite_hero):
        player = PlayerStats(name, matches_played, wins, losses, favorite_hero)  # Create a new player object
        self.array.append(player)  # Add player to the list
        self.size += 1  # Increase size

    def __str__(self):
        return '\n'.join([
            f"{player.name}: Matches: {player.matches_played}, Wins: {player.wins}, Losses: {player.losses}, Favorite Hero: {player.favorite_hero}"
            for player in self.array
        ])


def read_csv():
    playersList = DynamicArray()
    
    # Get the file path
    path = os.path.dirname(__file__)  
    file_path = os.path.join(path, 'marvel_rivals_stats.csv')

    if os.path.exists(file_path):
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            next(csv_reader, None) 

            for row in csv_reader:
                if len(row) == 5:  
                    playersList.add_player(row[0], row[1], row[2], row[3], row[4])

        print(playersList)

read_csv()
