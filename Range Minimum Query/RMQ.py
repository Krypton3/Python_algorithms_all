def Make_Tree(array, index, low, high, tree):
    if low == high:
        tree[index] = array[low]
        return
    left = index*2
    right = index*2 + 1
    mid = (low+high)/2
    Make_Tree(array, left, low, int(mid), tree)
    Make_Tree(array, right, int(mid)+1, high, tree)
    tree[index] = min(tree[left], tree[right])


def query(tree, index, low, high, a, b):
    if a > high or b < low:
        return 999999
    if a <= low and b >= high:
        return tree[index]
    left = index * 2
    right = index * 2 + 1
    mid = (low + high) / 2
    p1 = query(tree, left, low, int(mid), a, b)
    p2 = query(tree, right, int(mid)+1, high, a, b)
    return min(p1, p2)


if __name__ == '__main__':
    Array = [1, 3, 89, 2, 9, 11, 25, 42, 4, 6]
    N = 9
    MAX = 100
    tree = [None] * 300
    Make_Tree(Array, 1, 1, N, tree)

    print("Minimum value found in the given range: ")
    print(query(tree, 1, 1, N, 5, 9))
