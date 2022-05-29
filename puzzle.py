import math


def get_size(np_pic, max_size):
    """ return size which is M/2 """
    for x in range(0, max_size):
        for y in range(0, max_size):
            if (np_pic[y][x] == (0, 0, 0)).all():
                return max(y, x)


def get_location(np_pic, size):

    shape = np_pic.shape[0]-1

    for i in range(size+1):
        # check upper right (index 2):
        if (np_pic[size, shape-i] == (0, 0, 0)).all() or (np_pic[i, shape-size] == (0, 0, 0)).all():
            return 2

        # check bottom left (index 1):
        if (np_pic[shape-size, i] == (0, 0, 0)).all() or (np_pic[shape-i, size] == (0, 0, 0)).all():
            return 1

    # if not found, it is the option
    return 0


def solve_puzzle(files, n):
    res = [None, None, None, None]
    size = None

    max_size = math.ceil(math.sqrt(n)/2)

    for i in range(4):
        size = get_size(files[i], max_size)

        if size is not None:
            res[i] = 3  # piece solved!
            break

    sum_idx = 3
    last_idx = 3 if res[3] is None else 2  # last index to skip
    for i in range(3):
        if i == last_idx:
            break

        if res[i] is None:
            res[i] = get_location(files[i], size)
            sum_idx = sum_idx + res[i]

    # last file, no need to check
    res[last_idx] = 6 - sum_idx  # 0 + 1 + 2 + 3 = 6

    return res
