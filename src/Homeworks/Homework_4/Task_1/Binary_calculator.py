from fnmatch import fnmatch


def to_integer(binary):
    if binary == [1] + [0] * (len(binary) - 1):
        return (2 ** len(binary) // 2) * (-1)
    if not binary[0]:
        result = sum([binary[::-1][i] * 2**i for i in range(0, len(binary) - 1)])
    else:
        binary = binary_sum(binary, byte_form(-1, len(binary) + 1))
        binary = list(map(lambda x: int(not x), binary))
        result = sum([binary[::-1][i] * 2**i for i in range(0, len(binary) - 1)]) * (
            -1
        )
    return result


def binary(integer):
    integer = abs(integer)
    bytes = []
    while integer > 0:
        bytes.append(integer % 2)
        integer = integer // 2
    bytes.reverse()
    return bytes


def byte_form(integer, n):
    result = (
        [0 if integer > 0 else 1]
        + [0] * (n - len(binary(integer)) - 1)
        + binary(integer)
    )
    if result[0]:
        result = [result[0]] + binary_sum(
            list(map(lambda x: int(not x), result[1:])), byte_form(1, n)
        )
    return result


def binary_sum(firsts_num, second_num):
    ost = 0
    for i in range(1, len(firsts_num) + 1):
        firsts_num[i * (-1)] += second_num[i * (-1)] + ost
        ost = firsts_num[i * (-1)] // 2
        firsts_num[i * (-1)] = firsts_num[i * (-1)] % 2
    return firsts_num


def is_integer(num):
    if fnmatch(num, "-" + "[1234567890]" * (len(num) - 1)):
        return True
    return num.isdigit()


def valid_user_input(user_input):
    valid_nums = [is_integer(num) for num in user_input.split()]
    if all(valid_nums) and len(valid_nums) == 2:
        return list(map(int, user_input.split()))
    else:
        raise ValueError(
            "Введенные аргументы не являются числами или их количество выше допустимого"
        )


def main():
    user_input = input("Введите 2 числа\n")
    try:
        num1, num2 = valid_user_input(user_input)
        n = max(len(binary(num1)), len(binary(num2))) + 2
        print(f"Binary {num1}: {byte_form(num1, n)}")
        print(f"Binary {num2}: {byte_form(num2, n)}")
        binary_sum_num1_num2 = binary_sum(byte_form(num1, n), byte_form(num2, n))
        print(f"Binary result: {num1}+{num2}: {binary_sum_num1_num2}")
        print(f"Decimal result: {to_integer(binary_sum_num1_num2)}")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
