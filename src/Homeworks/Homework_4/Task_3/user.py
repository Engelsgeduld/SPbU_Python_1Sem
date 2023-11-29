from queue import *


def main():
    my_queue = create_queue()
    push(my_queue, 111)
    push(my_queue, 222)
    print(empty(my_queue))
    print(size(my_queue))
    print(top(my_queue))
    print(tail(my_queue))
    push(my_queue, 333)
    push(my_queue, "aaa")
    push(my_queue, "bbb")
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
