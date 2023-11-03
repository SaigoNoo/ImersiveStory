from json import load


class NPC:
    def __init__(self, npc: str):
        self.npc = self.actor_datas(npc_name=npc)
        self.choices_values = None

    def actor_datas(self, npc_name: str):
        with open(f'resources/main/npc/{npc_name}.json', 'r') as npc:
            return load(npc)

    def text(self, text_content: str):
        print(f"{self.npc['name']}: {text_content}")

    def choices(self, **kwargs):
        self.choices_values = kwargs.keys()
        for choice in kwargs.items():
            print(f"{choice[0]}: {choice[1]}")

    def choice_exist(self, key: str):
        return key in self.choices_values
