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

#------- variables -------
game = False


cardWidth = 200
cardLength = 300

buttonWirdth = 100
buttonHeight = 50


#------- classes -------

class Card:
    def __init__(self, color:str, value:int, next:Card = None):
        self.next:Card = None
        self.color:str = color
        self.value:int = value


class Deck:
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
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


class Stack:
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
    
    def addCard(self, color:str , value:int): #//TODO #7:
        node = Card(color, value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def peek(self):
        if self.isEmpty():
            return None
        else:
            temp1 = self.head.next.color
            temp2 = self.head.next.value
        return temp1, temp2
    
    def clear(self):
        self.head.next = None
        self.size = 0


class Hand: #// TODO: #5 Create class and linked list Hand
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0
        self.list:list = []

    def getLength(self):
        return self.size
    
    def showHand(self):
        print("Hand:", self.list)
        current = self.head.next
        while current != None:
            print(current.color, current.value)
            current = current.next

    def drawCard(self, deck:Deck, numCards:int):
        for i in range(numCards):
            temp = deck.peek()
            node = Card(temp[0], temp[1])
            if self.head.next == None:
                self.head.next = node
                self.size += 1
                self.list.append(temp)
                deck.pop()
            else:
                current = self.head
                while current.next != None:
                    current = current.next
                current.next = node
                self.size += 1
                self.list.append(temp)
                deck.pop()
            print(self.list)

    def canPlay(self, topOfStack:Card, cardToPlay:Card):
        return str(topOfStack[0]) == str(cardToPlay.color) or int(topOfStack[1]) == int(cardToPlay.value)
    
    def playCard(self, stapel:Stack, card:Card): #//TODO #6: play card also removes card from array
        if self.canPlay(Stapel.peek(), card):
            stapel.addCard(card.value, card.color)
            self.removeCard(card)
            return True
        else:
            return False
    
    def removeCard(self, card:Card):
        current = self.head
        found = False
        while current.next != None and not found:
            if current.next == card:
                found = True
            else:
                current = current.next
        if found:
            current.next = current.next.next
            self.size -= 1
            self.list.remove(card)
        else:
            print("Card not found in hand")
            return False


# Converts array deck into linked list 
# Return Value : unoDeck

def convertDeck():
    arrayDeck = Deck.buildDeck()
    unoDeck = Deck()

    for card in arrayDeck:
        temp = card.split(" ")
        if temp[0] == "Wild" or temp[0] == "WildDrawFour":
            unoDeck.push(temp[0], None)
        else:
            unoDeck.push(temp[0], temp[1])
    return unoDeck


unoDeck = convertDeck() # 108 Uno Karten werden in unoDeck gemischt

Stapel = Stack() # Stapel wird erstellt
Stapel.CreateStack(unoDeck) # Erste Karte wird auf den Stapel gelegt

print("-----------------------------------------------")
print("main function")
def main(game, turn):
    print("unoDeck size: ", unoDeck.getSize(),)
    print("Top of the stack after creating:", Stapel.peek())
    
    handBot = Hand()
    print(handBot.getLength())
    
    handBot.drawCard(unoDeck, 5)
    print(handBot.getLength())
    handBot.showHand()
    
    print(Stapel.peek())
    Stapel.addCard("Rot", 7)
    print("top of the stack after adding card: ", Stapel.peek())
    temp = Stapel.peek()
    print(temp[0], "temp 1: ", temp[1])
    print(Stapel.peek())
    print("Can play card: ", handBot.canPlay(Stapel.peek(), Card("Rot", 5)))
    print("error here?")
    print("playing card: ", handBot.playCard(Stapel, Card("Rot", 5)))
    print("top of the stack after playing card: ", Stapel.peek())
    print("length of hand after playing card: ", handBot.getLength())

    if game == False:
        print("Do you wish to play a game?")
        answer = input(" (y/n) ")
        if answer == "y":
            answer = input("Kopf oder Zahl? (k/z) ")
            coin = random.randint(0,1)
            if coin == 0:
                turn = 0
            else:
                turn = 1
            game = True
            print("Game started")
        else:
            print("Game not started")
    while game == True:
        if turn == 1:
            print("Your turn")
            print("Top of the stack: ", Stapel.peek())
            print("Your hand: ")
            handBot.showHand()
            print("Which card do you want to play?")
            card = input("Enter the color and value of the card you want to play: ")
            card = card.split(" ")
            cardToPlay = Card(card[0], card[1])
            if handBot.playCard(Stapel, cardToPlay):
                print("Card played: ", cardToPlay.color, cardToPlay.value)
                print("Top of the stack: ", Stapel.peek())
                print("Hand length: ", handBot.getLength())
                turn = 0
            else:
                print("You can't play that card. Please try again.")
        break







main(game, None)


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
