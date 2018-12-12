def selection(array):
    for i in range(len(array)):
        find_small_index = i
        for j in range(i+1, len(array)):
            if array[find_small_index] > array[j]:
                find_small_index = j

        temp = array[i]
        array[i] = array[find_small_index]
        array[find_small_index] = temp

    print("After Sorting: \n")
    for i in range(len(array)):
        print(array[i], end=" ")


if __name__ == '__main__':
    array = [2, 5, 1, 10, 5, 20, 8, 12, 0, 4, 25, 9]
    selection(array)
