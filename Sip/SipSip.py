from tkinter import*
root = Tk()
import random

from PIL import ImageTk,Image

root.title("Title 321th time")

root.geometry("1000x1000")

root.configure(background = "yellow")
img1 = ImageTk.PhotoImage(Image.open("download1.png"))
img2 = ImageTk.PhotoImage(Image.open("download2.png"))
img3 = ImageTk.PhotoImage(Image.open("download3.png"))
img4 = ImageTk.PhotoImage(Image.open("download4.png"))
img5 = ImageTk.PhotoImage(Image.open("download5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("download6.jpg"))
img7 = ImageTk.PhotoImage(Image.open("download7.png"))
img8 = ImageTk.PhotoImage(Image.open("download8.png"))
img9 = ImageTk.PhotoImage(Image.open("download9.jpg"))
img10 = ImageTk.PhotoImage(Image.open("download10.png"))
img11 = ImageTk.PhotoImage(Image.open("download11.jpg"))
img12 = ImageTk.PhotoImage(Image.open("download12.jpg"))
images = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12]

q1 = Label(root,bg = "light blue",text = "Player 1",fg = "black")

q2 = Label(root,bg = "light blue",text = "Player 2",fg = "black")





B3  = Button(root)


p1s = 0
p2s = 0

def w():
    global p1s
    r = random.randint(0, 11)
    pointy =images[r]
    B3["image"] = pointy

B1 = Button(root,text = "Player 1",command = w)
B2 = Button(root,text = "Player 2",command = w)

B1.place(relx = 0.2,rely = 0.7,anchor = CENTER)
B2.place(relx = 0.8,rely = 0.7,anchor = CENTER)
B3.place(relx = 0.5,rely = 0.7,anchor = CENTER)

q1.place(relx = 0.2,rely = 0.3,anchor = CENTER)
q2.place(relx = 0.8,rely = 0.3,anchor = CENTER)



root.mainloop()

