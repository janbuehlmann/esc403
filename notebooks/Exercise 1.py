from builtins import print, int

x = int(input("What's your value for x?"))
y = int(input("What's your value for y?"))

print('Your values for x and y are', x, "and", y)

if x < y:
    print(1)
elif x == y:
    print(0)
else:
    print(-1)


def compare(x,y):
        if x > y:
            print(1)
        elif( x < y):
            print(-1)
        else:
            print(0)

n1 = int(input("What's your x?"))
n2 = int(input("What's your y?"))

compare(n1,n2)