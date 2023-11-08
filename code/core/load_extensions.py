from os import listdir
from importlib import import_module
from os.path import exists


class Extensions:
    @staticmethod
    def check_init_pack(resource_module: str):
        if not exists(f"resources/{resource_module}/__init__.py"):
            raise FileNotFoundError(f'No __init__.py file founded in the "{resource_module}" pack !')

    def extensions(self):
        packs = listdir('resources/')
        packs.remove('__pycache__') if '__pycache__' in packs else self.nothing()
        for pack in packs:
            self.check_init_pack(resource_module=pack)
            globals()[pack] = import_module(f'resources.{pack}')
        return packs

    def nothing(self):
        pass
