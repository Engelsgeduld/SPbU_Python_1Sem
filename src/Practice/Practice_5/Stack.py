from collections import namedtuple
from dataclasses import dataclass

StackElement = namedtuple("StackElement", ["next", "value"])


@dataclass
class Stack:
    size: int
    head: StackElement


def create_stack():
    new_stack = Stack(size=0, head=StackElement(next=None, value=None))
    return new_stack


def empty(stack):
    return True if stack.size == 0 else False


def size(stack):
    return stack.size


def top(stack):
    return stack.head.value


def push(stack, value):
    stack.head = StackElement(stack.head, f"{value}")
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
    pop(stack)
    pop(stack)
    print(top(stack))
    print(empty(stack))
    print(size(stack))


if __name__ == "__main__":
    main()
