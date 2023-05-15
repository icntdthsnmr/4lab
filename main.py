def z1(number):
    if number % 3 == 0:
        return True
    else:
        return False


def z2():
    try:
        number = float(input("Введите число: "))
        if number == 0:
            raise ZeroDivisionError
        res = 100 / number
        return res
    except ValueError:
        print("Вы ввели не число.")
    except ZeroDivisionError:
        print("На ноль делить нельзя.")


def z3(date_str):
    day, month, year = map(int, date_str.split("."))
    if day * month == year % 100:
        return True
    else:
        return False


def z4(number):
    length = len(number)
    if length % 2 != 0:  # проверяем, что длина номера четная
        return False
    h_length = length // 2
    first_sum = sum(map(int, number[:h_length]))
    second_sum = sum(map(int, number[h_length:]))
    return first_sum == second_sum

