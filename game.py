import csv
import random
from typing import List
from collections import defaultdict

class Rollable:
    def __init__(self, choice):
        self.choice = choice
    
    # This function delivers random rolls of the dice as per the user's choice of dice/s
    def roll(self) -> int:
        if self.choice == 1:
            return random.randint(1, 4)
        elif self.choice == 2:
            return random.randint(1, 6)
        elif self.choice == 3:
            return random.randint(2, 10)

class Player:
    def __init__(self, name):
        self.name = name
        self.location = 0

class Game:
    def __init__(self, players: List[Player], rollable: Rollable, board, chutes_position, ladders_position, choice):
        self.players = players
        self.rollable = rollable
        self.board = board
        self.chutes_position = chutes_position 
        self.ladders_position = ladders_position
        self.choice = choice

    def play_game(self):
        while True:
            for player in self.players:
                roll_val = self.rollable.roll()
                print(f"{player.name} rolls a {roll_val}.")
                
                player.location += roll_val
                print(f"{player.name} is at a location {player.location}.")
                
                if player.location == 100:
                    print(f"{player.name} wins!")
                    return

                # Covering Multiple edge cases:
                  # Case - 1: If the user is using both the dices i.e. 4-sided and 6-sided, if the players land on position 99 on the board 
                  #           either by dice roll or climbing the ladder --> they can't win, and it will result in infinite operation.
                  # Case - 2: If the player rolls the dice and position after the roll is greater than 100.
                # In both the above cases, rolling back the player's position to their previous ones.
                elif (player.location == 99 and self.choice == 3) or player.location > 100:
                    player.location -= roll_val
                    print(f"{player.name} rolls back to a location {player.location}.")

                square_val = self.board[player.location - 1]
                
                if square_val.startswith("L"):
                    print("Square Value", square_val)
                    # Player landed on a ladder
                    # Update the player location as per the ladder's top location i.e. highest value of ladder
                    ladder_location = self.ladders_position[square_val]
                    print(f"{player.name} climbed a ladder to location {ladder_location}.")
                    
                    if ladder_location == 99 and self.choice == 3:
                        print(f"{player.name} rolls back to a location {player.location}.")
                    else:
                        player.location = ladder_location
                                    
                elif square_val.startswith("S"):
                    print("Square Value", square_val)
                    # Player landed on a chute/snake
                    # Update the player location as per the tail location of the snake i.e. lower value of the chute 
                    chute_location = self.chutes_position[square_val]
                    player.location = chute_location
                    print(f"{player.name} slids down a chute/snake to location {chute_location}.")

# The function helps in loading the board, and populate Hashmap with ladders and Chutes/snakes location
def load_board_from_csv(file_path, chutes_dict, ladders_dict):
    board = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            board.extend(row[:10])

        for indx in range(len(board)):
            if board[indx].startswith("L"):
                if board[indx] in ladders_dict:
                    ladders_dict[board[indx]] = max((indx+1),ladders_dict[board[indx]])
                else:
                    ladders_dict[board[indx]] = indx+1
            
            elif board[indx].startswith("S"):
                if board[indx] in chutes_dict:
                    chutes_dict[board[indx]] = min((indx+1),chutes_dict[board[indx]])
                else:
                    chutes_dict[board[indx]] = indx+1
    return board

if __name__ == "__main__":
    # Initializing the dictionary (HashMap) for ladders and Chutes/snakes location on the board
    chutes_dict = defaultdict()
    ladders_dict = defaultdict()
    
    # You can change the board name by updating the `board_file_path` with the  CSV descriptor file name.
    board_file_path = "board1.csv"

    # Calling the function to load the board and populate Hashmap with ladders and Chutes/snakes location
    board_data = load_board_from_csv(board_file_path, chutes_dict, ladders_dict)

    # Asking the user to enter the number of players who will be playing the game
    number_of_players = int(input("Please enter the total number of players: "))
    print("Total Number of Players:",number_of_players)

    # Requesting the user to enter the players name
    players_name = []
    for indx in range(number_of_players):
        player_name = Player(input(f"Enter the name of player{indx+1}.:"))
        players_name.append(player_name)
    players = players_name

    # Asking the user to enter their choice --> Which kind of dice/s they want to play with.
    print("What kind of dice/dices you wanna play with:")
    print("Enter 1 for 4-sided dice")
    print("Enter 2 for 6-sided dice")
    print("Enter 3 for both 4-sided and 6-sided dices")
    choice = int(input("Please enter your choice: "))

    # Calling the Rollable class, and providing the user's choice of dice/s
    rollable = Rollable(choice)

    # Start playing the game.
    game = Game(players, rollable, board_data, chutes_dict, ladders_dict, choice)
    
    game.play_game()