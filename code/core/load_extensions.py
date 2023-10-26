from os import listdir
from importlib import import_module


class Extensions:
    def pack_exist(self, pack_nr: int):
        packs = listdir('resources/')
        if pack_nr > len(packs):
            return False
        else:
            return True

    def list_packs(self):
        packs = listdir('resources/')
        if len(packs) > 1:
            for [index, pack] in enumerate(packs, 1):
                print(f'{str(index).zfill(2)}) {pack}')
            while self.pack_exist(int(input('Quel numéro de pack faut-il charger: '))):
                pass
        else:
            return packs

    def load_extensions(self, packs: list):
        for pack in packs:
            globals()[pack] = import_module(f'resources.{pack}')
            globals()['module'] = pack
