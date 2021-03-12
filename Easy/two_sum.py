"""
This file contains functions which returns
the elements of any non empty array whose
sum is equal to the target sum
eg: array = [3, -5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    output = [-1, 11]
"""


def two_sum_sol1(array, target_sum):
    """
    This is not optimal solution as the time complexity is O(n)²
    :param array: input array
    :param target_sum: target sum
    :return: elements that are equal to target sum
    """
    for x in range(len(array)-1):
        for y in range(x, len(array)):
            if array[x] + array[y] == target_sum:
                return [array[x], array[y]]
    return []


if __name__ == "__main__":
    array = [3, -5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    sol = two_sum_sol1(array, target_sum)
    print(sol)
