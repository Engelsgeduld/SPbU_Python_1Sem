def find(a, b):
    count = 0
    while a > b:
        a -= b
        count += 1
    return count


def main():
    while True:
        user_input = input("Введите 2 числа через пробел")
        if user_input == "exit":
            break
        inputs = [int(a) for a in user_input.split(" ")]
        print(
            f"Нахождение неплоного частного {inputs[0]} и {inputs[1]}. Результат: {find(inputs[0], inputs[1])}"
        )


if __name__ == "__main__":
    main()
