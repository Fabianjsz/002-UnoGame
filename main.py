#-------------------------------------------------------------------------------
# Name:         main.py
# Purpose:      main logic for Uno Game in python
#
# Author:       Fabianjsz
#
# Created:      09.12.2024
# Copyright:    (c)  2024
# Licence:
#-------------------------------------------------------------------------------
from __future__ import annotations
from tkinter import *
import random

unoDeck = None

class Card:
    def __init__(self, value:int, color:str, next:Card = None):
        self.next:Card = None
        self.value:int = value
        self.color:str = color

class Deck:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Card("head",None, None)
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
            temp1 = self.head.next.value
            temp2 = self.head.next.color
        return temp1, temp2

    # Push a value into the stack.
    def push(self, value, color):
        node = Card(value, color)
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
        
        return remove.value, remove.color
    
    # Build uno deck of 108 cards
    def buildDeck():
        deck = []
        
        #Define the card colors and values
        colors = ["Rot", "Gruen", "Gelb", "Blau"]
        values = [0,1,2,3,4,5,6,7,8,9, "drawTwo", "Skip", "Reverse"]
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
            randPos = random.randint(0,107)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
        
        return deck            

def convertDeck():
    arrayDeck = Deck.buildDeck()
    unoDeck = Deck()

    for card in arrayDeck:
        temp = card.split(" ")
        print(temp)
        if temp[0] == "Wild" or temp[0] == "WildDrawFour":
            unoDeck.push(temp[0], None)
        else:
            unoDeck.push(temp[0], temp[1])
    return unoDeck


class stack:
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0

    def push(self, value:int, color:str):
        node = Card(value, color)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def peek(self):
        if self.isEmpty():
            return None
        else:
            temp1 = self.head.next.value
            temp2 = self.head.next.color
        return temp1, temp2
    
    def clear(self):
        self.head.next = None
        self.size = 0

unoDeck = convertDeck()


class Hand: #// TODO: #5 Create class and linked list cpuHand
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0

    def drawCard(self, deck:Deck, numCards:int):
        print("drawwind Card")
        for i in range(numCards):
            print("inside loop ")
            print("peeking deck")
            temp = unoDeck.peek()
            print("adding card to hand")
            node = Card(temp[0], temp[1])
            node.next = self.head.next
            self.head.next = node
            self.size += 1
            unoDeck.pop()

    def getLength(self):
        return self.size
    
    def showHand(self):
        temp = self.head.next
        while temp != None:
            print(temp.value, temp.color)
            temp = temp.next



print("-----------------------------------------------")
print("main function")
def main():

    print("-----------------")
    print("Displaying the stack")
    print("Deck in stacked linear list form:")
    print(unoDeck.getSize())

    print("\nTop of the stack (peek):", unoDeck.peek())
    print("\nLength of the stack(lenght):", unoDeck.getSize())
    print("Popping the top card:", unoDeck.pop())
    print("length of the stack post pop:", unoDeck.getSize())
    print("Top of the stack after popping:", unoDeck.peek())


    handBot = Hand()
    print(handBot.getLength())
    print(unoDeck.peek())

    #error here //TODO #6:
    handBot.drawCard(unoDeck, 5)
    print(handBot.getLength())
    print(handBot.showHand())


main()
