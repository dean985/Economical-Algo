#!/usr/bin/env python3
from doctest import testmod
import numpy as np


def is_leximin_better(x: list, y: list) -> bool:
    # return true iff x is leximin better than y

    """
    :param x: list
    :param y: list
    :return: True if x is better leximin than y, otherwise, False.
    >>> is_leximin_better([1],[1,1,1])    # different lengths
    False
    >>> is_leximin_better([2,2,2],[2,2,2])    # same vectors
    False
    >>> is_leximin_better([3,1,3],[2,99,1])
    True
    >>> is_leximin_better([1,3,3],[3,2,1])
    True
    >>> is_leximin_better([50,51],[50,50])
    True
    >>> is_leximin_better([100,4.1,99,3.9],[7,4,10,33])
    False
    >>> is_leximin_better([55,6,44,3,99],[100,200,300,2,400])
    True
    >>> is_leximin_better([2],[3])
    False
    >>> is_leximin_better([5],[1])
    True
    >>> is_leximin_better([1,1,1,1,1,2],[1,1,1,1,1,0])
    True
    >>> is_leximin_better([5.0],[5])
    False
    >>> is_leximin_better([5.7],[3.9])
    True
    >>> is_leximin_better([3,3,9,5],[8,13,3,2])
    True
    >>> is_leximin_better([1,5,8,7],[7,1,5,9])
    False
    >>> is_leximin_better([2,1,8,4],[1,2,3,8])
    True
    >>> is_leximin_better([2,2,2,2],[1,100,45,2])
    True
    >>> is_leximin_better([24, 20, 19, 22, 18], [22, 17, 12, 29, 16])
    True
    >>> is_leximin_better([14, 15, 25, 2, 9], [26, 10, 12, 20, 22])
    False
    >>> is_leximin_better([8.48, 8.4, 2.5,9.02, 9.58], [ 1.77, 1.98, 1.99,  9.91, 12.9])
    True
    """

    if len(x) != len(y):
        return False
    while len(x) > 0:
        x_min = min(x)
        y_min = min(y)
        if x_min > y_min:
            return True
        elif y_min > x_min:
            return False
        else:
            x.remove(x_min)
            y.remove(y_min)
    return False


if __name__ == "__main__":
    testmod(name="is_leximin_better", verbose=True)
