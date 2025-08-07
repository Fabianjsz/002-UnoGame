#-------------------------------------------------------------------------------
# Name:         hand.py
# Purpose:      hand class for uno game
#
# Author:       Fabianjsz
#
# Created:      07.08.2025
# Copyright:    (c)  2025
# Licence:
#-------------------------------------------------------------------------------

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
            string = (temp, ")", current.color, current.value, "\n")
            txtAus.insert(END, string)
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
        txtAus.insert(END, "Playing card: ", cardToPlay[0], cardToPlay[1], "\n")
        
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
            txtAus.insert(END, "Card not found in hand", "\n")
            return False
        
    def checkAtributes(self, topOfStack): #//Todo #12 Check if any card in hand can be played
        for cards in range(len(self.list)):
            temp = self.list[cards]
            tempCard = Card(str(temp[0]), str(temp[1]))
            if self.canPlay(topOfStack, tempCard) == True:
                return True
        return False