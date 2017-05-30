import math

# calculate distance of 2 points
def distance(x1,x2,y1,y2):
    return math.sqrt(x2-x1)**2 + (y2-y1)**2

n1 = int(input("Insert x1: "))
n2 = int(input("Insert x2: "))
m1 = int(input("Insert y1: "))
m2 = int(input("Insert y1: "))

my_distance = distance(n1,n2,m1,m2)
print(my_distance)

# calculate volume of sphere

def volume_from_radius(radius):
    return((4.0/3.0) * math.pi * radius**3)
input()
print(volume_from_radius(my_distance/2))

# calculate volume of sphere whose radius is distance between two defined points

def volume_from_points(x1, y1, x2, y2):
    return ((4.0 / 3.0) * math.pi * my_distance/2 ** 3)

print(volume_from_points(x1,x2,y1,y2))

