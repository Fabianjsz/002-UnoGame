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
print(unoDeck)

"""
Draw card function that draws specific number of cards
Parameters: numCards -> integer
Return. cardsDrawn -> List
"""

def drawCard(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

player1 = drawCard(5)
player2 = drawCard(5)

print(player1, player2)


