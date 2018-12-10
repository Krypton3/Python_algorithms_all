# time complexity O(nlogn)
def binary_search(array, val, low, high):
    if high <= low:
        if val > array[low]:
            return low + 1
        else:
            return low

    mid = int((low + high)/2)
    if val == array[mid]:
        return mid + 1

    if val > array[mid]:
        return binary_search(array, val, mid+1, high)
    else:
        return binary_search(array, val, low, mid-1)


def insertion(array):
    for i in range(1, len(array)):

        value = array[i]
        track = i - 1

        loc = binary_search(array, value, 0, track)

        while track >= loc:
            array[track+1] = array[track]
            track -= 1
        array[track+1] = value

    print("After Sorting: \n")
    for i in range(len(array)):
        print(array[i])


if __name__ == '__main__':
    array = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    insertion(array)
