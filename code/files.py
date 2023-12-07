from json import load, dumps


class File:
    def __init__(self, file: str | bytes):
        self.file = file
        self.scenario = None

    def read(self) -> dict or list:
        """
        Ouvre un fichier initialement spécifié en paramètres et renvoie un dictionnaire ou une liste!
        """
        new_dict = {}
        with open(file=self.file, mode='r', encoding='utf8') as file:
            if str(self.file).split('.')[-1] == 'json':
                return load(file)
            elif self.file == 'config.ini':
                for line in file.read().splitlines():
                    new_dict[self.key(line=line)] = self.val_key(line=line)
                return new_dict
            else:
                return file.read().splitlines()

    def key(self, line: str):
        """
        Renvoie la clé dans la string recu.
        Uniquement utilisé quand on lit le fichier config.ini
        """
        return line.split('=')[0].strip()

    def val_key(self, line: str):
        """
        Renvoie la valeur dans la string recu.
        Uniquement utilisé quand on lit le fichier config.ini
        """
        return line.split('=')[1].strip()

    def write(self, content: dict) -> None:
        """
        Permet de modifier un fichiers !
        Attention, il est prévu à être utilisé uniquement pour les fichier JSON !
        """
        with open(file=self.file, mode='w', encoding='utf8') as file:
            file.write(dumps(content, indent=2))
