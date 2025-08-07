#-------------------------------------------------------------------------------
# Name:         deck.py
# Purpose:      deck for uno game
#
# Author:       Fabianjsz
#
# Created:      07.08.2025
# Copyright:    (c)  2025
# Licence:
#-------------------------------------------------------------------------------
import random
from card import Card

class Deck:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self, Card):
        self.head = Card("head",None)
        self.size = 0

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            return None
        else:
            temp1 = self.head.next.color
            temp2 = self.head.next.value
        return temp1, temp2

    # Push a value into the stack.
    def push(self, color, value):
        node = Card(color, value)
        node.next = self.head.next # Make the new node point to the current head
        self.head.next = node #!!! # Update the head to be the new node
        self.size += 1


    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next #!!! changed
        self.size -= 1
        
        return remove.color, remove.value
    
    # Build uno deck of 100 cards
    def buildDeck():
        print("test")
        deck = []
        
        #Define the card colors and values
        colors = ["Rot", "Gruen", "Gelb", "Blau"]
        values = [0,1,2,3,4,5,6,7,8,9, "drawTwo", "Reverse"]
        wilds = ["Wild", "WildDrawFour"]

        #Create the numbered and special cards for each color
        for color in colors:
            for value in values:
                cardVal = "{} {}".format(color, value)
                deck.append(cardVal)
                if value != 0:
                    deck.append(cardVal)
        
        #Add the wild cards to the deck
        for i in range(4):
            deck.append(wilds[0])
            deck.append(wilds[1])

        #Shuffle the deck
        for cardPos in range(len(deck)):
            randPos = random.randint(0,99)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
        print(deck)
        return deck
        
#
    def convertDeck(self):
        arrayDeck = self.buildDeck()
        unoDeck = Deck()

        for card in arrayDeck:
            temp = card.split(" ")
            if temp[0] == "Wild" or temp[0] == "WildDrawFour":
                unoDeck.push(temp[0], None)
            else:
                unoDeck.push(temp[0], temp[1])
        print(unoDeck)
        return unoDeck
        

    

deck = Deck(Card)

test = deck.buildDeck
print(deck.getSize())
print(test)