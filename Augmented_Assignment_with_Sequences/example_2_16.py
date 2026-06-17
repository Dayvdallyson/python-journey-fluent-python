try:
    # this would break cause the tuples are not mutable
    t = (1, 2, [30, 40])
    t[2] += [50, 60]
    print(t)

except:
    # this gonna work cause im extending the tuple, tuple is imutable
    # what is mutable in this case is the list inside the tuple
    t2 = (1, 2, [30, 40])
    t2[2].extend([50, 60])
    print("This works: ", t2)
