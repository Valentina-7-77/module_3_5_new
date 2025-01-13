# Рекурсивное умножение цифр
# Напишите функцию get_multiplied_digits и параметр number в ней
def get_multiplied_digits(number):
    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё
    str_number = str(number)
    if len(str_number) > 1:

        # Cоздайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int)
        first = int(str_number[0])
        # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
        # Таким образом вы умножите первую цифру числа на результат работы
        # этой же функции с числом, но уже без первой цифры.
        return first * get_multiplied_digits(int(str_number[1:]))
    # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first
    else:
        return max(1, int(str_number))


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)

