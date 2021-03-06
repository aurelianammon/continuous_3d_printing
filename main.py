import time
import threading
import getopt
import sys
import getopt
import random

from printhandler import DefaultUSBHandler
#import slicer_test as shape
import shapehandler
import slicerhandler

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
    print_handler.send(["G90", "M104 S210", "G28", "G91", "G1 Z10", "G90" ])
    #print_handler.send(["G90", "G28"])
    while print_handler.is_printing():
        root.update()
        time.sleep(0.1)

def printer_up():
    print_handler.send(["G91", "G1 Z10", "G90"])
    while print_handler.is_printing():
        time.sleep(0.1)

def printer_down():
    print_handler.send(["G91", "G1 Z-10", "G90"])
    while print_handler.is_printing():
        time.sleep(0.1)

def printer_pause_resume():
    if print_handler.is_printing():
        print_handler.pause()
    elif print_handler.is_paused():
        print_handler.resume()

def printer_extrude():
    print_handler.send(["G92 E0", "G1 E2 F100"])
    while print_handler.is_printing():
        time.sleep(0.1)

def zero_layer():
    app.layer.set(0)
    print("layer set to O")

def start_print():
    print_handler.send(slicerhandler.start())
    while print_handler.is_printing():
        time.sleep(0.1)

    angle = 0
    next_iteration = app.layer.get() + 50
    while app.layer.get() < next_iteration:
        #gcode = slicerhandler.create(i, shapehandler.create_test(0.5 * i))

        wobbler = 15
        angle = angle + random.randint(-wobbler, wobbler)
        print("angle = " + str(angle))

        # create the shape points
        points = shapehandler.create_stepover(angle, 6)
        points = shapehandler.toolpath(points, "SAW")

        repetitions = 2
        for i in range(repetitions):
            # create gcode from points
            gcode = slicerhandler.create(app.layer.get(), points)
            print_handler.send(gcode)
            while (print_handler.is_printing() or print_handler.is_paused()):
                root.update()
                time.sleep(0.1)
                #print(print_handler.status())
            # update layer hight
            app.layer.set(app.layer.get() + 1)
        
    
    print_handler.send(slicerhandler.end())

# disconnect from printer
# print_handler.disconnect()

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

        self.button_extrude = Button(text="Extrude", command=printer_extrude)
        self.button_extrude.pack(fill='x')

        self.button_pause = Button(text="Pause", command=printer_pause_resume)
        self.button_pause.pack(fill='x')

        self.button_pause = Button(text="Zeroing", command=zero_layer)
        self.button_pause.pack(fill='x')

        self.layer = tk.IntVar()

        self.entry = tk.Entry(textvariable=self.layer)
        self.entry.pack(fill='x')

        # Bind the entrybox to the Return key
        self.entry.bind("<Return>", self.click)

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

    def click(self, event):
        print(self.layer.get())


root = tk.Tk()
app = MainGUI(root)
root.mainloop()



