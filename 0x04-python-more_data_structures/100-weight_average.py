#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_sum = sum([x[0] * x[1] for x in my_list])
    total_weight = sum([x[1] for x in my_list])
    return weighted_sum / total_weight
