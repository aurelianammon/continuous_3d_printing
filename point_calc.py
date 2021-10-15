# importing numpy
import numpy as np

# define point relevant functions
def point(x = 0, y = 0, z = 0):
	return np.array([x, y, z])

def distance(a, b):
    return np.linalg.norm(a - b)

def rotate(p, o=np.array([0, 0, 0]), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle), 0],
                  [np.sin(angle), np.cos(angle), 0],
                  [0, 0, 0]])

    return np.squeeze((R @ (p.T-o.T) + o.T).T)

# Testing functions
if __name__ == "__main__":

    p = point(50, 50, 0)
    c = point(100, 100, 0)

    print(rotate(p, c, 180))



