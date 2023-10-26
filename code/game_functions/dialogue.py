class Dialogues():
    def __init__(self, npc: object):
        self.npc = npc

    def text(self, text_content: str):
        print(f"{self.npc['name']}: {text_content}")
