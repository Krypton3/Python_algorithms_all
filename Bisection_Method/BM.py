import math


def bisection(eq, a, b):
    # baseline
    if eq(a) == 0:
        return a
    elif eq(b) == 0:
        return b
    elif eq(a) * eq(b) > 0:
        print("Root can't be found!!")
        return 0
    else:
        start = a
        end = b
        mid = (start + end)/2
        while abs(start - mid) > 10**-7:
            if eq(mid) == 0:
                return mid
            elif eq(mid) * eq(start) < 0:
                end = mid
            else:
                start = mid
            mid = (start + end)/2
        return mid


def equation(x):
    return math.pow(x, 3) - 2 * x - 5


if __name__ == '__main__':
    print(bisection(equation, 1, 1000))

