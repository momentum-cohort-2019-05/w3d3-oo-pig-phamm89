import random

class RollAOneException(Exception):
    pass

class Dice:
    """Create a die to play Pig"""

    def __init__(self):
        self.value = random.randint(1, 6)

    def roll(self):
        """Rolls die and returns value or raises RollAOneException"""
        self.value = random.randint(1, 6)

        if self.value == 1:
            raise RollAOneException
        
        return self.value    

    def __str__(self):
        return "Roll: " + str(self.value)


class Player:
    """Creates player for Pig"""

    def __init__(self, name=None):
        self.name = name
        self.score = 0
    
    def add_score(self, player_score):
        """Adds the player_score to their total score."""
        self.score += player_score
    
    def __str__(self):
        """Returns player name and current score."""
        return f"{self.name}: {self.score}"
    

class HumanPlayer(Player):
    """Creates human player for Pig"""

    def __init__(self, name="Player1"):        
        super(HumanPlayer, self).__init__(name)
    
    def keep_rolling(self, turn):
        """Asks player if they want to continue rolling."""

        player_command = input("Hit R to Roll Again or H to Hold: ")
        if player_command.lower() == "r":
            return True
        else: 
            return False


class ComputerPlayer1(Player):
    """Creates computer player for Pig"""

    def __init__(self, name="CPU_1"):  
        super(ComputerPlayer1, self).__init__(name)
    
    def keep_rolling(self, turn):
        """Computer continues rolling until computer hits 20 points or raises exception"""

        while turn.value < 20:
            print("Computer will roll again.")
            return True
        print("Computer will hold.")
        return False

class ComputerPlayer2(Player):
    """Creates computer player for Pig"""

    def __init__(self, name="CPU_2"):  
        super(ComputerPlayer2, self).__init__(name)
    
    def keep_rolling(self, turn):
        """Computer continues rolling until computer hits 20 points or raises exception"""

        while turn.value < 25:
            print("Computer will roll again.")
            return True
        print("Computer will hold.")
        return False


class Turn:
    """Temporarily holds score for each turn"""

    def __init__(self):
        self.value = 0
   
    def score_reset(self):
        """Resets score to 0 after a turn"""
        self.value = 0

    def add_dice_value(self, dice_value):
        """Adds the roll total from a turn to the player"""
        self.value += dice_value


class GamePlay:
    """Initializes game play for Pig"""
    def __init__(self, humans=1, computers=1):
        
        self.players = []

        self.players.append(HumanPlayer('Player1'))
        self.players.append(ComputerPlayer1('CPU_1'))
        self.players.append(ComputerPlayer2('CPU_2'))

        self.dice = Dice()
        self.turn = Turn()
    
    def choose_first_player(self):
        """Randomly chooses between the user and computer to decide who starts play."""
    
        self.current_player = random.randint(1, 3) % 3

        print('\n{} starts'.format(self.players[self.current_player].name))

    def next_player(self):
        """Switch to next player"""
        self.current_player = (self.current_player + 1) % 3
    
    def previous_player(self):
        """Switch to previous player"""
        self.current_player = (self.current_player - 1) % 3
    
    def get_scores(self):
        """Returns all players' scores"""

        return ', '.join(str(player) for player in self.players)
    

    def keep_rolling(self):
            """Keep rolling dice if user wants to keep rolling. Do not keep rolling when dice rolls value of 1 or when user decides to hold."""

            try:
                dice_value = self.dice.roll()
                self.turn.add_dice_value(dice_value)
                print('Previous Roll: {}, Turn Total: {}'.format(dice_value, self.turn.value))

                return self.players[self.current_player].keep_rolling(self.turn)

            except RollAOneException:
                print('  Rolled a 1. Switching to next player.')
                self.turn.score_reset()
                return False
    
    def playgame(self):
        """Plays Pig"""

        print("Welcome to Pig Game!")
        self.choose_first_player()


        while all(player.score < 100 for player in self.players):
            print('\nCurrent Score: {}'.format(self.get_scores()))
            print('\n {} is playing now.'.format(self.players[self.current_player].name))
            self.turn.score_reset()

            while self.keep_rolling():
                pass

            self.players[self.current_player].add_score(self.turn.value)
            self.next_player()

        # Winner is the player to reach 100 or more first
        self.previous_player()
        print(' {} has won the game! '.format(self.players[self.current_player].name))
    


def main():
    human_players = 1
    computers = 2

    game_play = GamePlay(human_players, computers)
    game_play.playgame()


if __name__ == '__main__':
    main()

