import time
import getopt
import sys
import getopt

import math

# import custom classes
import point_calc as pc

# main code here
def create(layer, points):

    extrusion_rate = 0.08
    feed_rate = 1500

    gcode = []

    #set layer
    layer_hight = 0.5
    #gcode.append("G92 E0")
    #gcode.append("G1 E-5")
    #gcode.append("G1 Z" + str(layer * layer_hight))

    i = 0
    #gcode.append("G1 Z10")
    gcode.append("G1 Z" + str(layer * layer_hight))
    gcode.append("G1 X" + str(points[0][0]) + " Y" + str(points[0][1]))
    #gcode.append("G1 Z0")
    gcode.append("G92 E0")
    gcode.append("G1 E5 F500")
    while i < len(points) - 1:
        point = points[i]
        point_next = points[(i + 1) % (len(points))]
        x = point_next[0]
        y = point_next[1]
        gcode.append("G92 E0")
        gcode.append(
            "G1 X" + str(x) + 
            " Y" + str(y) + 
            " E" + str(pc.distance(point, point_next) * extrusion_rate) + 
            " F" + str(feed_rate)
        )
        #gcode.append("G1 X" + str(x) + " Y" + str(y) + "F1500")
        i += 1

    gcode.append("G92 E0")
    gcode.append("G1 E-6")

    return gcode

def start():
    
    gcode = []

    gcode.append("G91")
    gcode.append("G1 X0 Y0")
    gcode.append("G1 X100 E25")
    gcode.append("G90")
    gcode.append("G92 E0")
    gcode.append("G1 E-4")

    return gcode

def end():
    
    gcode = []

    gcode.append("G92 E0")
    gcode.append("G91")
    gcode.append("G1 Z10 E-15")
    gcode.append("G90")
    gcode.append("G28 X Y")

    return gcode