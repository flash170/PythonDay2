# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры:
#
# [ (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}), (2, {“название”: “принтер”,
# “цена”: 6000, “количество”: 2, “eд”: “шт.”}), (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7,
# “eд”: “шт.”}) ] Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров. Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


ktovar = []
features = {'Имя': '', 'Цена': '', 'количество': '', 'Единиц': ''}
analytics = {'Имя': [], 'Цена': [], 'количество': [], 'Единиц': []}
num = 0
feature_ = None
upr = None
while True:
    upr = input('Для выхода \'Q\', Для продолжения \'Enter\', Для аналитики \'A\'').upper()
    if upr == 'Q':
        break
    num += 1
    if upr == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'Цена' or f == 'количество') else feature_
        analytics[f].append(features[f])
    ktovar.append((num, features))

ktovar = int(input("Введите количество товара "))
n = 1
mdict = []
mlist = []
manalys = {}
while n <= ktovar:
    mdict = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                  'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    mlist.append((n, mdict))
    n += 1
    manalys = dict(
        {'название': mdict.get('название'), 'цена': mdict.get('цена'), 'количество': mdict.get('количество'),
         'ед': mdict.get('ед')})
print(mlist)
print(manalys)
