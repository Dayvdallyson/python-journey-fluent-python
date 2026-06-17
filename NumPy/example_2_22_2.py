import numpy

floats = numpy.loadtxt("floats-10M-lines.txt")

print(floats[-3:])

floats *= 0.5

print(floats[-3:])

from time import perf_counter as pc

t0 = pc()
floats /= 3

print(pc() - t0)

numpy.save("floats-10M", floats)
floats2 = numpy.load("floats-10M.npy", "r+")
floats2 *= 6

print(floats2[-3:])
