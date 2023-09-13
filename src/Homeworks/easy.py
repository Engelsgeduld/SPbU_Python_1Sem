def solve(x):
    try:
        float(x)
        if x[0] == '0' and len(x) > 1 or x[0:2] == '-0':
            print('Integer cant begin with 0')
            return 0
        else:x = float(x)
    except:
        print('x must be a integer')
        return 0

    # (X^2+1)*(X^2+x)+1
    square_x = x ** 2
    result = (square_x + 1) * (square_x + x) + 1
    print(f'This is result:{result}')

def main():
    print('Calculating x^4+x^3+x^2+x+1, enter x:')
    x = input()
    while x != 'exit':
        solve(x)
        print('Exit: enter "exit"')
        x = input()
    else: print('Bye')

if __name__ == '__main__':
    main()

