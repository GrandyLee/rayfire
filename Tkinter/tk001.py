from tkinter import *


def callback():
    var.set("吹吧，我才不信呢！")


root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("点击按钮看看有什么变化！")
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="G:/rayfire//images/1png.png")
imageLabel = Label(frame1, image=photo)  # , height=40, width=40
imageLabel.pack()

theButton = Button(frame2, text="我已经点了！", command=callback)

theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()
