from vector import Vector
from functools import reduce
import numpy as np
from math import pi

vectors = []
with open('vectors.txt') as f:
    for line in f:
        v = Vector(tuple(map(int, line.strip().split(','))))
        vectors.append(v)


vectors = [vectors[0].scale(3)] + [vectors[-1].scale(3)] + vectors[1:-1]
final = reduce(lambda acc, vec: acc + vec, vectors, Vector([0, 0]))
print(final)

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1, v1.norm())

# instructoions...
# part 1
# take the 5 vectors from the file, and display the
# lengths of each vector sorted from shortest to largest
# and dispay the shortest one

lengths = np.array([v.norm() for v in vectors])
sorted_lengths = np.sort(lengths)
print('lengths:', sorted_lengths, 'first:', sorted_lengths[0])

# part 2
# find the angle, theta, between each set
# i.e., theta between 1 and 2 ... 2 and 3 ... etc
# should have 4 thetas

thetas = [(180 / pi) * np.arccos(v1.dot(v2) / (v1.norm() * v2.norm())) for v1, v2 in zip(vectors, vectors[1:])]
print('thetas:', thetas)
