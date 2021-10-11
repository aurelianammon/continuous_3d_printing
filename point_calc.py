# importing numpy
import numpy as np

# define point relevant functions
def point(x = 0, y = 0, z = 0):
	return np.array([x, y, z])

def distance(a, b):
    return np.linalg.norm(a - b)