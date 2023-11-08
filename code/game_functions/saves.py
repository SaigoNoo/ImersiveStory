from json import dumps
from os.path import exists
from os import mkdir
from code import read_ini


class Save:
    def __init__(self):
        self.user = read_ini(key="USERNAME")

        if self.is_username_none():
            raise ValueError("The USERNAME variable inside the config.ini file is empty.\nPlease fill it !")

        if not self.save_exist():
            self.create_save()

    def is_username_none(self):
        return self.user is None

    def save_exist(self):
        return exists(f'saves/{self.user}/datas.json')

    def create_save(self):
        syntax = {
            "main": {
                "infos": {
                    "money": 250,
                    "name": "Méliodas",
                    "class": "warrior"
                }
            }
        }
        mkdir(f'saves/{self.user}')
        with open(f'saves/{self.user}/datas.json', 'a') as savefile:
            savefile.write(dumps(syntax))
