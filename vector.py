import numpy as np


class Vector:
    def __init__(self, nums):
        self.nums = np.array(nums)

    def __str__(self):
        return "{}".format(self.nums)

    def __add__(self, other):
        return Vector(self.nums + other.nums)

    def dot(self, other):
        return self.nums @ other.nums

    def scale(self, scalar):
        return Vector(scalar * self.nums)

    def norm(self):
        return np.linalg.norm(self.nums)
