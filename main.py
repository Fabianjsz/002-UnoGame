#-------------------------------------------------------------------------------
# Name:         File1.py
# Purpose:
#
# Author:
#
# Created:      09.12.2024
# Copyright:    (c)  2024
# Licence:
#-------------------------------------------------------------------------------
from __future__ import annotations
from tkinter import *


class Karte:
    def __init__(self, value:int, color:str):
        self.__value:int = value 
        self.__color:str = color
        self.__next = None

class Deck:
    def __init__(self):
        self.__head = Karte("head")
        self.__size:int = 0

    