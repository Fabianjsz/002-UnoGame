import random

def buildDeck():
    #Example card: Red 7, Green 8, Blue Skip
    deck = []
    colors = ["Red","Yellow","Blue","Green"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two","Skip","Reverse"]
    wilds = ["Wild", "Wild Draw Four"]
    for color in colors:
        for value in values:
            cardVal = "{} {}".format(color, value)
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    return deck


def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0,107) 
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)

"""
Draw card function that draws specific number of cards
Parameters: numCards -> integer
Return. cardsDrawn -> List
"""

def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn


def showHand(player, playerHand):

    print("player {}".format(player + 1))
    print("your Hand")
    print("---------------")
    for card in playerHand:
        print(card)
    print("")


def canPlay(discardCard, playerHand):
    splitCard = discardCard.split(" ",1) 
    color = splitCard[0]
    value = splitCard[1]


    
    return True


players = []
for player in range(2):
    players.append(drawCards(5))
print(players)

playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))

while playing:
    showHand(playerTurn,players[playerTurn])
    print("Card on top of discard pile : {}".format(discards[-1]))
