points = int(input("Insert number of points: "))
max_points = int(input("Insert number fo max. points: "))


def calculate_mark(points, max_points):
    mark = ((points*5)/max_points) + 1
    mark_rounded = round(mark*2)*0.5
    print(mark_rounded)

calculate_mark(points, max_points)