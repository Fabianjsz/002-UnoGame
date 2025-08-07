#-------------------------------------------------------------------------------
# Name:         card.py
# Purpose:      class card used by deck class
#
# Author:       Fabianjsz
#
# Created:      07.08.2025
# Copyright:    (c)  2025
# Licence:
#-------------------------------------------------------------------------------

class Card:
    def __init__(self, color:str, value:str, next):
        self.next:Card = None
        self.color:str = color
        self.value:str = value
    
    def getCard(self):
        return f"{self.color} {self.value}"
    
    def setColor(self, color:str):
        self.color = color
