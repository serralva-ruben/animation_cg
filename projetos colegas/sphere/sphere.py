import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import math
import numpy as np


# calculates the points around the sphere
def calculate_points(longitude, latitude, d):
    points = []
    step_latitude = 2*math.pi/latitude
    step_longitude = 2*math.pi/longitude
    for j in range(longitude):
        for i in range(latitude):
            x = d*math.sin(step_latitude*i)*math.cos(step_longitude*j)
            y = d*math.cos(step_latitude*i)*math.cos(step_longitude*j)
            z = d*math.sin(step_longitude*j)
            points.append((x, y, z))
    return points


# calculates the faces of the sphere using the list of points
def calculate_facesWPoints(points, longitude, latitude):
    faces = []
    for j in range(longitude-1):
        for i in range(latitude-1):
            # calculate the indices of the 4 vertices of the current quadrilateral
            v1 = i + j * latitude
            v2 = (i + 1) + j * latitude
            v3 = (i + 1) + (j + 1) * latitude
            v4 = i + (j + 1) * latitude
            faces.append([points[v1], points[v2], points[v3], points[v4]])
    return faces


# prints the list of points and faces of the sphere
def printSphere(longitude, latitude, diameter):
    points = calculate_points(longitude, latitude, diameter)
    matriz = np.array(points)
    return matriz

# shows the sphere using matplotlib
def showSphere(longitude, latitude, diameter):
    points = calculate_points(longitude, latitude, diameter)
    faces = calculate_facesWPoints(points, longitude, latitude)
    # Draw the sphere and faces
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], s=1)
    ax.set_aspect('equal')
    collection = Poly3DCollection(faces, alpha=0.2, facecolor='r', edgecolor='black')
    ax.add_collection(collection)
    plt.show()



