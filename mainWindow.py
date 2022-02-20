from threading import Thread
from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk







import rotateItem
from lableGroupe import VerticalScrolledFrame


class AppMainWindow:
    def __init__(self):
        print("[INFO]: init start...")
        self.__count = 0
        self.tempCount = 1

        self.colorOne = "#FFFFFF"
        self.colorTwo = "#E1E5ED"
        self.colorText = "#4D7992"
        self.colorGreen = "#00ED60"
        self.colorYellow = "#FFB106"
        self.colorRed = "#FF194B"

        self.initWindow()
        #self.insertCount()

        self.itemsList = []

        print("[INFO]: init ending...")


    def initWindow(self):
        self.__width = 1000
        self.__height = 600
        self.startWindow()
        self.createWidgets()
        self.place()

    def getCount(self):
        return self.__count

    def setCount(self, count):
        self.__count = count

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height


    def createWidgets(self):


        self.playIMG = (Image.open("sprites/play.png"))
        self.stopIMG = (Image.open("sprites/stop.png"))
        self.rotateIMG = (Image.open("sprites/rotate.png"))
        self.upIMG = (Image.open("sprites/up.png"))
        self.downIMG = (Image.open("sprites/down.png"))
        self.openIMG = (Image.open("sprites/open.png"))
        self.closeIMG = (Image.open("sprites/close.png"))
        self.startPositionIMG = (Image.open("sprites/standartPosition.png"))

        self.rotateResize = self.rotateIMG.resize((50, 50), Image.ANTIALIAS)
        self.rotate50x50 = ImageTk.PhotoImage(self.rotateResize)

        self.playResize = self.playIMG.resize((50, 50), Image.ANTIALIAS)
        self.play50x50 = ImageTk.PhotoImage(self.playResize)

        self.stopResize = self.stopIMG.resize((50, 50), Image.ANTIALIAS)
        self.stop50x50 = ImageTk.PhotoImage(self.stopResize)



        self.canvas = tk.Canvas(self.window, bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)
        self.canvasFooter = tk.Canvas(self.window,bg=self.colorTwo, relief=tk.FLAT, highlightthickness=0)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TCombobox", relief=tk.FLAT, foreground="#4D7992",
                             background=self.colorTwo, fieldbackground="#27292D", darkcolor="#27292D", lightcolor="#27292D", selectbackground="#27292D", selectforeground="#27292D", bordercolor="#27292D", insertcolor="#27292D", insertwidth="#27292D", arrowsize="#27292D", arrowcolor="#4D7992", )
        self.scrallCanvas = tk.Canvas(self.canvas, relief=tk.FLAT, bg=self.colorTwo, )
        self.scframe = VerticalScrolledFrame(self.scrallCanvas)

        self.createProductButton = tk.Button(self.canvas, relief=tk.FLAT, bg=self.colorTwo, command=self.createProduct, image=self.rotate50x50)

        self.playButton = tk.Button(self.canvasFooter, relief=tk.FLAT, bg=self.colorTwo, image=self.play50x50, command=self.playBtn)

    def place(self):
        self.canvas.place(x=0,y=0,width=self.getWidth(),height=(self.getHeight()//100)*90)
        self.canvasFooter.place(x=0, y=(self.getHeight()//10)*9, width=self.getWidth(), height=self.getHeight()//10)
        self.scrallCanvas.place(x=(self.getWidth()//100)*1, y=(self.getHeight()//100)*10, width=(self.getWidth()//100)*98, height=(self.getHeight()//100)*77)
        self.scframe.place(x=0, y=0, width=(self.getWidth()//100)*98, height=(self.getHeight()//100)*77)

        #self.createProductButton.place(x=(self.getWidth()//100)*1, y=(self.getHeight()//100)*1, width=(self.getWidth()//100)*8, height=(self.getHeight()//100)*8)
        self.playButton.pack()
        self.createProductButton.pack()

    def startWindow(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.getWidth()) + "x" + str(self.getHeight()))
        self.window.title("test")
        #self.window.resizable(False, False)
        self.window["bg"] = self.colorTwo
        self.window.bind('<Escape>', lambda e: self.window.quit())


    def createProduct(self):
        test = rotateItem.widgetGroup(self.scframe.interior, "90")
        self.itemsList.append(test)
        print(self.itemsList)


    def playCommand(self):
        if len(self.itemsList) > 0:
            self.playButton.configure(image=self.stop50x50)

            i = 0
            for item in self.itemsList:
                i = i+1
                item.doSomething(i)

            self.playButton.configure(image=self.play50x50)


        else:
            print("test")

    def playBtn(self):
        self.thread = Thread(target=self.playCommand)



        #self.playCommand()
        self.thread.start()

        #self.thread.join()




    def insertCount(self):
        for i in range(20):
            self.createProduct()