import math

def distance(x1,x2,y1,y2):
    return math.sqrt(x2-x1)**2 + (y2-y1)**2

def volume_from_radius(radius):
    return((4.0/3.0) * math.pi * radius**3)

def volume_fromm_points(x1, x2, y1, y2):
    dist = distance(x1,x2,y1,y2)
    return volume_from_radius(dist)

print(volume_from_points(1,2,3,5))