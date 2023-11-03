from code.core.config_files import read_ini


class Actions:
    def __init__(self):
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
        self.command = None

    def valid_command(self, command: str):
        if len(command) == 0:
            return False
        if command[0] == read_ini(key="PREFIX") and command[1::] in self.commands:
            self.command = command
            return True
