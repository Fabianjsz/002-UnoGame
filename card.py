#-------------------------------------------------------------------------------
# Name:         card.py
# Purpose:      card class
#
# Author:       Fabianjsz
#
# Created:      07.08.2025
# Copyright:    (c)  2025
# Licence:
#-------------------------------------------------------------------------------

class Card:
    def __init__(self, color:str, value:str, next = None):
        self.next:Card
        self.color:str = color
        self.value:str = value
    
    def getCard(self):
        return f"{self.color} {self.value}"
    
    def setColor(self, color:str):
        self.color = color