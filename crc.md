            Class Responsibility Collaborator (CRC) Models


Class RollAOneException
    Responsibilities
        raises Exception

Class Dice
    Responsibilities
        Initializes a die
        Rolls a die and returns value
        Determines pig
    Collaborators
        HumanPlayer
        ComputerPlayer
        Turn 
        GamePlay
        RollAOneException


Class Player
    Responsibilities
        Initializes a player
        Calculates score
    Collaborators
        HumanPlayer
        ComputerPlayer
        Dice
        Turn 
        GamePlay


Class HumanPlayer
    Responsibilities
        Chooses to roll or hold
    Collaborators
        Player
        Turn
        GamePlay


Class ComputerPlayer1
    Responsibilities
        Rolls a die until score > 20 or raises exception
    Collaborators 
        Player
        Turn
        GamePlay


Class ComputerPlayer2
    Responsibilities
        Rolls a die until score > 25 or raises exception
    Collaborators 
        Player
        Turn
        GamePlay


Class Turn
    Responsibilities
        Initializes score of each turn
        Resets score when an exception is raised
        Adds value of each roll to score for turn
    Collaborators
        GamePlay
        HumanPlayer
        ComputerPlayer
        Dice


Class GamePlay
    Responsibilities
        Chooses first player
        Switches player each turn
        Returns all player's scores
        Rolls or Holds
        Plays Game while scores are < 100
        Determines winner
    Collaborators
        RollAOneException
        Dice
        Player
        HumanPlayer
        ComputerPlayer
        Turn