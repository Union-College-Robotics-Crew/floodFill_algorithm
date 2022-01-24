# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
def std_dev(list_of_nums):
    """
    Returns standard deviation values for a list of numbers
    :param list_of_nums: a list of numbers
    :return: standard deviation val
    """
    length = len(list_of_nums)
    mean = sum(list_of_nums)/length

    std_dev = (sum([(num - mean)**2 for num in list_of_nums])/length)**0.5
    return std_dev


if __name__ == "__main__":
    print("std dev: {}".format(std_dev([1,3,5,7])))