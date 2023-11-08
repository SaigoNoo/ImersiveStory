from json import load


class NPC:
    def __init__(self, npc: str):
        self.npc = npc
        self.choices = None

    def actor_datas(self):
        with open(f'resources/main/npc/{self.npc}.json', 'r') as npc:
            return load(npc)

    def text(self, text_content: str):
        return f"{self.actor_datas()['name']}: {text_content}"
