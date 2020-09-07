from tkinter import *
root = Tk()
root.title("window resizer")
root.geometry("478x267")

def resize():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")
Label(text = "window resize").grid(row=0, column=6)

Label(text = "width", fg = "blue", pady=14).grid(row=1, column=5)
Label(text = "height", fg ="blue", pady=14).grid(row=2, column=5)

width = StringVar()
height = StringVar()

Entry(text=width).grid(row=1, column=6)
Entry(text=height).grid(row=2, column=6)

Button(text = "click me", fg = "blue", command=resize).grid(row=3, column=6)
root.mainloop()
