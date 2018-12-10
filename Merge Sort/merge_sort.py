def merge(array):
    if len(array) > 1:
        mid = len(array)/2
        left_array = array[:int(mid)]
        right_array = array[int(mid):]

        merge(left_array)
        merge(right_array)

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] > right_array[j]:
                array[k] = right_array[j]
                j += 1
            else:
                array[k] = left_array[i]
                i += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


def after_sort(array):
    for i in range(len(array)):
        print(array[i])


if __name__ == '__main__':
    array = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    merge(array)
    after_sort(array)
