def inverse(byte):
    return 0 if byte else 1


def positive_binary_to_integer(binary):
    reverse_binary = binary[::-1]
    binary_power_two = [reverse_binary[i] * 2**i for i in range(len(binary) - 1)]
    return sum(binary_power_two)


def negative_binary_to_integer(binary):
    negative_binary = to_binary_sum(binary, to_byte_form(-1, len(binary) + 1))
    negative_binary = list(map(lambda x: inverse(x), negative_binary))
    negative_binary = negative_binary[::-1]
    return -sum([negative_binary[i] * 2**i for i in range(len(negative_binary) - 1)])


def to_integer(binary):
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


def to_byte_form(integer, n):
    sign_bit = 0 if integer >= 0 else 1
    zero_row = [0] * (n - len(to_binary(integer)) - 1)
    result = [sign_bit] + zero_row + to_binary(integer)
    if sign_bit:
        inverse_binary = list(map(lambda x: inverse(x), result[1:]))
        result = [sign_bit] + to_binary_sum(inverse_binary, to_byte_form(1, n))
    return result


def to_binary_sum(firsts_num, second_num):
    ost = 0
    for i in range(1, len(firsts_num) + 1):
        firsts_num[-i] += second_num[-i] + ost
        ost = firsts_num[-i] // 2
        firsts_num[-i] = firsts_num[-i] % 2
    return firsts_num


def validate_user_input(user_input):
    split_user_input = user_input.split()
    if len(split_user_input) < 2:
        raise ValueError("Введено менее 2 аргументов")
    try:
        valid_nums = [float(num) for num in split_user_input]
    except:
        raise ValueError(
            "Введенные аргументы не являются числами или их количество выше допустимого"
        )
    return list(map(int, valid_nums))


def main():
    user_input = input("Введите 2 числа\n")
    try:
        num1, num2 = validate_user_input(user_input)
        n = max(len(to_binary(num1)), len(to_binary(num2))) + 2
        print(f"Binary {num1}: {to_byte_form(num1, n)}")
        print(f"Binary {num2}: {to_byte_form(num2, n)}")
        binary_sum_num1_num2 = to_binary_sum(
            to_byte_form(num1, n), to_byte_form(num2, n)
        )
        binary_diff_num1_num2 = to_binary_sum(
            to_byte_form(num1, n), to_byte_form(-num2, n)
        )
        print(f"Binary result: {num1}+{num2}: {binary_sum_num1_num2}")
        print(f"Binary result: {num1}-{num2}: {binary_diff_num1_num2}")
        print(
            f"Decimal result: {to_integer(binary_sum_num1_num2)}, {to_integer(binary_diff_num1_num2)}"
        )

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
