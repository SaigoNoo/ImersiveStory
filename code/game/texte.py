from rich.console import Console
from rich.panel import Panel
from code.game.variables import GameVariables

# Objects Init #
gv = GameVariables()


# ------------ #


class Texte:
    def __init__(self, scenario: dict):
        self.scenario = scenario

    def texte(self, index_start: int) -> None:
        """
        print juste un texte avec une peu de syntaxe rich
        """
        output = gv.set_variables(line=self.scenario[index_start + 1], color=True)
        npc = output.split(':')[0]
        text = ":".join(output.split(":")[1::])
        panel_1 = Panel.fit(f"{text.strip()}", title=f"{npc.strip()}", width=60)
        Console(record=True).print(panel_1)
