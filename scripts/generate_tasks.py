import json
import sys, os
from string import ascii_uppercase
import re
from itertools import product as iter_product, permutations

""" скрипт генерирует структуру словаря для базы игры ключ словаря - строка (подсказка) 
(или наверное на будущее - кортеж (строка, имя аудио файла для воспроизведения)).
Подсказка может быыть прямой - для сопоставление юзером соответсвия - '1' -ищет 1, 'А' - ищет 'А',
а может быть косвенной - '1+1', в поле ответов пользователь среди вариантов допустим  3, 8, 1, 2, 5
должен найти правильный"""

directory = os.path.dirname(__file__)
directory = directory + r'\..\data\tasks'

def generate_digits(name_game='цифры', level=None, knowledge_category=1):  # цифры
    game_data =  {f'{n}': f'{n}' for n in range(10)}
    return {'name_game':name_game, 'level':level, 'knowledge category': knowledge_category, 'data': game_data}


def generate_upp_letters(name_game='буквы',level=None, knowledge_category=2): # заглавные буквы
    game_data = {chr(l): chr(l) for l in range(ord('А'), ord('Я') + 1)}
    return {'name_game':name_game,'level':level, 'knowledge category': knowledge_category, 'data':game_data}


def generate_upp_disyllabic_syllables(text='', name_game='слоги', level=1, knowledge_category=3):
    """ двусложные слоги """

    vowels = 'АЕЁИОУЫЭЮЯ'
    consonants = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    special = 'ЬЪ'
    game_data = {}
    if text:
        for word in text.split():
            word = re.sub(rf'[^А-Я]','',word.upper())
            word_split = re.sub(fr'([{vowels}])',r'\1-',word)
            syllables = list(filter(lambda w: len(w)==2 and w[1] in vowels, word_split.split('-')))
            game_data |= {sy:sy for sy in syllables}
    else:
        consonants = consonants.replace('Й','')
        vowels = vowels.replace('Ё','')
        syllables = map(''.join, iter_product(list(consonants),list(vowels)))
        game_data |= {sy: sy for sy in syllables}
    return {'name_game':name_game,'level':level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_upp_open_trisyllabic_syllables(text='', name_game='слоги', level=2, knowledge_category=3):
    """ трёхсложные открытые слоги """

    vowels = 'АЕЁИОУЫЭЮЯ'
    consonants = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    special = 'ЬЪ'
    game_data = {}
    if text:
        for word in text.split():
            word = re.sub(rf'[^А-Я]','',word.upper())
            word_split = re.sub(fr'([{vowels}])',r'\1-',word)
            syllables = list(filter(lambda w: len(w)==3, word_split.split('-')))
            game_data |= {sy:sy for sy in syllables}
    else:
        consonants = consonants.replace('Й','')
        vowels = vowels.replace('Ё','')
        syllables = map(''.join, iter_product(list(consonants),list(consonants),list(vowels)))
        game_data |= {sy: sy for sy in syllables}
    return {'name_game':name_game, 'level':level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_upp_close_trisyllabic_syllables(text='', name_game='слоги', level=3, knowledge_category=3):
    """ трёхсложные закрытые слоги """

    vowels = 'АЕЁИОУЫЭЮЯ'
    consonants = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    special = 'ЬЪ'
    game_data = {}
    if text:
        for word in text.split():
            word = re.sub(rf'[^А-Я]','',word.upper())
            word_split = re.sub(fr'([{vowels}][{consonants}])',r'\1-',word)
            conditions = lambda w: len(w)==3 and w[0] not in vowels and w[-1] not in vowels
            syllables = list(filter(conditions, word_split.split('-')))

            game_data |= {sy: sy for sy in syllables}
    else:
        consonants = consonants.replace('Й','')
        vowels = vowels.replace('Ё','')
        syllables = map(''.join, iter_product(list(consonants),list(vowels),list(consonants)))
        game_data |= {sy: sy for sy in syllables}
    return {'name_game':name_game, 'level':level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_addition(digit_number_x=1,digit_number_y=1, name_game='сложение', level=None, knowledge_category=4):
    game_data = {}
    min_x, max_x = 10**(digit_number_x-1), 10**digit_number_x
    min_y, max_y = 10**(digit_number_y-1), 10**digit_number_y
    for x in range(min_x,max_x):
        for y in range(min_y, max_y):
            game_data[f'{x} + {y}'] = f'{x+y}'
    return {'name_game':name_game, 'level':level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_subtraction(digit_number_x=1,digit_number_y=1, name_game='вычитание', level=None, knowledge_category=5):
    game_data = {}
    min_x, max_x = 10**(digit_number_x-1), 10**digit_number_x
    min_y, max_y = 10**(digit_number_y-1), 10**digit_number_y
    for x in range(min_x,max_x):
        for y in range(min_y, max_y):
            if x-y > 0:
                game_data[f'{x} - {y}'] = f'{x-y}'
    return {'name_game': name_game, 'level': level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_multiplication(digit_number_x=1,digit_number_y=1,  name_game='умножение', level=None, knowledge_category=6):
    game_data = {}
    min_x, max_x = 10**(digit_number_x-1), 10**digit_number_x
    min_y, max_y = 10**(digit_number_y-1), 10**digit_number_y
    for x in range(min_x,max_x):
        for y in range(min_y, max_y):
            if x!=1 and y!=1:
                game_data[f'{x} х {y}'] = f'{x*y}'
    return {'name_game': name_game, 'level': level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_division(digit_number_x=1,digit_number_y=1, name_game='деление', level=None, knowledge_category=7):
    game_data = {}
    min_x, max_x = 10**(digit_number_x-1), 10**digit_number_x
    min_y, max_y = 10**(digit_number_y-1), 10**digit_number_y
    for x in range(min_x,max_x):
        for y in range(min_y, max_y):
            if all([x%y == 0, y!=1, x!=y]) :
                game_data[f'{x} : {y}'] = f'{x//y}'
    return {'name_game': name_game, 'level': level, 'knowledge category': knowledge_category, 'data': game_data}

def generate_exponentiation(digit_number_x=1,pow_number_y=2, name_game='квадраты', level=None, knowledge_category=8):
    game_data = {}
    min_x, max_x = 10 ** (digit_number_x - 1), 10 ** digit_number_x
    y = pow_number_y
    for x in range(min_x, max_x):
        if x > 1:
            game_data[f'{x} ^ {y}'] = f'{x**y}'
    return {'name_game': name_game, 'level': level, 'knowledge category': knowledge_category, 'data': game_data}

if __name__ == '__main__':
    text = '''Буря мглою небо кроет, Вихри снежные крутя; То, как зверь, она завоет, То заплачет, как дитя, То по кровле обветшалой Вдруг соломой зашумит, То, как путник запоздалый, К нам в окошко застучит.
    Наша ветхая лачужка И печальна и темна. Что же ты, моя старушка, Приумолкла у окна? Или бури завываньем Ты, мой друг, утомлена, Или дремлешь под жужжаньем Своего веретена?
    Выпьем, добрая подружка Бедной юности моей, Выпьем с горя; где же кружка? Сердцу будет веселей. Спой мне песню, как синица Тихо за морем жила; Спой мне песню, как девица За водой поутру шла.
    Буря мглою небо кроет, Вихри снежные крутя; То, как зверь, она завоет, То заплачет, как дитя. Выпьем, добрая подружка Бедной юности моей, Выпьем с горя: где же кружка? Сердцу будет веселей.'''

    def recursive_print_dct(data: dict, sep=' ', count_sep=0):
        for k, v in data.items():
            if type(v) is dict:
                out_str = f'{sep*count_sep}{k}:'
                print(out_str)
                recursive_print_dct(v, count_sep=count_sep+len(out_str)+1)
            else:
                print(f'{sep*count_sep}{k}: {v}')

    file_names = {'digits.json': generate_digits(),
                  'upp_ltrs.json': generate_upp_letters(),
                  'upp_2_slbls.json': generate_upp_disyllabic_syllables(text),
                  'upp_o_3_slbls.json': generate_upp_open_trisyllabic_syllables(text),
                  'upp_c_3_slbls.json': generate_upp_close_trisyllabic_syllables(text),
                  'add_digits11.json': generate_addition(1,1, level=1),
                  'add_digits21.json': generate_addition(2,1, level=2),
                  'add_digits22.json': generate_addition(2,2, level=3),
                  'add_digits32.json': generate_addition(3,2, level=4),
                  'add_digits33.json': generate_addition(3,3, level=5),
                  'sub_digits11.json': generate_subtraction(1,1, level=1),
                  'sub_digits21.json': generate_subtraction(2,1, level=2),
                  'sub_digits22.json': generate_subtraction(2,2, level=3),
                  'sub_digits31.json': generate_subtraction(3,1, level=4),
                  'sub_digits32.json': generate_subtraction(3,2, level=5),
                  'sub_digits33.json': generate_subtraction(3,3, level=6),
                  'mult_digits11.json': generate_multiplication(1, 1, level=1),
                  'mult_digits21.json': generate_multiplication(2, 1, level=2),
                  'div_digits11.json': generate_division(1, 1, level=1),
                  'div_digits21.json': generate_division(2, 1, level=2),
                  'exponentiation11.json': generate_exponentiation (1, 2, level=1),
                  'exponentiation21.json': generate_exponentiation(2, 2, level=2),
                  'exponentiation22.json': generate_exponentiation(1, 3, name_game='кубы', level = 2),
                  'exponentiation23.json': generate_exponentiation(2, 3, name_game='кубы', level=3),
                  }

    for name, data in file_names.items():
        with open(fr'{directory}\{name}','w',encoding='utf-8') as file:
            json.dump(data,file, ensure_ascii=False)
    for name,data in file_names.items():
        with open(fr'{directory}\{name}','r',encoding='utf-8') as file:
            assert data == json.load(file)
            print(f'{name} +')
            # recursive_print_dct(data)
            # input(f'{'-'*20}')

