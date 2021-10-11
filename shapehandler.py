import time
import getopt
import sys
import getopt

import math

# import custom classes
import point_calc as pc

# default test shape
def create_test(factor = 0):
    diameter = 50
    number_of_points = 4
    center = pc.point(50, 50, 0)
    radius = math.sqrt(pow(diameter, 2) + pow(diameter, 2)) / 2
    rotation = math.pi / number_of_points + math.pi / 180 * factor

    points = []

    i = 0
    while i < number_of_points:
        x = center[0] + radius * math.cos(2 * math.pi * i / number_of_points + rotation)
        y = center[1] + radius * math.sin(2 * math.pi * i / number_of_points + rotation)
        z = 0
        points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))
        i += 1

    return points

# stepover test shape
def create_stepover(factor = 0):
    diameter = 50
    number_of_points = 4
    center = pc.point(100, 100, 0)
    radius = math.sqrt(pow(diameter, 2) + pow(diameter, 2)) / 2
    rotation = math.pi / number_of_points + math.pi / 180 * factor

    points = []

    i = 0
    while i < number_of_points:
        x = center[0] + radius * math.cos(2 * math.pi * i / number_of_points + rotation)
        y = center[1] + radius * math.sin(2 * math.pi * i / number_of_points + rotation)
        z = 0
        points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))
        i += 1

    return points