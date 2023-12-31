from dataclasses import dataclass
from typing import TypeVar, Optional, Generic

Data = TypeVar("Data")


@dataclass
class Node(Generic[Data]):
    data: Data
    next = None
    prev = None


@dataclass
class Queue:
    size: int = 0
    head: Optional[Node[Data]] = None
    tail: Optional[Node[Data]] = None


def create_queue():
    return Queue()


def size(queue):
    return queue.size


def empty(queue):
    return queue.size == 0


def push(queue, new_data: Data):
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
