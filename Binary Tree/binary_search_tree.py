class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def min_value_find(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)

# hints to update a position: use search node function with a little modification


def search_node(root, val):
    if root is not None and root.val == val:
        print("The key is root value and it is found!")
    else:
        if root.val < val:
            if root.right.val == val:
                print("The key is found --> right side of the root!!")
            else:
                search_node(root.right, val)
        elif root.val > val:
            if root.left.val == val:
                print("The key is found --> left side of the root!!")
            else:
                search_node(root.left, val)
        else:
            print("Key doesn't exists!!")


def delete_node(root, val):
    if root is None:
        return root

    if root.val < val:
        root.right = delete_node(root.right, val)
    elif root.val > val:
        root.left = delete_node(root.left, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_find(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


r = Node(50)
insert_node(r, Node(30))
insert_node(r, Node(20))
insert_node(r, Node(40))
insert_node(r, Node(70))
insert_node(r, Node(60))
insert_node(r, Node(80))

print("In order printing:")
in_order(r)

print("post order printing:")
post_order(r)

print("pre order printing:")
pre_order(r)

print("Binary search tree search with a val: ")
search_node(r, 80)

print("\nDelete 20")
root = delete_node(r, 20)
print("In order traversal of the modified tree")
in_order(root)

print("\nDelete 50")
root = delete_node(r, 50)
print("In order traversal of the modified tree")
in_order(root)
