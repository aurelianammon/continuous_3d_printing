import time
import threading
import getopt
import sys
import getopt

from printhandler import DefaultUSBHandler
import slicer_test as shape

# gui
import tkinter as tk
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
    print_handler.send_now("G90")
    print_handler.send("G28")
    while print_handler.p.printing:
        time.sleep(0.1)
# print_handler.send("G1 E100 F100")
# while print_handler.p.printing:
#     time.sleep(0.1)

def printer_up():
    print_handler.send("G1 Z5")
    while print_handler.p.printing:
        time.sleep(0.1)

def printer_down():
    print_handler.send("G1 Z0")
    while print_handler.p.printing:
        time.sleep(0.1)

def send_gcode():
    i = 0
    while i < 90:
        gcode = shape.create(i)

        for line in gcode:
            print_handler.send(line)
            while print_handler.p.printing:
                time.sleep(0.1)

        i = i + 10

def start_print():

    thread = threading.Thread(target=send_gcode)
    thread.start()

    # wait here for the result to be available before continuing
    thread.join()

    print_handler.send("G1 Z10")
    while print_handler.p.printing:
        time.sleep(0.1)

    print_handler.send("G1 X0 Y0")
    while print_handler.p.printing:
        time.sleep(0.1)

# disconnect from printer
#print_handler.disconnect()


window = tk.Tk(className="Streamline")
window.geometry("500x200")
button_connect = Button(text="Connect", command=print_handler.conncet)
button_connect.pack()
button_disconnect = Button(text="Disconnect", command=print_handler.disconnect)
button_disconnect.pack()
button_setup = Button(text="Setup", command=printer_setup)
button_setup.pack()
button_up = Button(text="Up", command=printer_up)
button_up.pack()
button_down = Button(text="Down", command=printer_down)
button_down.pack()
button_print = Button(text="Print", command=start_print)
button_print.pack()
window.mainloop()



