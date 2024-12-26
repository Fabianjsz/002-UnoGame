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

class Card:
    def __init__(self, value:int, color:str):
        self.next:Card = None
        self.value:int = value
        self.color:str = color

class Deck:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Card("head",None)
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

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

        return self.head.next.value

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
        return remove.value
    
    """
    Generate UNO deck of 108 cards
    """
    def buildDeck(): #//TODO #4 Create a Funktion for generating uno Deck
        deck = []
        colors = ["Rot", "Gruen", "Gelb", "Blau"]
        values = [0,1,2,3,4,5,6,7,8,9, "Ziehe Zwei", "Skip", "Reverse"]
        wilds = ["Wild", "Wild Ziehe Vier"]
        for color in colors:
            for value in values:
                cardVal = "{} {}".format(color, value)
                deck.append(cardVal)
                if value != 0:
                    deck.append(cardVal)
        for i in range(4):
            deck.append(wilds[0])
            deck.append(wilds[1])
        for cardPos in range(len(deck)):
            randPos = random.randint(0,107)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
        return deck            

class stack:
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0

class cpuHand: #//TODO #3 Create Class and linked list hand
    def __init__(self):
        self.head:Card = Card("head", None)


class playerHand: #//TODO #2 Create Class and linked list Hand
    def __init__(self):
        self.head:Card = Card("head", None)



# Driver Code
if __name__ == "__main__":
    stack = Deck()
    for i in range(1, 11):
        stack.push(i,"")
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        top_value = stack.pop()
        print(f"Pop: {top_value}") # variable name changed
    print(f"Stack: {stack}")


Karte = Deck
print(Karte.buildDeck())
