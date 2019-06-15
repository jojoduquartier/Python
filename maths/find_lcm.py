def find_lcm(num_1, num_2):
    """
    Returns the least common multiple of two integers.
    :param x: any integer
    :param y: any integer
    :return: integer z such that remainder(z/x) == 0 and remainder(z/y) == 0
    """
    max = num_1 if num_1 > num_2 else num_2
    lcm = max
    while (True):
        if ((lcm % num_1 == 0) and (lcm % num_2 == 0)):
            break
        lcm += max
    return lcm


def lcm(x: int, y: int):
    """
    Returns the least common multiple of two integers.
    :param x: any integer
    :param y: any integer
    :return: integer z such that remainder(z/x) == 0 and remainder(z/y) == 0

    Not necessarily faster solution, just a different solution using filter
    """

    # if either number is 0 then lcm should be 0
    if x == 0 or y == 0:
        return 0

    # simple algorithm is to return the first multiple of x that is also a multiple of y
    # the built in filter function is great for such tasks
    # note that we use multiples of the large number as it makes the generator length smaller
    min_ = min(x, y)
    max_ = max(x, y)

    return next(filter(lambda i: i % min_ == 0, (max_ * j for j in range(1, min_ + 1))))


def main():
    num_1 = 12
    num_2 = 76
    print(find_lcm(num_1, num_2))
    print(lcm(num_1, num_2))


if __name__ == '__main__':
    main()
