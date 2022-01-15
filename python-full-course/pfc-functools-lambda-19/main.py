from functools import reduce

def get_max(my_list):
    global_best = float("-inf")
    for el in my_list:
        if el > global_best:
            global_best = el
    return global_best

my_list = [1,3,4,5,6,2,3]
reduced = reduce(min,my_list,float("inf"))
print(reduced)
