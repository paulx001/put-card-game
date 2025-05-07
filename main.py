# Programmer Names: Paul Xiong
# Course: ICS 2O1
# Date: Jan 21, 2022
# Description:  1) Ask user to lead, throw, or put
#               2) Calculate the players cards, who won the round, who won the set, who won the game
#               3) Display player's cards, game, and other

# Import modules
import random

# Player
playerDeck = []
playerCard = ""
playerPoints = 0
playerRoundsWon = 0

# Computer
computerDeck = []
computerCard = ""
computerPoints = 0
computerRoundsWon = 0

# Main Variables
winner = False
currentTurn = "Player"
roundsPlayed = 0
setsPlayed = 0
setOngoing = False

# Convert the card to an int value rank
def CheckCardRank(card):
    cardValue = 0

    if card.startswith("3"):
        cardValue = 13
    elif card.startswith("2"):
        cardValue = 12
    elif card.startswith("A"):
        cardValue = 11
    elif card.startswith("K"):
        cardValue = 10
    elif card.startswith("Q"):
        cardValue = 9
    elif card.startswith("J"):
        cardValue = 8
    elif card.startswith("10"):
        cardValue = 7
    elif card.startswith("9"):
        cardValue = 6
    elif card.startswith("8"):
        cardValue = 5
    elif card.startswith("7"):
        cardValue = 4
    elif card.startswith("6"):
        cardValue = 3
    elif card.startswith("5"):
        cardValue = 2
    elif card.startswith("4"):
        cardValue = 1

    return cardValue

# Function to give the player cards
# Set the 52-deck cards
FullCardDeck = ['2D', '2C' , '2H' , '2S',
              '3D', '3C' , '3H' , '3S',
              '4D', '3C' , '4H' , '4S',
              '5D', '5C' , '5H' , '5S',
              '6D', '6C' , '6H' , '6S',
              '7D', '7C' , '7H' , '7S',
              '8D', '8C' , '8H' , '8S',
              '9D', '9C' , '9H' , '9S',
              '10D', '10C', '10H', '10S',
              'JD', 'JC' , 'JH' , 'JS',
              'QD', 'QC' , 'QH' , 'QS',
              'KD', 'KC' , 'KH' , 'KS',
              'AD', 'AC' , 'AH' , 'AS',
               ]

# Function to give players 3 cards
def GiveCards():
    global playerDeck, computerDeck, ShuffledCardDeck

    # Reset players deck
    playerDeck = []
    computerDeck = []

    # Shuffle cards
    ShuffledCardDeck = random.sample(FullCardDeck, len(FullCardDeck))
    for index in range(0, 3):
        playerDeck.append(ShuffledCardDeck.pop(0))
        computerDeck.append(ShuffledCardDeck.pop(0))

# Restart set with a function
def RestartSet():
    global setsPlayed, setOngoing, roundsPlayed, playerRoundsWon, computerRoundsWon # access global variable

    # Make sure there is actually a set ongoing to reset
    if setOngoing == True:
        roundsPlayed = 0
        playerRoundsWon = 0
        computerRoundsWon = 0
        setsPlayed += 1
        setOngoing = False

def DisplayScore():
    # Show Game Details After A Turn.
    print("\n------------------------------------")
    print("Currrent Score:")
    print("Current Round:", roundsPlayed)
    print("Player Wins -", playerRoundsWon, ":", "Computer Wins -", computerRoundsWon)
    print("Sets Played:", setsPlayed)
    print("Player Points -", playerPoints, ":", "Computer Points -", computerPoints)
    CheckGameWinner() # After displaying the game info, check if a player won the game

# Giving points function
def GivePoints(player):
    global playerPoints, computerPoints, currentTurn # access global variables

    # Check which player got the point from the parameter
    if player == "Player":
        playerPoints += 1
        print("\nPlayer won the set!")
    elif player == "Computer":
        computerPoints += 1
        print("\nComputer won the set!")

    # Make sure the game is reset for the next set
    RestartSet()
    DisplayScore()
    currentTurn = player

# Check the winner of the game function
def CheckGameWinner():
    global playerPoints, computerPoints, winner, currentTurn # access global variables
    if playerPoints >= 5:
        winner = "Player"
        currentTurn = "Player"
    elif computerPoints >= 5:
        winner = "Computer"
        currentTurn = "Computer"

def CheckRoundWinner():
    # access global variables
    global playerCard, computerCard, roundsPlayed, playerRoundsWon, computerRoundsWon, playerPoints, computerPoints, currentTurn

    playerCardRank = CheckCardRank(playerCard.upper().strip())
    computerCardRank = CheckCardRank(computerCard.upper().strip())

    # After setting the card ranks, check if they are both above 0, meaning they both have cards to compare
    if playerCardRank > 0 and computerCardRank > 0:
        print("\nPlayer -", playerCard.upper().strip(), ":", "Computer -", computerCard) # Display both the player's and the computer's chosen card
        if playerCardRank == computerCardRank:
            print("Round tied!")
        elif playerCardRank > computerCardRank:
            playerRoundsWon += 1
            currentTurn = "Player"
            print("Player won the round!")
        elif computerCardRank > playerCardRank:
            computerRoundsWon += 1
            currentTurn = "Computer"
            print("Computer won the round!")

        roundsPlayed += 1
        playerCard = ""
        computerCard = ""

        # If the last round of the set was played, check the winner of the set
        if roundsPlayed == 3:
            if playerRoundsWon == computerRoundsWon:
                print("\nSet tied!")
            elif playerRoundsWon > computerRoundsWon:
                GivePoints("Player")
            elif computerRoundsWon > playerRoundsWon:
                GivePoints("Computer")
                
            RestartSet()
        DisplayScore() # Display that the player or computer won a round
        
    else: # if both players do not have a card placed alternate turns
        if currentTurn == "Player":
            currentTurn = "Computer"
        elif currentTurn == "Computer":
            currentTurn = "Player"
        
            
