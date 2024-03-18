class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left) - get_height(root_node.right)


def update_height_and_balance(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)
    return node, balance

def restore_balance(node, balance):
    if balance > 1:
        if get_balance(node.left) >= 0:
            return right_rotation(node)
        else:
            node.left = left_rotation(node.left)
            return right_rotation(node)
    if balance < -1:
        if get_balance(node.right) <= 0:
            return left_rotation(node)
        else:
            node.right = right_rotation(node.right)
            return left_rotation(node)


def find_node_with_highest_priority(root_node):
    node_with_highest_priority = root_node
    while node_with_highest_priority.right:
        node_with_highest_priority = node_with_highest_priority.right
    return node_with_highest_priority


def insert_into_queue(root_node, value, priority):
    if not root_node:
        return Node(value, priority)
    elif priority <= root_node.priority:
        root_node.left = insert_into_queue(root_node.left, value, priority)
    else:
        root_node.right = insert_into_queue(root_node.right, value, priority)
    root_node, balance = update_height_and_balance(root_node)
    if abs(balance) > 1:
        return restore_balance(root_node, balance)
    return root_node



def delete_from_queue(root_node):
    if not root_node:
        return root_node
    if not root_node.right:
        return root_node.left
    root_node.right = delete_from_queue(root_node.right)
    root_node, balance = update_height_and_balance(root_node)
    if abs(balance) > 1:
        return restore_balance(root_node, balance)
    return find_node_with_highest_priority(root_node)


def right_rotation(z_node):
    y_node = z_node.left
    w_node = y_node.right

    y_node.right = z_node
    z_node.left = w_node

    z_node.height = 1 + max(get_height(z_node.left), get_height(z_node.right))
    y_node.height = 1 + max(get_height(y_node.left), get_height(y_node.right))
    return y_node


def left_rotation(z_node):
    y_node = z_node.right
    w_node = y_node.left

    y_node.left = z_node
    z_node.right = w_node

    z_node.height = 1 + max(get_height(z_node.left), get_height(z_node.right))
    y_node.height = 1 + max(get_height(y_node.left), get_height(y_node.right))
    return y_node



def left_right_rotation(z_node):
    z_node.left = left_rotation(z_node.left)
    return right_rotation(z_node)


def right_left_rotation(z_node):
    z_node.right = left_rotation(z_node.right)
    return left_rotation(z_node)


def print_queue(root_node):
    if not root_node:
        return
    print_queue(root_node.right)
    print(root_node.value)
    print_queue(root_node.left)
