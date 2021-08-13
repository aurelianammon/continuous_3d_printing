# importing numpy
import numpy as np

# define point relevant functions
def point(x, y, z):
	return np.array([x, y, z])

def distance(a, b):
    return np.linalg.norm(a - b)