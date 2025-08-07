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
import tkinter.scrolledtext as st
import random

#------- variables -------

game = False
index = None


# ----- Functions -----
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
        txtAus.insert(END, "Cpu zieht 2 karten ", handGegner.getLength(), "\n")
    elif card[1] == "Reverse":
            return "reverse"
    elif card[0] == "Wild":
        txtAus.insert(END, "farbe der oberen karte: ", topOfStack[0], "\n")
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
        txtAus.insert(END, "Kein Effekt", "\n")

def labelUpdate(topOfStack:Card, label:Label):
    if topOfStack[0] == "Gelb":
        label.config(bg="yellow", fg="black")
    elif topOfStack[0] == "Blau":
        label.config(bg= "blue")
    elif topOfStack[0] == "Rot":
        label.config(bg="red")
    elif topOfStack[0] == "Gruen":
        label.config(bg="green")
    elif topOfStack[0] == "Wild":
        label.config(bg="black", text="Wild")
    elif topOfStack[0] == "WilfDrawFour":
        label.config(bg= "black",text="+4")
    if topOfStack[1] == "DrawTwo":
        label.config(text="+2")
    elif topOfStack[1] == "Reverse":
        label.config(text="Reverse")
    



def enter():
    global index
    index = entry.get()
    print(index)

    entry.delete(0, END)

    print(index)
    pass

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
                txtAus.insert(END, "Spieler 1 ist drann:\n")
                labelUpdate(stapel.peek(), topCard)
                drawn = False
                print("debug: \n ist card playable?\n", handSpielerEins.checkAtributes(stapel.peek()))
                if handSpielerEins.checkAtributes(stapel.peek()) == True:
                    #txtAus.insert(END, "Top of the stack: \n", stapel.peek())
                    txtAus.insert(END, "Your hand:\n")
                    handSpielerEins.showHand()

                    index = input("Enter the index of the card which you'd like to play: ")
                    if handSpielerEins.playCard(stapel, int(index)) == True:
                        txtAus.insert(END, "Karte erfolgreich gespielt.", "\n")
                        labelUpdate(stapel.peek(), topCard)
                        if handSpielerEins.getLength() == 0:
                            playing = False
                        else:
                            effect = cardEffect(stapel.peek(), handSpielerZwei, unoDeck, stapel.peek())
                            #print(effect)
                            labelUpdate(stapel.peek(), topCard)
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
                            #print(stapel.peek())
                            labelUpdate(stapel.peek(), topCard)
                            if effect != "reverse":
                                #//clear
                                turn = turn + 1

                    elif handSpielerEins.playCard(stapel, int(index)) == False:
                        #//clear
                        txtAus.insert(END, "du kannst diese karte nicht spielen\n")
                else:
                    #//clear
                    txtAus.insert(END, "Du kannst keine Karte Spielen.\n")
                    handSpielerEins.drawCard(unoDeck, 1)
                    
                    


            elif turn == 1:
                txtAus.insert(END, "Spieler 2 ist drann:","\n")
                labelUpdate(stapel.peek(), topCard)
                drawn = False
                
                print("debug: \n ist card playable?\n", handSpielerZwei.checkAtributes(stapel.peek()))
                if handSpielerZwei.checkAtributes(stapel.peek()) == True:
                    #txtAus.insert(END, "Top of the stack: ", stapel.peek(), "\n")
                    txtAus.insert(END, "Your hand:\n")
                    handSpielerZwei.showHand()

                    index = input("Enter the index of the card which you'd like to play: ")
                    if handSpielerZwei.playCard(stapel, int(index)) == True:
                        txtAus.insert(END, "Karte erfolgreich gespielt.", "\n")
                        labelUpdate(stapel.peek(), topCard)
                        if handSpielerZwei.getLength() == 0:
                            playing = False
                        else:
                            effect = cardEffect(stapel.peek(), handSpielerEins, unoDeck, stapel.peek())
                            if effect == "reverse":
                                turn = 1
                            elif effect == "Blau":
                                stapel.changeColor("Blau")
                            elif effect == "Rot":
                                stapel.changeColor("Rot")
                            elif effect == "Gelb":
                                stapel.changeColor("Gelb")
                            elif effect == "Gruen":
                                stapel.changeColor("Gruen")
                            #print(stapel.peek())
                            if effect != "reverse":
                                turn = turn - 1
                            labelUpdate(stapel.peek(), topCard)

                    elif handSpielerZwei.playCard(stapel, int(index)) == False:
                        txtAus.insert(END, "du kannst diese karte nicht spielen", "\n")
                else:
                    txtAus.insert(END, "Du kannst keine Karte Spielen.", "\n")
                    handSpielerZwei.drawCard(unoDeck, 1)   
    if playing == False:
        if handSpielerEins.size == 0:
            #//clear
            txtAus.insert(END, "Spieler Eins hat gewonnen!\n")
        elif handSpielerZwei.size == 0:
            #//clear
            txtAus.insert(END, "Spieler Zwei hat gewonnen!\n ")

# ----- GUI -----

#Fenster
fenster = Tk()
fenster.geometry("1000x500")
fenster.title("UNO CARD DUELL")
fenster.configure(bg="white")





#current Card
topCard = Label(fenster)
topCard.place(x=700, y=50, width=250, height=400)
topCard.config(bg="grey", fg="white", text="UNO")



# Textreturn
txtAus = st.ScrolledText(fenster, width=500, height=300, bg="lightgrey", fg="black", font=("Times New Roman", 15))
txtAus.place(x=50, y=50, width=500, height=300)

# Entry for indexing
entry = Entry(fenster, bg="white", fg="black")
entry.place(x= 200, y=400, width=200, height=50)

def test():
    txtAus.insert(END, "Hello world\n")
    txtAus.delete("1.0", END)

# Buttons

enter = Button(fenster, text="Bestaetigen", command=test)
enter.place(x=50, y= 400, width=100, height=50)



#main(preGame(), turn()) # Hauptfunktion


main(True, 0) # Test aufruf der Hauptfunktion

