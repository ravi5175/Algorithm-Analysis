import random
import bubbleSort

class Test:
    available_sort=['bubble_sort']

    def __init__(self, sorting, length=100, range=None, rand=True, reverse=False):
        if sorting in available_sort:
            