import time
import getopt
import sys
import getopt

from printhandler import DefaultUSBHandler

port = '/dev/tty.usbmodem14101'
baud = 250000

print_handler = DefaultUSBHandler(port, baud)
print_handler.conncet()

time.sleep(1)
print(print_handler.status())
print_handler.send("G28")
time.sleep(1)

print_handler.disconnect()