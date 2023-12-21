from rich.console import Console
from rich.panel import Panel
from code.game.variables import GameVariables
from rich.table import Table
from datetime import timedelta
from code.game.player import Player
from time import time
from code.files import File

# Objects Init #
gv = GameVariables()


# ------------ #


class Texte:
    def __init__(self, scenario=None):
        self.scenario = scenario

    def texte(self, index_start: int) -> None:
        """
        print juste un texte avec une peu de syntaxe rich
        """
        output = gv.set_variables(line=self.scenario[index_start + 1], color=True)
        if ":" in output:
            npc = output.split(':')[0].strip()
            text = ":".join(output.split(":")[1::]).strip()
        else:
            npc = None
            text = output.strip()
        panel_1 = Panel.fit(f"{text}", title=npc, width=60)
        Console(record=True).print(panel_1)

    def stats(self) -> None:
        """
        print juste un texte avec une peu de syntaxe rich
        """
        table = Table(title="Statistiques de votre partie", width=45)
        player = Player(file="save.json")
        temp = File(file="temp.json")

        table.add_column("Durée de jeu", style="cyan")
        table.add_column("Position", style="red")
        table.add_column("Niveau", style="magenta")
        table.add_column("Argent", style="yellow")

        table.add_row(
            str(timedelta(seconds=(int(player.get_seconds_playing()) + int(round(time()) - temp.read()['time'])))),
            "Markarth",
            str(player.get_level()),
            f"{player.get_money()}$"
        )

        console = Console()
        console.print(table)