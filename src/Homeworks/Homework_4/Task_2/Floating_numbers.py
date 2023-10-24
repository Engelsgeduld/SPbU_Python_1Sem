def valid_user_input_float(user_input):
    try:
        float(user_input)
    except:
        raise ValueError("Entered value must be integer")


def choose_standard(user_input):
    standards = {"FP64": (11, 52), "FP32": (8, 23), "FP16": (5, 10)}
    if user_input in standards:
        return standards[user_input]
    else:
        raise ValueError("Standard not found")


def get_sign(user_input):
    return user_input[0] if user_input[0] == "-" else ""


def binary(integer):
    integer = abs(integer)
    bytes = []
    while integer > 0:
        bytes.append(integer % 2)
        integer = integer // 2
    bytes.reverse()
    return bytes


def get_fact_part(user_input):
    first_part = user_input.split(".")[0]
    return binary(int(first_part))


def get_dec_part(user_input, deep=52):
    second_part = "0." + user_input.split(".")[1]
    second_part = float(second_part)
    binary_second_part = []
    while second_part != 0 and len(binary_second_part) != deep:
        second_part *= 2
        binary_second_part.append((int(second_part)))
        second_part -= int(second_part)
    return binary_second_part


def fp_standard(sign, mantis, exp, k, m):
    switch = binary(exp + 2 ** (k - 1) - 2)
    if len(switch) > k:
        raise ValueError("Range overflow")

    if len(mantis) > m:
        raise ValueError("Precision out of range")
    sign = 0 if sign == "" else 1
    return f"{sign} {''.join(map(str,switch))} {''.join(map(str,mantis))} {'0'*(m - len(mantis))}"


def normalize(first, second):
    moved_element = 0
    while len(first) != 0:
        element = first.pop(-1)
        second = [element] + second
        moved_element += 1
    first = 0
    return [first, second, moved_element]


def normalize_output(first, second, moved_element, sign):
    normalize_float = f"{sign}{first}.{''.join(map(str,second))}*2^{moved_element}"
    return normalize_float


def main():
    try:
        user_input = input("Enter a number\n")
        type_of_standard = input("Choose from FP64, FP32, FP16\n")
        valid_user_input_float(user_input)
        exp_range, precision = choose_standard(type_of_standard)
        print(
            "Normalized form:",
            normalize_output(
                *normalize(get_fact_part(user_input), get_dec_part(user_input)),
                get_sign(user_input),
            ),
        )
        print(
            f"Saved as {type_of_standard}:",
            fp_standard(
                get_sign(user_input),
                *normalize(
                    get_fact_part(user_input),
                    get_dec_part(
                        user_input, precision - len(get_fact_part(user_input))
                    ),
                )[1:],
                exp_range,
                precision,
            ),
        )
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
