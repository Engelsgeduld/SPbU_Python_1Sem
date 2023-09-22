from random import randint


def game(secret, user_input):
    if user_input == secret: return None
    cows, bulls = 0, 0
    for num in user_input:
        if num in secret:
            if user_input.index(num) == secret.index(num):
                bulls += 1
            else:
                cows += 1
    return cows, bulls


def main():
    n = [int(x) for x in str(randint(1000, 10000))]
    print("Вас привествует игра Быки и Коровы. Число уже загадано")
    user_input = [int(x) for x in input("Введите ваше предположение \n")]

    while len(user_input) !=4:
        print("Число должно быть четырех значное")
        user_input = [int(x) for x in input()]
        
    while game(n, user_input) is not None:
        cows, bulls = game(n, user_input)
        print(f"Результат: Коров - {cows} Быков - {bulls}")
        user_input = [int(x) for x in input("Продолжайте, вы все ближе к ответу \n")]
    else:
        print("Поздравляем, вы выйграли")


if __name__ == "__main__":
    main()
