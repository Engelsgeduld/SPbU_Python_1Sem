def prime(number):
    return number > 1 and all(
        number % i != 0 for i in range(2, int(number**1 / 2) + 1)
    )


def prime_numbers(number):
    result = [a for a in range(2, number) if prime(a)]
    return result


if __name__ == "__main__":
    while True:
        print("Введите число:")
        user_input = input()
        if user_input == "exit":
            break
        res = ",".join(map(str, prime_numbers(int(user_input))))
        print(f"Простые числа: {res}")
