## Assignment3 ES 122
## Name:
## EID : 
##
## Fill in the functions and classes below


# Problem 1
# Optional Paramaters:
# Each of these paramaters should have the value True if you are applying the paramater 
# Reverse: Sorts from highest to lowest.
# NoDuplicates: That does not print any duplicate numbers
# SortbyAbsoluteValues: That takes the absolute values of all transmitted numbers before 
# If a keyword argument is passed that is not one of the three above Print "Error: Not a valid Paramater" and return nothing 
# The function should return the sorted list
def sortedTheseNumbers(*args, **kwargs):
    return



# Problem 2
# A class that represents a point in space
# required variables and methods
# x - stores the x value of the point
# y - stores the y value of the point
# z - stores the z value of the point
# __init__  (method) - Should take in x, y, and z parameters and set their values
# __str__ (method) - Should return a string representation of the point. It should be formatted like a tuple ex: (x, y, z) 
# __eq__ (method) - Should take in a Point object and return true if the x, y and z values of the input point are the same as the x, y, and z values of the calling point

class Point:
    def __init__(self, x, y, z):
        return 

    def __str__(self):
        return

    def __eq__(self, p):
        return

# This class holds a list of 3D points which it uses to construct the bounding box
# required variables and methods
# points - stores the list of Point objects
# __init__ (method) - Should take in a list of Point objects and set the value of points
# add (method) - takes a Point object as input and inserts it in to the points list
# remove (method)- takes a Point object as input and removes it from Points list. Should do nothing if point is not in list
class PointCloudData:
    def __init__(self, Points):
        return

    def add(self, p):
        return

    def remove(self, p):
        return

# This class represents a bounding box. It stores the center and dimensions of the box. This class is a subclass of PointCloudData
# center (variable) - A Point object used to store the location of the box in Cartesian space. The point should be at the center of the box.
# dimensions (variable) - A list with the width, height, and depth of the bounding box.
# __init__ (method) - Should take in a list of points as input and then call the superclass’s init method. It should then calculate and set the center and dimensions of the box.
# updateBox (method) - This method should take in a new list of points for the bounding box and should update the dimensions and center. 
# collisionCheck (method) - this method takes in a BoundingBox, b, as an input and checks to see if the passed bounding box b is in collision with it and returns true if so and otherwise false.
# __add__ (method) - This method should take in a BoundingBox, b, as an input and it should combine the two bounding boxes. It should return a bounding box that minimally contains both bounding boxes. Note: this method overrides the + operation. This means that if you say BoundingBox1 + BoundingBox2, what is really happening is you are saying BoundingBox1.__add__(BoundingBox2).
# __len__ (method) - This method should return the volume of the bounding box

class BoundingBox(PointCloudData):
    def __init__(self, Points):
        return 

    def updateBox(self, Points):
        return

    def collisionCheck(self, b):
        return

    def __add__(self, b):
        return

    def __len__(self):
        return
    
    
# You can test your code by running testcases.py
