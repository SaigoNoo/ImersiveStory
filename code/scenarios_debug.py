from os import listdir
from os.path import isfile


class Scenarios:
    def __init__(self):
        pass

    @staticmethod
    def checks_id():
        table_of_ids = []
        for chapters in listdir("scenarios"):
            if not isfile(f"scenarios/{chapters}"):
                for quest in listdir(f"scenarios/{chapters}"):
                    if (isfile(f"scenarios/{chapters}/{quest}") and
                            f"scenarios/{chapters}/{quest}".split(".")[1] == "isf"):
                        if quest.split(' - ')[1] not in table_of_ids:
                            table_of_ids.append(quest.split(" - ")[1])
                        else:
                            raise NameError(
                                f"Quest {quest} ayant pour identifiant {quest.split(' - ')[1]} est déjà utilisé ! "
                                f"Veuillez utiliser un QID diffèrent pour le scenario.")
