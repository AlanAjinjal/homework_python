def real_date(day, month, year):
    #Списки месяцев по количеству дней в них.
    month31 = [1,3,5,7,8,10,12]
    month30 = [4,6,9,11]

    if month in range(1, 13):
        # Проверка на соответствие дня количеству дней в месяце.
        if (month in month31 and day <= 31) or (month in month30 and day <= 30):
            return True # Дата верна
        # Для 29 февраля високосного года, и с 1 по 28 февраля
        elif month == 2 and (day == 29 and year % 4 == 0 or day < 29):
            return True # Дата верна
    return False # По умолчанию дата неверна

print(real_date(7, 11, 2021))
print(real_date(29, 2, -20))
print(real_date(30, 9, 2021))
print(real_date(31, 9, 2021))