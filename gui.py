import tkinter as tk
from tkmacosx import Button

def test():
	print("hello")

window = tk.Tk(className="Streamline")
window.geometry("500x200")
button = Button(text="Click me!", command=test)
button.pack()


window.mainloop()