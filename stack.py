#-------------------------------------------------------------------------------
# Name:         stack.py
# Purpose:      stack for uno game
#
# Author:       Fabianjsz
#
# Created:      07.08.2025
# Copyright:    (c)  2025
# Licence:
#-------------------------------------------------------------------------------

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
            if temp[0] == "Wild" or temp[0] == "WildDrawFour":
                Deck.pop()
                temp = Deck.peek()
            node = Card(temp[0], temp[1])
            node.next = self.head.next # Make the new node point to the current head
            self.head.next = node #!!! # Update the head to be the new node
            self.size += 1
            Deck.pop()
            return True
        
        else:
            return False