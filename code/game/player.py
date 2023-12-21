from code.files import File


class Player(File):
    def add_xp(self, xps: int):
        content = self.read()
        content["player"]["xp"] = xps
        self.write(content=content)

    def get_level(self):
        level_steps = [1, 100, 300, 900, 1200, 1500, 2000, 2500]
        xps = self.read()["player"]["xp"]
        last_index = 0
        for step in level_steps:
            if xps >= step:
                last_index = level_steps.index(step) + 1
            else:
                break
        return last_index

    def get_seconds_playing(self):
        seconds = int(self.read()["player"]["time"])
        return seconds

    def get_money(self):
        return int(self.read()['player']['money'])

    def set_money(self, money: int):
        content = self.read()
        content["player"]["money"] += money
        self.write(content=content)
