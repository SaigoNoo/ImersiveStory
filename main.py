from os.path import exists
from atexit import register
from code.files import File
from time import time

if exists('scenarios/__init__.py'):
    from scenarios import load_menu
    from code.scenarios_debug import Scenarios
else:
    raise ModuleNotFoundError(
        "Impossible de charger les modules de scenarios."
        "Veuillez consulter le documentation sur <lien_à_venir>..."
    )


def reset_temp_datas():
    temp = File(file="temp.json")
    save = File(file="save.json")
    seconds = round(time()) - temp.read()['time']
    data = save.read()
    last_sec = data['player']['time']
    seconds = last_sec + seconds
    data['player']['time'] = seconds
    save.write(content=data)
    temp.write(content={})


if __name__ == '__main__':
    register(reset_temp_datas)
    Scenarios().checks_id()
    load_menu()