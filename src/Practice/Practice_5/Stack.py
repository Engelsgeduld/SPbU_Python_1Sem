from collections import namedtuple
from dataclasses import dataclass
from typing import Optional

StackElement = namedtuple("StackElement", ["next", "value"])


@dataclass
class Stack:
    size: int
    head: Optional[StackElement]


def create_stack():
    new_stack = Stack(size=0, head=None)
    return new_stack


def empty(stack):
    return not bool(stack.size)


def size(stack):
    return stack.size


def top(stack):
    return stack.head.value if stack.head is not None else None


def push(stack, value):
    stack.head = StackElement(stack.head, value)
    stack.size += 1


def pop(stack):
    if empty(stack):
        return False
    stack.head = stack.head.next
    stack.size -= 1
    return True


def main():
    stack = create_stack()
    push(stack, "111")
    push(stack, "222")
    push(stack, "333")
    pop(stack)
    pop(stack)
    print(top(stack))
    print(empty(stack))
    print(size(stack))


if __name__ == "__main__":
    main()
