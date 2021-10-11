import tkinter as tk

class App:
    def __init__(self, root):
        #setting title
        root.title("streamline")
        #setting window size
        #root.geometry('200x300')

        label = tk.Label(text="hello, I am here to show something").grid(row=0, columnspan=10)
        button = tk.Button(text="hello").grid(row=1, column=0)
        button = tk.Button(text="hello").grid(row=2, column=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()