# Get a random chance, used for determining computer's decision
def GetRandomChance(maxNum, Type):
    chance = 0

    if maxNum == 1:
        chance = 0
    elif Type == "Decision" or Type == "50/50":
        chance = random.randrange(1, maxNum + 1)
    elif Type == "Card":
        chance = random.randrange(1, maxNum)
        
    return chance

def DisplayPlayerDeck(playerDeck): # Display the cards to the player
    print("Your cards: ", end="")
    for card in range(0, len(playerDeck)):
        if card == len(playerDeck) - 1:
            print(playerDeck[card]) # remove comma if it is last card
        else:
            print(playerDeck[card], ", ", sep="", end="")

# Main Code Function
def main():
    global playerDeck, playerCard, computerDeck, computerCard, setsPlayed, setOngoing, roundsPlayed, playerRoundsWon, computerRoundsWon, currentTurn, computerPlayed
    
    # Before the game beings, notify the player about the game
    print("Put Game:")
    print("Cards ranked from highest to lowest: 3, 2, A, K, Q, J, 10, 9, 8, 7, 6, 5, 4")
    print("Suits are not taken into account")

    # while loop that continues the game as long as there is no winner
    while winner == False:
        # If there is no set going, give the player cards
        if setOngoing == False:
            GiveCards()
            setOngoing = True

        computerPlayed = False  # Initialize computerPlayed for each round

        # On every iteration, detect which player is playing
        if currentTurn == "Player":
            print("\n------------------------------------")
            print("Player's Turn:")
            # Show player his cards first so they know which decision to make
            DisplayPlayerDeck(playerDeck)

            action = input("Do you want to Lead, Throw, or Put: ") # ask user what they want to do
            decision = action.lower().strip() # fix string

            # What did the player choose to play
            if decision == "lead":
                print("Player chooses to Lead")
                playerCard = input("\nChoose a card from your deck: ") # ask user to choose a card
                while not playerCard.upper().strip() in playerDeck:
                    print("\nNot a card in your deck. Choose again.")
                    DisplayPlayerDeck(playerDeck)
                    playerCard = input("Choose a card from your deck: ")
                playerDeck.remove(playerCard.upper().strip())
                print("Player chooses the card: " + playerCard.upper().strip())
                CheckRoundWinner()

            elif decision == "throw":
                print("\nPlayer chooses to Throw. Computer gains a point.")
                GivePoints("Computer")
                
            elif decision == "put":
                print("Player chooses to Put.")
                chance = GetRandomChance(2, "50/50") # Computer has a 50% of choosing to throw or not
                if chance == 1:
                    print("Computer Throws. Player gains a point.")
                    GivePoints("Player")
                    CheckRoundWinner()
                    
                elif chance == 2:
                    # Computer does not throw. Player chooses a card
                    print("Computer denies.")
                    playerCard = input("\nChoose a card from your deck: ") # ask user to choose a card
                    # Keeps asking for the card if the chosen card is not in the players deck 
                    while not playerCard.upper().strip() in playerDeck:
                        print("\nNot a card in your deck. Choose again.")
                        DisplayPlayerDeck(playerDeck)
                        playerCard = input("Choose a card from your deck: ")
                    playerDeck.remove(playerCard.upper().strip())
                    print("Player chooses the card: " + playerCard.upper().strip())

                    # Forces computer to play a card if not played already
                    if not computerPlayed:
                        computerCard = computerDeck[GetRandomChance(len(computerDeck), "Card")]
                        print("Computer Leads. Computer plays the card,", computerCard)
                        computerDeck.remove(computerCard)

                    CheckRoundWinner()

                    
            else:
                print("\n" + action, "is not a valid decision. Please try again.") # input validation, loop again if user does not select one of the three options 
                    

        # else if it is computers turn
        elif currentTurn == "Computer":
            print("\n------------------------------------")
            print("Computer's Turn:")
            chance = GetRandomChance(6, "Decision")

            if chance == 1 or chance == 2 or chance == 3:  # Computer leads
                computerCard = computerDeck[GetRandomChance(len(computerDeck), "Card")]
                print("Computer Leads. Computer plays the card,", computerCard)
                computerDeck.remove(computerCard)
                computerPlayed = True  # Set computerPlayed to True
                CheckRoundWinner()

            elif chance == 4:  # Computer throw
                print("Computer Throws. Player gains a point.")
                GivePoints("Player")

            elif chance == 5 or chance == 6:  # Computer put
                action = input("Computer chooses to Put. Do you want to Throw? (Y/N): ")
                decision = action.lower().strip()

                while True:
                    if decision == "yes" or decision == "y":
                        print("Player chooses to Throw. Computer gains a point.")
                        GivePoints("Computer")
                        CheckRoundWinner()
                        break
                    if decision == "no" or decision == "n":
                        print("Player denies")
                        if not computerPlayed:  # Check if computer has already played
                            computerCard = computerDeck[GetRandomChance(len(computerDeck), "Card")]
                            print("\nComputer Leads. Computer plays the card,", computerCard)
                            computerDeck.remove(computerCard)
                            computerPlayed = True  # Set computerPlayed to True
                        CheckRoundWinner()
                        break
                    else:
                        print("\nDid not select yes or no.")
                        action = input("Computer chooses to Put. Do you want to Throw? (Y/N): ")
                        decision = action.lower().strip()

    # If there is a winner
    if winner != False:
        print("") # create new line
        print(winner, "won the game!")


# Call the main function
main()
