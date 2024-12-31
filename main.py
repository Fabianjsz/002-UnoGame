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

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def CreateStack(self, Deck:Deck):
        if self.isEmpty():
            temp = Deck.peek()
            node = Card(temp[0], temp[1])
            node.next = self.head.next # Make the new node point to the current head
            self.head.next = node #!!! # Update the head to be the new node
            self.size += 1
            Deck.pop()
            return True
        
        else:
            return False


    def addCard(self, value:int, color:str): #//TODO #7:
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

Stapel = stack()
Stapel.CreateStack(unoDeck)

class Hand: #// TODO: #5 Create class and linked list Hand
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0

    def getLength(self):
        return self.size
    
    def showHand(self):
        current = self.head.next
        while current != None:
            print(current.value, current.color)
            current = current.next

    def drawCard(self, deck:Deck, numCards:int):
        for i in range(numCards):
            temp = unoDeck.peek()
            node = Card(temp[0], temp[1])
            node.next = self.head.next
            self.head.next = node
            self.size += 1
            unoDeck.pop()

    def canPlay(self, topCard:Card, cardToPlay:Card):
        temp = Stapel.peek()
        return temp[0] == cardToPlay.color or temp[1] == cardToPlay.value
    
    def playCard(self, card:Card, cardToPlay:Card):
        if self.canPlay(Stapel.peek(), card):
            stack.addCard(card.value, card.color)
            self.removeCard(card)
            return True
        else:
            return False




print("-----------------------------------------------")
print("main function")
def main():
    print("unoDeck size: ", unoDeck.getSize(),)
    print("Top of the stack after creating:", Stapel.peek())
    
    handBot = Hand()
    print(handBot.getLength())
    handBot.drawCard(unoDeck, 5)
    print(handBot.getLength())
    handBot.showHand()
    
    print(Stapel.peek())
    cardToPlay = Card("Rot", 5)
    print("Can play card: ", handBot.canPlay(Stapel.peek(), cardToPlay))
    if handBot.playCard(handBot.head.next, cardToPlay):
        print("Card played successfully")
    else:
        print("Card can't be played")





main()


"""
example driver code
    print("Stapel wurde erstellt", "\n")
    print("\nTop of the stack (peek):", unoDeck.peek())
    print("\nLength of the stack(lenght):", unoDeck.getSize())
    print("Popping the top card:", unoDeck.pop())
    print("length of the stack post pop:", unoDeck.getSize())
    print("Top of the stack after popping:", unoDeck.peek())




    handBot.drawCard(unoDeck, 5)
    print("Anzahl der Karten in der Hand von Bot post draw: ", handBot.getLength())
    print("-----------------------------------------------")
    print(handBot.showHand())
    print("-----------------------------------------------")
    handBot.playCard(handBot.head.next)
    print(handBot.showHand())
    print(Stapel.peek())
"""