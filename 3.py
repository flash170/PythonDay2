# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

slist = ['Зима', 'Весна', 'Лето', 'Осень']
sdict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц по номеру "))
if month ==1 or month == 12 or month == 2:
        print(sdict.get(1))
        print(slist[0])
elif month == 3 or month == 4 or month ==5:
    print(sdict.get(2))
    print(slist[1])
elif month == 6 or month == 7 or month == 8:
    print(sdict.get(3))
    print(slist[2])

elif month == 9 or month == 10 or month == 11:
    print(sdict.get(4))
    print(slist[3])
else:
        print("Нет такого месяца")