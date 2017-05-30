def calc_sum(list):
    print(sum(list))

list = [int(x) for x in input("Give a list of numbers: ").split()]

calc_sum(list)