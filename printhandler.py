import time
import getopt
import sys
import getopt

from printrun.printcore import printcore
from serial import SerialException

port = '/dev/tty.usbmodem14101'
baud = 250000

class DefaultUSBHandler:
    def __init__(self, port = None, baud = None):
        self.p = printcore()
        self.port = port
        self.baud = baud

        self.p.loud = True

    def conncet(self, port = None, baud = None):
        if port is not None and baud is not None:
            self.p.connect(port, baud)
            print("connected to printer")
        elif self.port is not None and self.baud is not None:
            self.p.connect(self.port, self.baud)
            print("connected to printer")
        else:
            print("not connected to printer")
    def disconnect(self):
        self.p.disconnect()

    def send(self, t = None):
        if t:
            self.p.send_now(t)
        else:
            print("nothing to send")

    def status(self):
        return (self.p.online)

