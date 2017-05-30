def calculate_mark(points, max_points):
    points = float(points)
    max_points = float(max_points)
    mark = ((points * 5) / max_points) + 1
    mark_rounded = round(mark * 2) * 0.5
    print(mark_rounded)



my_class = {}

while True:
    name = input("Insert your name: ")
    if name == "exit":
        print("Good Bye!")
        break


    else:
        points = input("Insert number of your points: ")
        max_points = input("Insert number of max. points: ")
        student_mark = calculate_mark(points, max_points)
        my_class[name] = student_mark

sum = 0
counter = 0
for name, grade in my_class.items():
    sum += mark
    counter += 1
    line = name + ": " +str(mark)
    if grade >= 4.0:
        line +=
    else:
        line = line + ", failed"
    print(line)

print("The average grade is: ")
