from json import load, dumps


class File:
    def __init__(self, file: str | bytes):
        self.file = file
        self.scenario = None

    def read(self) -> dict or list:
        new_dict = {}
        with open(file=self.file, mode='r', encoding='utf8') as file:
            if str(self.file).split('.')[-1] == 'json':
                return load(file)
            elif self.file == 'config.ini':
                for line in file.read().splitlines():
                    new_dict[line.split('=')[0].strip()] = line.split('=')[1].strip()
                return new_dict
            else:
                return file.read().splitlines()

    def write(self, content: dict) -> None:
        with open(file=self.file, mode='w', encoding='utf8') as file:
            file.write(dumps(content, indent=2))
