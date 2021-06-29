import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
 'Seven':7, 'Eight':8, 
 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            # taking suits one by one
            for rank in ranks:
                #taking rank one by one from ranks
                #creating a card object
                created_card = Card(suit,rank)#here we created a card by assigning the suit and rank to the card class
                self.all_cards.append(created_card)
                #this for loop creates a new deck for us
                #now we don't have to creat a card one by one 

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self,name):
        self.name = name
        self.allcards = []

    def remove_one(self):
        return self.allcards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):#this is for multiple card object
            self.allcards.extend(new_cards)
        else:#this is for single card
            self.allcards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.allcards)} cards.'

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.allcards) == 0:
        print("Player One, out of cards! player two wins")
        game_on = False
        break

    if len(player_two.allcards) == 0:
        print("Player Two, out of cards! player one wins")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAR!")
            if len(player_one.allcards) < 5:
                print("player ONE unable to declare war")
                print("player TWO wins")
                game_on = False
                break

            elif len(player_two.allcards) < 5:
                print("player TWO unable to declare war")
                print("player ONE wins")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())




