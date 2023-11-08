from code.core.functions import read_ini


class Action:
    def __init__(self, command: str):
        self.commands = [
            "start",
            "stop",
            "save",
            "load",
            "player_stats",
            "ennemy_stats",
            "attack",
            "items"
        ]
        self.command = command
        self.valid_command()

    def valid_command(self):
        return self.command[0] == read_ini(key="PREFIX") and self.command[1::] in self.commands
