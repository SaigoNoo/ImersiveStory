from code.files import File
from os import listdir
from os.path import isfile


class Sauvegardes(File):
    def sauvegarder(self):
        saves = self.read()
        saves["last_save"] = saves["last_save"] + 1
        self.write(content=saves)

    def full_file(self, quest_id: int):
        quest_id = str(quest_id).zfill(5)
        for chapter in listdir(f"scenarios/"):
            if not isfile(f"scenarios/{chapter}"):
                for quest in listdir(f"scenarios/{chapter}/"):
                    if quest_id == quest.split("-")[1].strip():
                        return f"scenarios/{chapter}/{quest}"
