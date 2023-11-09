from json import load, dumps
from code import read_ini


class Player:
    def __init__(self):
        pass

    @staticmethod
    def datas():
        with open(f'saves/{read_ini("USERNAME")}/datas.json', "r", encoding='utf-8') as datas:
            return load(datas)

    @property
    def money(self):
        return int(self.datas()['main']['infos']['money'])

    def add_money(self, money: int):
        data = self.datas()
        data['main']['infos']['money'] = self.money + money
        with open(f'saves/{read_ini("USERNAME")}/datas.json', 'w', encoding='utf-8') as datas:
            datas.write(dumps(data))
        return self.money

    def lost_money(self, money: int):
        data = self.datas()
        data['main']['infos']['money'] = self.money - money
        with open(f'saves/{read_ini("USERNAME")}/datas.json', 'w', encoding='utf-8') as datas:
            datas.write(dumps(data))
        return self.money
