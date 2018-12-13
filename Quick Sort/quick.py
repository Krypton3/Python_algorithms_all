def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i+1]
    array[i+1] = array[high]
    array[high] = temp
    return i + 1


def quick(array, low, high):
    if low < high:
        prt = partition(array, low, high)
        quick(array, low, prt - 1)
        quick(array, prt + 1, high)


if __name__ == '__main__':
    array = [2, 5, 1, 10, 5, 20, 8, 12, 0, 9, 11, 13, 21, 3]
    low = 0
    high = len(array) - 1
    quick(array, low, high)

    print("After sorting: ")
    for i in range(len(array)):
        print(array[i], end=" ")
