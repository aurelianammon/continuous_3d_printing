import time
import getopt
import sys
import getopt

from printrun.printcore import printcore
from printrun import gcoder
from serial import SerialException

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
            print("connected to " + self.port)
        else:
            print("not connected to printer")
    def disconnect(self):
        self.p.disconnect()
        print("disconnceted from " + self.port)

    def send_now(self, t = None):
        if t:
            self.p.send_now(t)
        else:
            print("nothing to send")

    def send(self, t = None):
        if t:
            self.p.startprint(gcoder.LightGCode([t]))
        else:
            print("nothing to send")

    def status(self):
        return ("online: " + str(self.p.online) + ", printing: " + str(self.p.printing))

