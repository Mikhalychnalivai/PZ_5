# Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
# Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится ноль?

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def count_steps_to_zero(n):
    steps = 0
    current = n

    while current > 0:
        digit_sum = sum_of_digits(current)
        current -= digit_sum
        steps += 1

    return steps

n = input("Введите число: ")

while True:
    try:
        n = int(n)
        if n < 0:
            print("Число должно быть неотрицательным!")
            n = input("Введите число: ")
            continue
        break
    except ValueError:
        print("Введено не число!")
        n = input("Введите число: ")

result = count_steps_to_zero(n)
print(f"Через {result} действий получится нуль.")
