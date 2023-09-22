def gcd(num1, num2):
    if num2 == 0: return num1
    return gcd(num2, num1%num2)

def all_nums(n):
    nums = []
    for den in range(2,n+1):
        for nom in range(1,den):
            if gcd(nom,den) == 1:
                nums.append([nom,den])
    return nums

def main():
    print("Нахождение всех простых несократимых дробей, заключенных между 0 и 1, знаменатели которых не превышают N")
    n = input("Введите N \n")
    if n.isdigit(): n = int(n)
    else:
        exit(print("Неверный ввод N"))

    print("Результат:\n"+"\n".join([str(nom)+"/"+str(den) for nom, den in all_nums(n)]))

if __name__ == "__main__":
    main()