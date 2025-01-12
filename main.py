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
    def __init__(self, color:str, value:str, next:Card = None):
        self.next:Card = None
        self.color:str = color
        self.value:str = value
    
    def __str__(self):
        return f"{self.color} {self.value}"
    
    def setColor(self, color:str):
        self.color = color


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
    
    # Build uno deck of 100 cards
    def buildDeck():
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
        
        return deck      


class Stack:
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            temp1 = self.head.next.color
            temp2 = self.head.next.value
        return temp1, temp2

    def push(self, color:str , value:str): #//TODO #7:
        node = Card(color, value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def clear(self):
        self.head.next = None
        self.size = 0

    def changeColor(self, color:str):
        self.head.next.color = color
        return True



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


class Hand: #// TODO: #5 Create class and linked list Hand
    def __init__(self):
        self.head:Card = Card("head", None)
        self.size:int = 0
        self.list:list = []

    def getLength(self):
        return self.size
    
    def checkUno(self):
        if self.size <= 1:
            return False
        else:
            return "UNO - Letzte Karte!"
    
    def showHand(self):
        temp = 1
        current = self.head.next
        while current != None:
            print(temp, ")", current.color, current.value)
            temp = temp + 1
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

    def canPlay(self, topOfStack:Card, cardToPlay:Card):
        stackCard = Card(topOfStack[0], topOfStack[1])
        newCard = Card(cardToPlay.color, cardToPlay.value)

        if newCard.color == "Wild" or newCard.color == "WildDrawFour":
            return True
        elif newCard.color == stackCard.color:
            return True
        elif newCard.value == stackCard.value:
            return True
        

    def playCard(self, stapel:Stack, cardIndex:int): #//TODO #6: play card also removes card from array
        cardToPlay = self.list[int(cardIndex) - 1]
        print("Playing card: ", cardToPlay[0], cardToPlay[1]) #//TODO #12
        
        card = Card(cardToPlay[0], cardToPlay[1])
        if self.canPlay(stapel.peek(), card):
            print("Card can be played")
            stapel.push(card.color, card.value)
            self.removeCard(card.color, card.value)
            for cards in self.list:
                if cards == (card.color, card.value):
                    self.list.remove(cards)
                    print("removed card", card.color, card.value)
            return True
        else:
            return False
    
    def removeCard(self, color:str, value:str): #//TODO #11 remove card also removes card in array
        card = Card(color, value)
        print("inside of removeCard: ", card.color, card.value)
        current = self.head
        found = False
        while current.next != None and not found:
            if current.next.color == card.color and current.next.value == card.value:
                found = True
            else:
                current = current.next
        if found:
            #removing card from linked list
            current.next = current.next.next
            self.size -= 1
            #removing card from array
            temp = (color, value)
            for cards in self.list:
                if cards == temp:
                    self.list.remove(cards)
                    print("removed card in array ", card.color, card.value)
                    break
        
        else:
            print("Card not found in hand")
            return False
        
    def checkAtributes(self, topOfStack): #//Todo #12 Check if any card in hand can be played
        for cards in range(len(self.list)):
            temp = self.list[cards]
            tempCard = Card(str(temp[0]), str(temp[1]))
            if self.canPlay(topOfStack, tempCard) == True:
                return True
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


def preGame():
    answer = input("Do you wish to play a game?: \n(y/n) ")
    if answer == "y":  
        playing = True
        print("Game started")
        return playing
    else:
        print("Fehler! Bitte versuchen Sie es erneut.")
        preGame(playing)

def turn():
    answer = input("Kopf oder Zahl? \n(k/z) ")
    coin = random.randint(0,1) #0 == Kopf, 1 == Zahl
    if coin == 0 and answer == "k":
        return 0 #//TODO #10 #Create turn system
    elif coin == 0 and answer == "z":
        return  1
    elif coin == 1 and answer == "k":
        return  1
    elif coin == 1 and answer == "z":
        return  0
    else:
        print("Fehler! Bitte versuchen Sie es erneut.")
        turn()  

def init():
    pass

def cardEffect(card:Card, handGegner:Hand, unoDeck:Deck, topOfStack:Card):
    if card[1] == "drawTwo":
        handGegner.drawCard(unoDeck, 2)
        print("Cpu zieht 2 karten ", handGegner.getLength())
    elif card[1] == "Reverse":
            return "reverse"
    elif card[0] == "Wild":
        print("farbe der oberen karte: ", topOfStack[0])
        color = input("wähle eine Farbe aus: (b/r/y/g)")
        if color == "b":
            return "Blau"
        elif color == "r":
            return "Rot"
        elif color == "b":
            return "Gelb"
        elif color == "b":
            return "Gruen"

    elif card[0] == "WildDrawFour":
        handGegner.drawCard(unoDeck, 4)
        color = input("wähle eine Farbe aus: (b/r/y/g)")
        if color == "b":
            return "Blau"
        elif color == "r":
            return "Rot"
        elif color == "y":
            return "Gelb"
        elif color == "g":
            return "Gruen"
    else:
        print("Kein Effekt")



print("-----------------------------------------------")
print("main function")

def main(play, turn):
    init() # Initialisierung

    unoDeck = convertDeck() # 108 Uno Karten werden in unoDeck gemischt

    stapel = Stack() # Stapel wird erstellt
    stapel.CreateStack(unoDeck) # Erste Karte wird auf den Stapel gelegt

    handSpielerEins = Hand() # Hand von Spieler wird erstellt
    handSpielerEins.drawCard(unoDeck, 5) # 5 Karten werden gezogen
    
    handSpielerZwei = Hand() # Hand von Bot wird erstellt
    handSpielerZwei.drawCard(unoDeck, 5) # 5 Karten werden gezogen

    # Variables
    playing = play


    while playing:
        if unoDeck.getSize() >= 0:
            if turn == 0:
                print("Spieler 1 ist drann:")
                drawn = False
                print(stapel.peek())
                print("debug: \n ist card playable?\n", handSpielerEins.checkAtributes(stapel.peek()))
                if handSpielerEins.checkAtributes(stapel.peek()) == True:
                    print("Top of the stack: ", stapel.peek())
                    print("Your hand: ")
                    handSpielerEins.showHand()

                    index = input("Enter the index of the card which you'd like to play: ")
                    if handSpielerEins.playCard(stapel, int(index)) == True:
                        print("Karte erfolgreich gespielt.")
                        if handSpielerEins.getLength() == 0:
                            playing = False
                        else:
                            effect = cardEffect(stapel.peek(), handSpielerZwei, unoDeck, stapel.peek())
                            if effect == "reverse":
                                turn = 0
                            elif effect == "Blau":
                                stapel.changeColor("Blau")
                            elif effect == "Rot":
                                stapel.changeColor("Rot")
                            elif effect == "Gelb":
                                stapel.changeColor("Gelb")
                            elif effect == "Gruen":
                                stapel.changeColor("Gruen")
                            print(stapel.peek())
                            turn = turn + 1

                    elif handSpielerEins.playCard(stapel, int(index)) == False:
                        print("du kannst diese karte nicht spielen")
                else:
                    print("Du kannst keine Karte Spielen.")
                    handSpielerEins.drawCard(unoDeck, 1)
                    
                    


            elif turn == 1:
                print("Spieler 2 ist drann:")
                drawn = False
                print(stapel.peek())
                print("debug: \n ist card playable?\n", handSpielerZwei.checkAtributes(stapel.peek()))
                if handSpielerZwei.checkAtributes(stapel.peek()) == True:
                    print("Top of the stack: ", stapel.peek())
                    print("Your hand: ")
                    handSpielerZwei.showHand()

                    index = input("Enter the index of the card which you'd like to play: ")
                    if handSpielerZwei.playCard(stapel, int(index)) == True:
                        print("Karte erfolgreich gespielt.")
                        if handSpielerZwei.getLength() == 0:
                            playing = False
                        else:
                            effect = cardEffect(stapel.peek(), handSpielerEins, unoDeck, stapel.peek())
                            if effect == "reverse":
                                turn = 0
                            elif effect == "Blau":
                                stapel.changeColor("Blau")
                            elif effect == "Rot":
                                stapel.changeColor("Rot")
                            elif effect == "Gelb":
                                stapel.changeColor("Gelb")
                            elif effect == "Gruen":
                                stapel.changeColor("Gruen")
                            print(stapel.peek())
                            turn = turn + 1

                    elif handSpielerZwei.playCard(stapel, int(index)) == False:
                        print("du kannst diese karte nicht spielen")
                else:
                    print("Du kannst keine Karte Spielen.")
                    handSpielerZwei.drawCard(unoDeck, 1)   
    if playing == False:
        if handSpielerEins.size == 0:
            print("Spieler Eins hat gewonnen! ")

        elif handSpielerZwei.size == 0:
            print("Spieler Zwei hat gewonnen! ")


#main(preGame(), turn()) # Hauptfunktion


main(True, 0) # Test aufruf der Hauptfunktion

