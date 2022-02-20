import tkinter as tk
from threading import Thread
from tkinter import messagebox as mb
from time import sleep
import playsound






class widgetGroup:
    def __init__(self, root, name):
        self.__name = name
        self.__root = root

        self.colorOne = "#FFFFFF"
        self.colorTwo = "#E1E5ED"
        self.colorText = "#4D7992"
        self.colorGreen = "#00ED60"
        self.colorYellow = "#FFB106"
        self.colorRed = "#FF194B"

        self.tick1 = r"C:\Users\Dell\Desktop\sound1.mp3"
        self.tick2 = r"C:\Users\Dell\Desktop\sound2.mp3"

        self.createWidjets()
        self.place()



    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getRoot(self):
        return self.__root

    def setRoot(self, value):
        self.__root = value



    def createWidjets(self):
        self.canvas = tk.Canvas(self.getRoot(), bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)
        self.nameLable = tk.Label(self.canvas, text=self.getName(), height=2,)
        self.plusMinusEntry = tk.Entry(self.canvas)
        self.deleteBtn = tk.Button(self.canvas, text=" ⃠ ", command=self.checkClear, height=2, width=5)

    def place(self):
        self.canvas.pack(padx=10, pady=5)
        self.nameLable.pack(side=tk.LEFT, padx=10)
        self.plusMinusEntry.pack(side=tk.LEFT)
        self.deleteBtn.pack(side=tk.LEFT)

    def checkClear(self):
        answer = mb.askyesno(title="answer", message="do you want to delete " + self.getName() + " ?")
        if answer:
            self.clear()


    def clear(self):
        self.canvas.destroy()


    def doSomething(self, count):


        print("rotate start - " + str(count))
        #self.deleteBtn.pack_forget()
        playsound.playsound(self.tick1)
        self.canvas.config(bg=self.colorRed)
        sleep(0.5)
        self.canvas.config(bg=self.colorYellow)

        sleep(0.4)
        self.canvas.config(bg=self.colorGreen)
        playsound.playsound(self.tick2)
        sleep(0.1)

        print("rotate finish - " + str(count))





