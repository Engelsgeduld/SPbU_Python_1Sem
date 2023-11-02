def inverse(byte):
    return 0 if byte else 1


def positive_binary_to_integer(binary):
    binary_power_two = [binary[::-1][i] * 2**i for i in range(len(binary) - 1)]
    return sum(binary_power_two)


def zero_binary(binary):
    return -(2 ** len(binary) // 2)


def negative_binary_to_integer(binary):
    negative_binary = to_binary_sum(binary, byte_form(-1, len(binary) + 1))
    negative_binary = list(map(lambda x: inverse(x), negative_binary))[::-1]
    return -sum([negative_binary[i] * 2**i for i in range(len(negative_binary) - 1)])


def to_integer(binary):
    if binary == [1] + [0] * (len(binary) - 1):
        return zero_binary(binary)
    if not binary[0]:
        return positive_binary_to_integer(binary)
    else:
        return negative_binary_to_integer(binary)


def to_binary(integer):
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
        + [0] * (n - len(to_binary(integer)) - 1)
        + to_binary(integer)
    )
    if result[0]:
        result = [result[0]] + to_binary_sum(
            list(map(lambda x: x ^ 1, result[1:])), byte_form(1, n)
        )
    return result


def to_binary_sum(firsts_num, second_num):
    ost = 0
    for i in range(1, len(firsts_num) + 1):
        firsts_num[-i] += second_num[-i] + ost
        ost = firsts_num[i * (-1)] // 2
        firsts_num[-i] = firsts_num[-i] % 2
    return firsts_num


def valid_user_input(user_input):
    split_user_input = user_input.split()
    if len(split_user_input) < 2:
        raise ValueError("Введено менее 2 аргументов")
    try:
        valid_nums = [float(num) for num in split_user_input]
        return list(map(int, valid_nums))
    except:
        raise ValueError(
            "Введенные аргументы не являются числами или их количество выше допустимого"
        )


def main():
    user_input = input("Введите 2 числа\n")
    try:
        num1, num2 = valid_user_input(user_input)
        n = max(len(to_binary(num1)), len(to_binary(num2))) + 2
        print(f"Binary {num1}: {byte_form(num1, n)}")
        print(f"Binary {num2}: {byte_form(num2, n)}")
        binary_sum_num1_num2 = to_binary_sum(byte_form(num1, n), byte_form(num2, n))
        print(f"Binary result: {num1}+{num2}: {binary_sum_num1_num2}")
        print(f"Decimal result: {to_integer(binary_sum_num1_num2)}")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
