import random
import pyinputplus as pyip
 
# The Card class definition
class Card:

    def __init__(self, suit, value, card_value):
         
        # Suit of the Card like Spades and Clubs
        self.suit = suit
 
        # Representing Value of the Card like A for Ace, K for King
        self.value = value
 
        # Score Value for the Card like 10 for King
        self.card_value = card_value

# Function to print the cards
def print_cards(cards, hidden):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()
 
# Function for a single game of blackjack
def blackjack_game(deck):

    print("""\033[92m

.-..-. _  .-.                 .--.  .-.                .-.   .--.
: :; ::_;.' `.               : .--'.' `.               : :  :_,. :
:    :.-.`. .'   .--. .--.   `. `. `. .'.--.  ,-.,-. .-' :    ,','
: :: :: : : :   ' .; :: ..'   _`, : : :' .; ; : ,. :' .; :   :_;
:_;:_;:_; :_;   `.__.':_;    `.__.' :_;`.__,_;:_;:_;`.__.'   :_;                                                           

    \033[0m""")

    while True:
        player1 = input("What is your name, superstar? ")

        if player1 == '':
            print("Username is empty, please select a name")

        elif player1 != '':
            break

    print("Welcome {}! Let's play! ".format(player1.upper()))
    print("-"*40)
    print("\033[92mWELCOME TO THE BLACKJACK TABLE\033[0m")
    print("-"*40)

    while True:
        drink = input("Would you like a drink? (Y/N) ")
            
        if drink == '':
            print("Please make a choice  ")

        elif drink != '':
            break

    if drink.upper() == "Y":
        drink_choice = pyip.inputNum(prompt="Perfect! What kind of drink would you like? eg.(1,2,3)\n 1. Beer  2. Wine  3. Cocktail   ", min=1, lessThan=4)

        if drink_choice == 1:
            print("""\033[93m
         .   *   ..  . *  *
       *  * @()Ooc()*   o  .
           (Q@*0CG*O()  ___
          |\_________/|/ _ \'
          |  |  |  |  | / | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | | | |
          |  |  |  |  | \_| |
          |  |  |  |  |\___/  
          |\_|__|__|_/|
           \_________/

There you are! Enjoy your beer!\n
The bartenders are efficient around here.
    \033[0m""")
        
        if drink_choice == 2:
            print("""\033[35m
               __
              [__]
              |  |
              |  |
              |  |
              |  |
              |  |
 ,----.      /`-. \'
(      )    /-._|  \'
|`----'|   |        |
\      /   |`-...   |
 `.  ,'    |'` . |  |
   ||      |`,'- |  |
 ,-||-.    |`-...|  |
(  ''  )   |        | 
 `----'     `-....-' 

There you are! Enjoy your wine!\n
The bartenders are efficient around here.
    \033[0m""")
        
        if drink_choice == 3:
            print('''\033[96m        
         \ 
   .\"""""""""-.
   \`\-------'`/
    \ \__ o . /
     \/  \  o/
      \__/. /
       \_ _/
         Y
         |
         |
     _.-' '-._
    `---------`

There you are! Enjoy your cocktail!\n
The bartenders are efficient around here.
        \033[0m''')

    print("-"*40)
    rules = input("Do you know how to play? (Y/N) ")
    if rules.upper() == "N":
        print("Okay! The rules are simple. You and the dealer will receive two cards in your hand. \n"
              "Your goal is to beat the dealer by getting closer to 21.\nIf you and the dealer have the same number, it's a tie or push \n"
              "Cards 2 - 10 counts as it's own number; jacks, queens, and kings counts as 10 each, and aces can count\n"
              "as either 1 or 11. You can draw up to four cards at this table.")
        print("-"*40)
        print("Let's begin blackjack!")
        print("-"*40)
    else:
        print("Let's begin blackjack!")
        print("-"*40)
 
    # Cards for both dealer and player
    player_cards = []
    dealer_cards = []
 
    # Scores for both dealer and player
    player_score = 0
    dealer_score = 0
 
    # Initial dealing for player and dealer
    while len(player_cards) < 2:
 
        # Randomly dealing a card
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
 
        # Updating the player score
        player_score += player_card.card_value
 
        # In case both the cards are Ace, make the first ace value as 1 
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10
 
        # Print player cards and score      
        print("{}'S CARDS: ".format(player1.upper()))
        print_cards(player_cards, False)
        print("{}'S SCORE = ".format(player1.upper()), player_score)
 
        input()
 
        # Randomly dealing a card
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer score
        dealer_score += dealer_card.card_value
 
        # Print dealer cards and score, keeping in mind to hide the second card and score
        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False)
            print("DEALER SCORE = ", dealer_score)
        else:
            print_cards(dealer_cards[:-1], True)    
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
        # In case both the cards are Ace, make the second ace value as 1 
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
 
        input()
 
    # Player gets a blackjack   
    if player_score == 21:
        print("{} HAS A BLACKJACK!!!!".format(player1.upper()))
        print("{} WINS!!!!".format(player1.upper()))
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()

        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    # Print dealer and player cards
    print("DEALER CARDS: ")
    print_cards(dealer_cards[:-1], True)
    print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
    print() 
 
    print("{}'S CARDS: ".format(player1.upper()))
    print_cards(player_cards, False)
    print("{}'S SCORE = ".format(player1.upper()), player_score)
 
    # Managing the player moves
    while player_score < 21:
        choice = input("Enter H to Hit or S to Stand : ")
 
        # Sanity checks for player's choice
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Wrong choice!! Try Again")
 
        # If player decides to HIT
        if choice.upper() == 'H':
 
            # Dealing a new card
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # Updating player score
            player_score += player_card.card_value
 
            # Updating player score in case player's card have ace in them
            c = 0
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
   
 
            # Print player and dealer cards
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
 
            print()
 
            print("{}'S CARDS: ".format(player1.upper()))
            print_cards(player_cards, False)
            print("{}'S SCORE = ".format(player1.upper()), player_score)
             
        # If player decides to Stand
        if choice.upper() == 'S':
            break
 
 
    # Print player and dealer cards
    print("{}'S CARDS: ".format(player1.upper()))
    print_cards(player_cards, False)
    print("{}'S SCORE = ".format(player1.upper()), player_score)
 
    print()
    print("DEALER IS REVEALING THE CARDS....")
 
    print("DEALER CARDS: ")
    print_cards(dealer_cards, False)
    print("DEALER SCORE = ", dealer_score)
 
    # Check if player has a Blackjack
    if player_score == 21:
        print("{} HAS A BLACKJACK".format(player1.upper()))
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()

        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    # Check if player busts
    if player_score > 21:
        print("{} BUSTED!!! GAME OVER!!!".format(player1.upper()))
        print("-"*40)
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()
        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    input() 
 
    # Managing the dealer moves
    while dealer_score < 17:
 
        print("DEALER DECIDES TO HIT.....")
 
        # Dealing card for dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer's score
        dealer_score += dealer_card.card_value
 
        # Updating player score in case player's card have ace in them
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1
 
        # print player and dealer cards
        print("{}'S CARDS: ".format(player1.upper()))
        print_cards(player_cards, False)
        print("{}'S SCORE = ".format(player1.upper()), player_score)
 
        print()
 
        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)      
 
        input()
 
    # Dealer busts
    if dealer_score > 21:        
        print("DEALER BUSTED!!! YOU WIN!!!") 
        print("-"*40)
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()

        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    # Dealer gets a blackjack
    if dealer_score == 21:
        print("DEALER HAS A BLACKJACK!!! {} LOSES".format(player1.upper()))
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()

        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    # TIE Game
    if dealer_score == player_score:
        print("TIE GAME!!!!")
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()
        elif anothergame.upper() == "Y":
            blackjack_game(deck)
 
    # Player Wins
    elif player_score > dealer_score:
        print("{} WINS!!!".format(player1.upper()))
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()
        elif anothergame.upper() == "Y":
            blackjack_game(deck)                 
 
    # Dealer Wins
    else:
        print("DEALER WINS!!!")
        anothergame = input("Want to try another round?(Y/N) ")
        if anothergame.upper() == "N":
            print("Thanks for playing! Come back for free martinis anytime!")
            quit()
        elif anothergame.upper() == "Y":
            blackjack_game(deck)                 
 
if __name__ == '__main__':
 
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit value 
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # The deck of cards
    deck = []
 
    # Loop for every type of suit
    for suit in suits:
 
        # Loop for every type of card in a suit
        for card in cards:
 
            # Adding card to the deck
            deck.append(Card(suits_values[suit], card, cards_values[card]))

    
     
    blackjack_game(deck)    