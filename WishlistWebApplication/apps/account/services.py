"""
    get_random_profile_image была построена на функциях glob и findall
соответствующих модулей. В процессе разработки выяснилось, что данное
решение не оптимально и решать через функцию такую задачу может быть
не рационально, особенно в таком виде.
    Решение необходимо переработать в соответствии с наиболее
лучшими практиками в области подобных задач.

"""

# from glob import glob

from random import choice

# from re import findall



# для запуска функциии get_random_profile_image на пк разработчика путь для оператора glob должен соответствовать полному
# пути, как в примере ниже
# path = 'C:/DjangoProjects/WishlistWebApplication/venv/src/WishlistWebApplication/media_cdn/wlwap/fundogs/*.jpg'


def get_random_profile_image():
    """
    Функция вызова рандомной картинки из базы картинок.
    Применять как заглушку на случай, если пользователь не
    загрузил свое фото профиля.
    Название картинок должно удовлетворять требованию:
    номер картирки.jpg
    """

    listofpics = ['man.jpg', 'woman.jpg']
    # itemlist = []
    # for pth in listofpics:
    #     imgext = pth.split("fundogs/")
    #     for item in imgext:
    #         itemlist.append(findall(pattern=r'(\d\.jpg)', string=item))
    randompic = choice(listofpics)
    return randompic

