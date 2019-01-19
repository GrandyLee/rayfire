from tkinter import *

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

root.title("hahaha")
photo = PhotoImage(file="G://rayfire/images/1png.png")
textLabel = Label(root, text="粉色粉色发热更。\n发生发生的发生，\n真美！",
                  justify=LEFT,
                  image=photo,
                  compound=CENTER,
                  font=("华康少女字体", 20),
                  fg="yellow"
                  )
textLabel.pack(side=LEFT)


# # imageLabel = Label(root, image=photo)
# imageLabel.pack(side=RIGHT)

mainloop()


