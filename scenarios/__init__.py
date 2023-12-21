from code.game.choices import Choices
from curses import wrapper
from code.main import Main
from code.files import File
from time import sleep
from code.game.saves import Sauvegardes
from time import time


def choice(**kwargs):
    menu = []
    for element in kwargs.values():
        menu.append(element)
    return wrapper(Choices().run, menu, "Menu de jeu ", None, True)


def load_menu():
    quest_file = Sauvegardes(file="save.json").full_file
    saves = File("save.json")
    menu_do = choice(a="new_game", b="load_last_save", c="left_game")
    temp = File(file="temp.json")
    if menu_do == "new_game":
        datas = temp.read()
        datas["time"] = round(time())
        temp.write(content=datas)
        saves.write(content={
            "last_save": 0,
            "player": {
                "xp": 1,
                "time": 0,
                "money": 0
            }
        })
        Main(file=quest_file(quest_id=1)).play_scenario()
        print("Sauvegarde en cours...")
        sleep(2)

        while choice(a="Continuer", b="Quitter") == "Continuer":
            Main(file=quest_file(quest_id=saves.read()['last_save'] + 1)).play_scenario()

    elif menu_do == "load_last_save":
        datas = temp.read()
        datas["time"] = round(time())
        temp.write(content=datas)
        try:
            Main(file=quest_file(quest_id=saves.read()['last_save'] + 1)).play_scenario()
        except TypeError:
            Main(file=quest_file(quest_id=saves.read()['last_save'])).play_scenario(no_save=True)

        print("Sauvegarde en cours...")
        sleep(2)

        while choice(a="Continuer", b="Quitter") == "Continuer":
            try:
                Main(file=quest_file(quest_id=saves.read()['last_save'] + 1)).play_scenario()
            except TypeError:
                Main(file=quest_file(quest_id=saves.read()['last_save'])).play_scenario(no_save=True)
            print("Sauvegarde en cours...")
            sleep(2)
    elif menu_do == "left_game":
        exit()
