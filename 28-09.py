from datetime import datetime, timedelta

def dnevnik(list, start):
    date = datetime.strptime(start, '%d.%m.%Y')
    file = open("dnevnik.txt", "w", encoding="utf-8")
    for item in list:
        file.write(datetime.strftime(date, '%d.%m.%Y') + ': ' + item + '\n')
        date = date + timedelta(days=1)
    file.close()

dnevnik(['Сегодня я ухожу в плавание',
         'Наш корабль потерпел бедствие.'], '31.12.2022')