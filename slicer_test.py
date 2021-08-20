import time
import getopt
import sys
import getopt

import numpy as np
import math

# import custom classes
import point_calc as pc

# main code here
def create(factor):
    diameter = 50
    number_of_points = 4
    center = pc.point(50, 50, 0)
    radius = math.sqrt(pow(diameter, 2) + pow(diameter, 2)) / 2
    rotation = math.pi / number_of_points + math.pi / 180 * factor
    extrusion_rate = 2

    points = []
    gcode = []

    i = 0
    while i < number_of_points:
        x = center[0] + radius * math.cos(2 * math.pi * i / number_of_points + rotation)
        y = center[1] + radius * math.sin(2 * math.pi * i / number_of_points + rotation)
        z = 0
        points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))
        i += 1

    i = 0
    gcode.append("G1 Z10")
    gcode.append("G1 X" + str(points[0][0]) + " Y" + str(points[0][1]))
    gcode.append("G1 Z0")
    while i < len(points):
        point = points[i]
        point_next = points[(i + 1) % (len(points))]
        x = point_next[0]
        y = point_next[1]
        gcode.append("G92 E0")
        gcode.append(
            "G1 X" + str(x) + 
            " Y" + str(y) + 
            " Z" + str(0.1 * factor) + 
            " E" + str(pc.distance(point, point_next) * extrusion_rate)
        )
        #gcode.append("G1 X" + str(x) + " Y" + str(y))
        i += 1

    return gcode