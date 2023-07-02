class Film:
    def __init__(self, title, director, county):
        self.title = title
        self.director = director
        self.country = county

    def info(self):
        print('Информация о фильме:\n%s\n%s\n%s' %
              ('Название:'.ljust(10) + self.title,
               'Режиссёр:'.ljust(10) + self.director,
               'Страна:'.ljust(10) + self.country))

    def cinema(self, name):
        print(f'Фильм "{self.title}" в прокате в кинотеатре {name}')

    def online(self, name):
        print(f'Фильм "{self.title}" онлайн на {name}')

    def lang(self, lang):
        print(f'Фильм "{self.title}" переведён на {lang}')


class Horror(Film):
    def scare(self, subj):
        print(f'Ужастик "{self.title}" страшен {subj}')


class Comedy(Film):
    def funny(self, subj):
        print(f'Комедия "{self.title}" смешна {subj}')


film1 = Film('Переводчик', 'Гай Ричи', 'США')
film2 = Film('Такси', 'Жерар Пирес', 'Франция')
film3 = Film('Терминатор', 'Джеймс Кэмерон', 'США')

film1.info()
film1.cinema('Октябрь')
film1.online('Амедиатека')
film1.lang('русский')

print()

film2.info()
film2.cinema('Пушка')
film2.online('ИВИ')
film2.lang('английский')

print()

film3.info()
film3.cinema('Художественный')
film3.online('Кинопоиск')
film3.lang('китайский')

print()

film4 = Horror('Пятница 13', 'Шон С. Каннингэм', 'США')
film5 = Comedy('Ананасовый экспресс', 'Дэвид Гордон Грин', 'США')

film4.info()
film4.cinema('Художественный')
film4.online('ИВИ')
film4.lang('китайский')
film4.scare('кровавыми расправами')

print()

film5.info()
film5.cinema('Пушка')
film5.online('Кинопоиск')
film5.lang('английский')
film5.funny('глупыми шутками')