# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_circle_distance(xc1, yc1, xc2, yc2):
    """Returns the distance between the two circles."""
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

print(f'distance: {get_circle_distance(4, 4.25, 53, -5.35)}')

def get_vector_length(xa, ya, xb, yb):
    """Returns the length of vector AB vector
    which is a vector between A and B points."""
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

print(f'length: {get_vector_length(-36, 97, .34, .91)}')
