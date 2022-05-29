import math
import numpy as np
from random import randint
from puzzle import solve_puzzle


def create_images(shape, size):
    size = size - 1
    res = []

    # blank image (green background)
    for i in range(4):
        res.append(np.full((int(shape/2), int(shape/2), 3), (0, 255, 0), dtype=np.uint8))

    # add one random pixel
    for i in range(4):

        axis = randint(0, 1)  # axis x or y
        r = randint(0, size)  # pixel index

        if axis == 0:
            res[i][size][r] = (0, 0, 0)
        else:
            res[i][r][size] = (0, 0, 0)

        for j in range(i):
            res[i] = np.rot90(res[i])

    return [res[2], res[1], res[3], res[0]]


if __name__ == '__main__':

    num_tests = 10
    for ii in range(num_tests):
        n = randint(10, 1000)  # N
        s = randint(2, math.ceil(math.sqrt(n)))  # M

        sub_images = create_images(n, int(s/2))

        # shuffle
        for i in range(4):
            for j in range(4):
                if j == i:
                    continue
                for k in range(4):
                    if k in [i, j]:
                        continue
                    for l in range(4):
                        if l in [i, j, k]:
                            continue
                        shuffled = [sub_images[i], sub_images[j], sub_images[k], sub_images[l]]
                        if solve_puzzle(shuffled, n) != [i, j, k, l]:
                            print("FAIL")
                            exit(1)

    print("PASS")
