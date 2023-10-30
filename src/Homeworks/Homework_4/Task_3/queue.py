class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


def create_queue():
    return Queue()


def size(queue):
    return queue.size


def empty(queue):
    return queue.size == 0


def push(queue, new_data):
    new_node = Node(new_data)
    new_node.next = queue.head
    if queue.size != 0:
        queue.head.prev = new_node
        queue.head = new_node
        new_node.prev = None

    else:
        queue.head = new_node
        queue.tail = new_node
        new_node.prev = None
    queue.size += 1


def top(queue):
    if empty(queue):
        return None
    return queue.head.data


def tail(queue):
    if empty(queue):
        return None
    return queue.tail.data


def pop(queue):
    if queue.size == 0:
        raise IndexError("Queue is empty. Please add something to delete")
    elif queue.size == 1:
        queue.head = queue.tail = queue.tail.next
    else:
        temp = queue.tail
        temp.prev.next = None
        queue.tail = temp.prev
        temp.prev = None
    queue.size -= 1
