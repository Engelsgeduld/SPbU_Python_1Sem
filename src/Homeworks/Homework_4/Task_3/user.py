from queue import *


def main():
    my_queue = create_queue()
    push(111, my_queue)
    push(222, my_queue)
    print(empty(my_queue))
    print(size(my_queue))
    print(top(my_queue))
    print(tail(my_queue))
    push(333, my_queue)
    push("aaa", my_queue)
    push("bbb", my_queue)
    pop(my_queue)
    pop(my_queue)
    print(size(my_queue))
    print(top(my_queue))
    print(tail(my_queue))
    pop(my_queue)
    pop(my_queue)
    pop(my_queue)
    print(empty(my_queue))
    print(top(my_queue))
    print(tail(my_queue))
    pop(my_queue)


if __name__ == "__main__":
    main()
