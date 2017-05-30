# is_between(x, y, z)

def is_between(x,y,z):
    if x <= y and y <= z:
        return(True)
    else: return(False)

x = int(input("Insert x: "))
y = int(input("Insert y: "))
z = int(input("Insert z: "))


print(is_between(x,y,z))