import sys


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    first, second = 1, 1
    result = 0
    for _ in range(2, n):
        result = first + second
        first = second
        second = result
    return result


def validation_fib_input(n: str) -> int:
    if not n.isdigit():
        raise ValueError(
            "N must be a positive integer without any other symbols(+ - . etc)"
        )
    if n[0] == "0":
        raise ValueError("N can not begin with zero")
    integer_n = int(n)
    if not 0 <= integer_n <= 90:
        raise ValueError("N must be in range 0..90")
    return integer_n


def main():
    fib_n_input = input("Enter number of Fibonacci:\n")
    try:
        n = validation_fib_input(fib_n_input)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
    else:
        print(f"{n}th Fibonacci number: {fibonacci(n)}")


if __name__ == "__main__":
    main()
