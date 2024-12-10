#-------------------------------------------------------------------------------
# Name:         main.py
# Purpose:
#
# Author:       Fabianjsz
#
# Created:      09.12.2024
# Copyright:    (c)  2024
# Licence:
#-------------------------------------------------------------------------------
from __future__ import annotations
from tkinter import *


class Card:
    def __init__(self, value:int, color:str):
        self.__value:int = value 
        self.__color:str = color
        self.__next: = None

class Deck: #Stack //TODO #1 Stack

    # Initializing a stack
    def __init__(self):
        self.__head = Card("head")
        self.__size:int = 0

    # String represantation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
    
    # Get the current size of the stack
    def getSize(self):
        return self.__size
    
    # Check if the Stack is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the top item of the stack
    def peek(self):

        #Check if we are peeking an empty stack
        if self.isEmpty():
            return None
        
        return self.head.next.value
    
    # Push a value into the stack.
    def push(self, )

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = remove.next 
        self.size -= 1
        return remove.value
    
    







class Hand: #//TODO #2 Create Class and linked list Hand
    def __init__(self):
        self.__head = Card("head")
        self.__size:int = 0
        self.__

