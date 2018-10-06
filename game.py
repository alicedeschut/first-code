from tkinter import *
import tkinter as tk
import random

def bulgpatiens(number):
    """Nytt spelfönster"""
    rootbulg = Tk()
    rootbulg.geometry("700x700")
    rootbulg.title("Bulgarisk Patiens, spelet")
    stacklist = []
    repetitionlist = [0]
    utlist = []
    inteutlist = []

    def delauppkort(antal, choice):
            """Här delar jag upp korten i olika stacks"""
            stack = 0
            del stacklist[:]
            variable = int(antal)
            while 1 == 1:
                if choice == 1:
                    stack = random.randint(1, variable)
                else:
                    stack = random.randint(1, 5)
                stacklist.append(stack)
                if sum(stacklist) > int(antal):
                    stacklist.pop()
                if sum(stacklist) < int(antal):
                    variable = int(antal) - stack
                else:
                    break

    def allt(choice):
        """här tar jag bort ett kort från varje stack. Sedan lägger jag till de korten till en ny stack.
        Och efter det så tar jag bort alla nollor som finns i listan.
        det sista jag gör är att sätta listan (stacklist) i en annan lista (repetitionslista)"""
        n = 0
        lenstacklist = len(stacklist)
        while lenstacklist > n:
            cardstack = stacklist[n]
            cardstack = cardstack - 1
            stacklist[n] = cardstack
            n = n + 1
        lenstacklist = len(stacklist)
        stacklist.append(lenstacklist)
        while True:
            try:
                stacklist.remove(0)
            except:
                break
        stacklist.sort()
        repetitionlist.append(tuple(stacklist))

    def repetition(choice):
        """Här repeterar jag stegen tills patiensen går ut/max 25 steg/cykel"""
        m = 1
        while True:
            if m == 25:
                while True:
                    try:
                        repetitionlist.remove(0)
                    except:
                        break
                stegen = '\n'.join(map(str, repetitionlist))
                label3['text'] = stegen
                label4['text'] = "Patiensen har inte gått ut... tyvärr"
                break
            else:
                i = 0
                while i < m:
                    if repetitionlist[i] == repetitionlist[m]:
                        if i == m - 1:
                            if choice == 1:
                                while True:
                                    try:
                                        repetitionlist.remove(0)
                                    except:
                                        break
                                stegen = '\n'.join(map(str, repetitionlist))
                                label3['text'] = stegen
                                label4['text'] = "Patiensen har gått ut!"
                                return
                            else:
                                utlist.append(1)
                                return
                        else:
                            if choice == 1:
                                while True:
                                    try:
                                        repetitionlist.remove(0)
                                    except:
                                        break
                                stegen = '\n'.join(map(str, repetitionlist))
                                label3['text'] = stegen
                                label4['text'] = "Patiensen har inte gått ut... tyvärr. En cykel uppstår."
                                return
                            else:
                                inteutlist.append(1)
                                return
                    else:
                        i = i + 1
                        continue
                allt(choice)
                m = m + 1

    def statistik():
        """Här börjar statistik spelet"""
        antalpatienser = entry1.get()
        label1['text'] = "Du har valt att se statistik på " + antalpatienser + " patienser."
        stack = 0
        choice = 2
        upprepning = 0

        while upprepning < int(antalpatienser):
            antal = random.randint(0,10)
            delauppkort(antal, choice)
            allt(choice)
            repetition(choice)
            del repetitionlist[:]
            repetitionlist.append(0)
            upprepning += 1

        label2['text'] = "Vi har gjort statistik på " + str(antalpatienser) + " patienser."
        label3['text'] = str(len(utlist)) + " patiens(er) gick ut. " + str(len(inteutlist)) + " patiens(er) gick inte ut."
        del utlist[:]
        del inteutlist[:]

    def enter():
        """Här börjar bulgarisk patiens spelet"""
        antal = entry1.get()
        label1['text'] = "Du har valt att spela med " + antal + " kort."

        try:
            antal = int(antal)
            if antal >= 2 and antal <= 52:
                choice = 1
                delauppkort(antal, choice)
                label2['text'] = "Vi har delat upp korten i " + str(len(stacklist)) + " hög(ar). Så ser det ut:\n" + str(stacklist) + "\n Nu börjar spelet!"
                allt(choice)
                repetition(choice)
            else:
                try:
                    label3['text'] = ""
                    label4['text'] = ""
                except:
                    pass
                label2['text'] = "Fel antal kort. Försök igen"

        except ValueError:
            try:
                label3['text'] = ""
                label4['text'] = ""
            except:
                pass
            label2['text'] = "Fel antal kort. Inte ett heltal. Försök igen"
        del repetitionlist[:]
        repetitionlist.append(0)

    if number == 1:
        label1 = Label(rootbulg, text="Okej!\nHur många kort vill du spela med? (du får välja mellan 2 och 52)")
        entry1 = Entry(rootbulg, width=10)
        entrybutton1 = Button(rootbulg, text="Enter", command=enter)
        label1.pack()
        entry1.pack()
        entrybutton1.pack()
    else:
        label1 = Label(rootbulg, text="Okej!\nVilket antal patienser vill du se statistik på?")
        entry1 = Entry(rootbulg, width=10)
        entrybutton1 = Button(rootbulg, text="Enter", command=statistik)
        label1.pack()
        entry1.pack()
        entrybutton1.pack()

    label2 = Label(rootbulg, text="")
    label3 = Label(rootbulg, text ="")
    label4 = Label(rootbulg, text="")
    label5 = Label(rootbulg, text="")

    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()

    rootbulg.mainloop()

def menu():
    """Det här är min meny"""
    root = Tk()
    root.geometry("300x300")
    root.title("Bulgarisk Patiens")

    mLabel = Label(root, text="Vad vill du göra?")
    button1 = Button(root, text="Se utlägg av en patiens.", command=lambda:bulgpatiens(1))
    button2 = Button(root, text="Se statistik på valt antal patienser.", command=lambda:bulgpatiens(2))
    button3 = Button(root, text="Avsluta", command=lambda:root.destroy())

    mLabel.pack()
    button1.pack()
    button2.pack()
    button3.pack()

    root.mainloop()

menu()

