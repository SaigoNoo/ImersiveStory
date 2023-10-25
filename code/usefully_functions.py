from json import load


class UsefullyFunctions:
    def __init__(self):
        self.pack = ['main']
        self.resources = ['map', 'npc', 'skills', 'spells', 'weapons']

    def return_value(self, pack: str, value_type: str, filename: str):
        """
        This function will return a dictionary of a specific JSON file !
        :param pack:        Name of packs (folders) inside the resources folder
        :param value_type:  Name of the wanted object (npc, weapons, ...)
        :param filename:    Name of the file who contain all datas about a specific item or object
        :return:            The dictionary of the read file
        """
        if pack not in self.pack:
            raise FileExistsError(f"{pack} don't exist inside resources.\nPlease check pack names !")

        if value_type not in self.resources:
            raise FileExistsError(f"{value_type} don't exist inside resources/{pack}.\nPlease check objects names !")

        with open(fr'resources/{pack}/{value_type}/{filename}.json', 'r', encoding='utf8') as file:
            return load(file)
