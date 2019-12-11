import random


def city_find(first_letter, cities):
    for key in cities:
        if cities[key] and key[0] == first_letter:
            return key
    return ''


def get_last_of(city):
    ending = city[-1].title()
    if ending in 'ЁЪЫЬ':
        ending = city[-2].title()
    return ending


DB_FILENAME = 'cities.txt'
MSG_EMPTY_INPUT = 'Надо город назвать'
MSG_WRONG_FIRST_LETTER = 'Надо назвать город на букву {}'
MSG_CITY_USED = 'Такой город уже был'
MSG_NO_SUCH_CITY = 'Такого города нет'


if __name__ == "__main__":
# Внутренний тип данных: словарь, где город -- ключ, а значение True/False -- был ли город в игре.
# Пример:
# {'Антверпен': True, 'Москва': False, 'Новый Уренгой': True, 'Йорк': True, 'Калининград': True}
    cities = []
    with open(DB_FILENAME, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            cities.append(line.strip())
    random.shuffle(cities)
    cities_bank = {}.fromkeys(cities, True)

    last_named_city = ''

    while True:
        try:
            current_city = input('Пользователь: ').strip().title()
        except KeyboardInterrupt:
            print('\nПрограмма: Мы ещё доиграем.')
            break
        if 'сдаюсь' in current_city.lower():
            print('Программа: Ха! Моя победа!')
            break

        if not current_city:
            print(MSG_EMPTY_INPUT)
            continue

        if last_named_city:
            required_1st_letter = get_last_of(last_named_city)
            if current_city[0] != required_1st_letter:
                print(MSG_WRONG_FIRST_LETTER.format(required_1st_letter))
                continue

        check_city = cities_bank.get(current_city)
        if check_city is None:
            print(MSG_NO_SUCH_CITY)
            continue
        elif not check_city:
            print(MSG_CITY_USED)
            continue

        cities_bank[current_city] = False

        bot_reply_1st_letter = get_last_of(current_city)
        bot_reply_city = city_find(bot_reply_1st_letter, cities_bank)

        if bot_reply_city:
            print(f'Программа: {bot_reply_city}')
            last_named_city = bot_reply_city
            cities_bank[bot_reply_city] = False
        else:
            print('Я не нашла город. Ты победил :\'(')
            break
