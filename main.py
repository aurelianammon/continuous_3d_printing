import time
import threading
import getopt
import sys
import getopt

from printhandler import DefaultUSBHandler
import slicer_test as shape

# gui
import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button

port = '/dev/tty.usbmodem14101'
baud = 250000

# connect to printer
print_handler = DefaultUSBHandler(port, baud)

#print_handler.conncet()
#while not print_handler.p.online:
#    time.sleep(0.1)

#print(print_handler.status())

#reset printer postition ans setting
def printer_setup():
    print_handler.send(["G90", "M104 S200", "G28"])
    while print_handler.is_printing():
        root.update()
        time.sleep(0.1)

def printer_up():
    print_handler.send(["G1 Z10"])
    while print_handler.is_printing():
        time.sleep(0.1)

def printer_down():
    print_handler.send(["G91", "G1 E10", "G90"])
    while print_handler.is_printing():
        time.sleep(0.1)

def printer_pause_resume():
    print_handler.pause()

def start_print():
    print_handler.send(["G1 Z10", "G1 X0 Y0"])
    while print_handler.is_printing():
        time.sleep(0.1)

    i = 0
    while i < 90:
        gcode = shape.create(i)
        print_handler.send(gcode)
        while print_handler.p.printing:
            root.update()
        i = i + 10

# disconnect from printer
#print_handler.disconnect()

class MainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Streamline")
        master.geometry('300x500')
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.button_connect = Button(text="Connect", command=print_handler.connect)
        self.button_connect.pack(fill='x')

        self.button_disconnect = Button(text="Disconnect", command=print_handler.disconnect)
        self.button_disconnect.pack(fill='x')

        self.button_setup = Button(text="Setup", command=printer_setup)
        self.button_setup.pack(fill='x')

        self.button_up = Button(text="Up", command=printer_up)
        self.button_up.pack(fill='x')

        self.button_down = Button(text="Down", command=printer_down)
        self.button_down.pack(fill='x')

        self.button_print = Button(text="Print", command=start_print)
        self.button_print.pack(fill='x')

        self.button_pause = Button(text="Pause", command=printer_pause_resume)
        self.button_pause.pack(fill='x', side='left')

        # lable test
        self.label_a = tk.Label(text="Printer online:")
        self.label_a.pack(side='left')

        self.label = tk.Label(text=str(print_handler.p.online))
        self.label.pack(side='right')

        self.master.after(50, self.update_stats)

    def update_stats(self):

        self.label.configure(text=str(print_handler.p.online))

        self.master.after(50, self.update_stats)

    def on_closing(self):
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
            #print_handler.disconnect()
            #window.destroy()
        print_handler.disconnect()
        self.master.destroy()


root = tk.Tk()
my_gui = MainGUI(root)
root.mainloop()



