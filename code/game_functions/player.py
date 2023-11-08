from json import load
from code import read_ini


class Player:
    def __init__(self):
        pass

    @staticmethod
    def datas():
        with open(f'saves/{read_ini("USERNAME")}/datas.json', "r") as datas:
            return load(datas)

    @property
    def money(self):
        return self.datas()['main']['infos']['money']
