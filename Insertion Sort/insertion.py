# time complexity O(n^2)
def insertion(array):
    for i in range(1, len(array)):
        value = array[i]

        track = i - 1

        while track >= 0 and value < array[track]:
            array[track+1] = array[track]
            track -= 1
        array[track+1] = value

    print("After Sorting: \n")
    for i in range(len(array)):
        print(array[i])


if __name__ == '__main__':
    array = [2, 5, 1, 10, 5, 20, 8, 12]
    insertion(array)
