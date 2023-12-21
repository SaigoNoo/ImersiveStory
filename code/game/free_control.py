from code.game.choices import Choices
from curses import wrapper
from code.game.texte import Texte


class FreeControl:
    def __init__(self):
        self.condition = True

    def choice(self, **kwargs):
        menu = []
        for element in kwargs.values():
            menu.append(element)
        return wrapper(Choices().run, menu, "Choix ", None, True)

    def run_mode(self):
        while self.condition:
            command = input("action (help) > ")
            if command == "" or command == "help":
                menu = self.choice(a="stats", b="exit")
                if menu == "stats":
                    Texte().stats()
                elif menu == "exit":
                    exit()
