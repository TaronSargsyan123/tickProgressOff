from PIL import Image, ImageTk

playIMG = (Image.open("sprites/play.png"))
stopIMG = (Image.open("sprites/stop.png"))
rotateIMG = (Image.open("sprites/rotate.png"))
upIMG = (Image.open("sprites/up.png"))
downIMG = (Image.open("sprites/down.png"))
openIMG = (Image.open("sprites/open.png"))
closeIMG = (Image.open("sprites/close.png"))
startPositionIMG = (Image.open("sprites/standartPosition.png"))

rotateResize = rotateIMG.resize((50, 50), Image.ANTIALIAS)

newRotate = ImageTk.PhotoImage(rotateResize)

# self.playIMG          = tk.PhotoImage(file=r"sprites/play.png")
# self.stopIMG          = tk.PhotoImage(file=r"sprites/stop.png")
# self.rotateIMG        = tk.PhotoImage(file=r"sprites/rotate.png")
# self.upIMG            = tk.PhotoImage(file=r"sprites/up.png")
# self.downIMG          = tk.PhotoImage(file=r"sprites/down.png")
# self.openIMG          = tk.PhotoImage(file=r"sprites/open.png")
# self.closeIMG         = tk.PhotoImage(file=r"sprites/close.png")
# self.startPositionIMG = tk.PhotoImage(file=r"sprites/standartPosition.png")