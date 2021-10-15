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
def create_stepover(angle = 0, stepover_parameter = 10):
    diameter = 50
    center = pc.point(100, 100, 0)


    points = []

    # first line
    x = center[0] - diameter / 2
    y = center[1] - diameter / 2
    z = 0
    points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))

    x = points[-1][0] + diameter
    y = points[-1][1]
    z = 0
    points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))

    for i in range(stepover_parameter):
        x = points[-1][0]
        y = points[-1][1] + (diameter/stepover_parameter)
        z = 0
        points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))

        if (i % 2) == 0:
            x = points[-1][0] - diameter
            y = points[-1][1]
            z = 0
            points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))
        else:
            x = points[-1][0] + diameter
            y = points[-1][1]
            z = 0
            points.append(pc.point(round(x, 5), round(y, 5), round(z, 5)))

    for i in range(len(points)):
        points[i] = pc.rotate(points[i], center, angle)

    return points

def toolpath(points):
    
    new_points = []

    for i in range(len(points) - 1)
    i = 0
    while i < len(points) - 1:
        point = points[i]
        point_next = points[(i + 1) % (len(points))]



        new_points.append()
        i += 1
    
    return new_points