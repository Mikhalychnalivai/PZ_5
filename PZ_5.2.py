# Задача 2:
# Описать функцию AddLeftDigit(D, K), добавляющую слева к числу D число K, 
# являющееся одновремнно входным и выходным, с последовательным добавлением к данному числу K слева данные цифры D1 и D2, выводя результат каждого добавления.

def add_left_digit(D, K):
    if not (0 <= D <= 9):
        raise ValueError("D должна быть цифрой (0-9).")
    if K < 0:
        raise ValueError("K должно быть неотрицательным числом.")
    
    return int(str(D) + str(K))

while True:
    try:
        D1 = int(input("Введите цифру D1: "))
        if 0 <= D1 <= 9:
            break
        else:
            print("D1 должна быть цифрой. Попробуйте снова.")
    except ValueError:
        print("Введено не число. Попробуйте снова.")

while True:
    try:
        D2 = int(input("Введите цифру D2: "))
        if 0 <= D2 <= 9:
            break
        else:
            print("D2 должна быть цифрой. Попробуйте снова.")
    except ValueError:
        print("Введено не число. Попробуйте снова.")

while True:
    try:
        K = int(input("Введите начальное число K (неотрицательное): "))
        if K >= 0:
            break
        else:
            print("K должно быть неотрицательным. Попробуйте снова.")
    except ValueError:
        print("Введено не число. Попробуйте снова.")

K = add_left_digit(D1, K)
print(f"D1: {K}")

K = add_left_digit(D2, K)
print(f"D2: {K}")
