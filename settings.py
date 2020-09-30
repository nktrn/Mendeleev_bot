from mendeleev_element import Element

# picture height and width
WIDTH = 180
HEIGHT = 200

# bot url
URL = '@MendeleevText_bot'

# colors
GREEN = (65, 195, 159)
ORANGE = (234, 135, 78)
PURPLE = (191, 155, 183)
BLUE = (13, 168, 212)
DARKBLUE = (85, 146, 200)
BEIGE = (224, 193, 162)
DARKPURPLE = (198, 81, 172)
RED = (225, 127, 142)
YELLOW = (237, 213, 3)
LIGHTGREEN = (183, 189, 125)
BLACK = (0, 0, 0)

# font
FONT_URL_REGULAR = 'font/Roboto-Regular.ttf'
FONT_URL_BOLD = 'font/Roboto-Bold.ttf'
FONT_INDEX_SIZE = 30
FONT_NAME_SIZE = 70
FONT_FULLNAME_SIZE = 17
FONT_BOT_URL_SIZE = 10

# offset
OFFSET = 2

# Mendeleev elements
elements = {
    'h': Element('H', 'Водовород', 1, ORANGE),
    'c': Element('C', 'Углерод', 6, ORANGE),
    'n': Element('N', 'Азот', 7, ORANGE),
    'o': Element('O', 'Кислород', 8, ORANGE),
    'p': Element('P', 'Фосфор', 15, ORANGE),
    's': Element('S', 'Сера', 16, ORANGE),
    'se': Element('Se', 'Селений', 34, ORANGE),
    'li': Element('Li', 'Литий', 3, DARKBLUE),
    'na': Element('Na', 'Натрий', 11, DARKBLUE),
    'k': Element('K', 'Катериний', 19, DARKBLUE),
    'rb': Element('Rb', 'Рубидий', 37, DARKBLUE),
    'cs': Element('Cs', 'Цезний', 55, DARKBLUE),
    'fr': Element('Fr', 'Франций', 87, DARKBLUE),
    'be': Element('Be', 'Беррилий', 4, BEIGE),
    'mg': Element('Mg', 'Магний', 12, BEIGE),
    'ca': Element('Ca', 'Кальций', 20, BEIGE),
    'sr': Element('Sr', 'Стронций', 38, BEIGE),
    'ba': Element('Ba', 'Барий', 56, BEIGE),
    'ra': Element('Ra', 'Радий', 88, BEIGE),
    'sc': Element('Sc', 'Скандий', 21, YELLOW),
    'ti': Element('Ti', 'Титан', 22, YELLOW),
    'v': Element('V', 'Ванадий', 23, YELLOW),
    'cr': Element('Cr', 'Хром', 24, YELLOW),
    'mn': Element('Mn', 'Марганец', 25, YELLOW),
    'fe': Element('Fe', 'Железо', 26, YELLOW),
    'co': Element('Co', 'Кобальт', 27, YELLOW),
    'ni': Element('Ni', 'Никель', 28, YELLOW),
    'cu': Element('Cu', 'Мель', 29, YELLOW),
    'zn': Element('Zn', 'Цинк', 30, YELLOW),
    'y': Element('Y', 'Иттрий', 39, YELLOW),
    'zr': Element('Zr', 'Цирконий', 40, YELLOW),
    'nb': Element('Nb', 'Ниобий', 41, YELLOW),
    'mo': Element('Mo', 'Молибден', 42, YELLOW),
    'tc': Element('Tc', 'Технеций', 43, YELLOW),
    'ru': Element('Ru', 'Рутений', 44, YELLOW),
    'rh': Element('Rh', 'Родий', 45, YELLOW),
    'pd': Element('Pd', 'Палладий', 46, YELLOW),
    'ag': Element('Ag', 'Серебро', 47, YELLOW),
    'cd': Element('Cd', 'Кадмий', 48, YELLOW),
    'lu': Element('Lu', 'Лютений', 71, YELLOW),
    'hf': Element('Hf', 'Гафний', 72, YELLOW),
    'ta': Element('Ta', 'Тантал', 73, YELLOW),
    'w': Element('W', 'Вальфрам', 74, YELLOW),
    're': Element('Re', 'Рений', 75, YELLOW),
    'os': Element('Os', 'Осмий', 76, YELLOW),
    'ir': Element('Ir', 'Ирилий', 77, YELLOW),
    'pt': Element('Pt', 'Платина', 78, YELLOW),
    'au': Element('Au', 'Золото', 79, YELLOW),
    'hg': Element('Hg', 'Ртуть', 80, YELLOW),
    'lr': Element('Lr', 'Лоуренсий', 103, YELLOW),
    'rf': Element('Rf', 'Резерфордий', 104, YELLOW),
    'db': Element('Db', 'Дубний', 105, YELLOW),
    'sg': Element('Sg', 'Сиборгий', 106, YELLOW),
    'bh': Element('Bh', 'Борий', 107, YELLOW),
    'hs': Element('Hs', 'Хассий', 108, YELLOW),
    'mt': Element('Mt', 'Мейтнерий', 109, YELLOW),
    'ds': Element('Ds', 'Дармштадтий', 110, YELLOW),
    'rg': Element('Rg', 'Рентгений', 111, YELLOW),
    'cn': Element('Cn', 'Коперниций', 112, YELLOW),
    'he': Element('He', 'Гелий', 2, DARKBLUE),
    'ne': Element('Ne', 'Неон', 10, DARKBLUE),
    'ar': Element('Ar', 'Аргон', 18, DARKBLUE),
    'kr': Element('Kr', 'Криптон', 36, DARKBLUE),
    'xe': Element('Xe', 'Ксеон', 54, DARKBLUE),
    'rn': Element('Rn', 'Радон', 86, DARKBLUE),
    'f': Element('F', 'Фтор', 9, PURPLE),
    'cl': Element('Cl', 'Хлор', 17, PURPLE),
    'br': Element('Br', 'Бром', 35, PURPLE),
    'i': Element('I', 'Йод', 53, PURPLE),
    'b': Element('B', 'Бор', 5, PURPLE),
    'si': Element('Si', 'Кремний', 14, GREEN),
    'ge': Element('Ge', 'Германий', 32, GREEN),
    'as': Element('As', 'Мышьяк', 33, GREEN),
    'sb': Element('Sb', 'Сурьма', 51, GREEN),
    'te': Element('Te', 'Теллур', 52, GREEN),
    'po': Element('Po', 'Поланий', 84, GREEN),
    'al': Element('Al', 'Алюминий', 13, LIGHTGREEN),
    'ga': Element('Ga', 'Галлий', 31, LIGHTGREEN),
    'in': Element('In', 'Индий', 49, LIGHTGREEN),
    'sn': Element('Sn', 'Олово', 50, LIGHTGREEN),
    'tl': Element('Tl', 'Таллий', 81, LIGHTGREEN),
    'pb': Element('Pb', 'Свинец', 82, LIGHTGREEN),
    'bi': Element('Bi', 'Висмут', 83, LIGHTGREEN),
    'lv': Element('Lv', 'Ливерморий', 116, LIGHTGREEN),
    'la': Element('La', 'Лантан', 57, DARKPURPLE),
    'ce': Element('Ce', 'Церий', 58, DARKPURPLE),
    'pr': Element('Pr', 'Празеодим', 59, DARKPURPLE),
    'nd': Element('Nd', 'Неодим', 60, DARKPURPLE),
    'pm': Element('Pm', 'Прометий', 61, DARKPURPLE),
    'sm': Element('Sm', 'Самарий', 62, DARKPURPLE),
    'eu': Element('Eu', 'Европий', 63, DARKPURPLE),
    'gd': Element('Gd', 'Гадолиний', 64, DARKPURPLE),
    'tb': Element('Tb', 'Тербий', 65, DARKPURPLE),
    'dy': Element('Dy', 'Димпрозий', 66, DARKPURPLE),
    'ho': Element('Ho', 'Гольмий', 67, DARKPURPLE),
    'er': Element('Er', 'Эрбий', 68, DARKPURPLE),
    'tm': Element('Tm', 'Тулий', 69, DARKPURPLE),
    'yb': Element('Yb', 'Иттербий', 70, DARKPURPLE),
    'ac': Element('Ac', 'Актиний', 89, RED),
    'th': Element('Th', 'Торий', 90, RED),
    'pa': Element('Pa', 'ПРотактиний', 91, RED),
    'u': Element('U', 'Уран', 92, RED),
    'np': Element('Np', 'Нептуний', 93, RED),
    'pu': Element('Pu', 'Плутоний', 94, RED),
    'am': Element('Am', 'Америций', 95, RED),
    'cm': Element('Cm', 'Кюрий', 96, RED),
    'bk': Element('Bk', 'Берклий', 97, RED),
    'cf': Element('Cf', 'Калифорний', 98, RED),
    'es': Element('Es', 'Эйнштений', 99, RED),
    'fm': Element('Fm', 'Фермий', 100, RED),
    'md': Element('Md', 'Менделевий', 101, RED),
    'no': Element('No', 'Нобелий', 102, RED),
    'a': Element('A', 'Апаровий', 117, ORANGE),
    'd': Element('D', 'Дамний', 118, PURPLE),
    'e': Element('E', 'Евклидий', 119, DARKBLUE),
    'g': Element('G', 'Гетельманий', 120, DARKPURPLE),
    'j': Element('J', 'Жорий', 121, GREEN),
    'l': Element('L', 'Любовий', 122, LIGHTGREEN),
    'm': Element('M', 'Марсианий', 123, RED),
    'q': Element('Q', 'Курилий', 124, RED),
    'r': Element('R', 'Ремений', 125, BLUE),
    't': Element('T', 'Тесаковий', 126, BEIGE),
    'x': Element('X', 'Сьяолаошу', 127, GREEN),
    'z': Element('Z', 'Зелений', 128, ORANGE),
}
