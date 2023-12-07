from code.variables import Variables


class PlayerInput:
    def __init__(self, scenario: dict):
        self.scenario = scenario

    def input_player(self, index_start: int) -> None:
        """
        Prompt utilisateur

        __info__:
        - var_name: nom de variable qui sera associé à une valeur (clé)
        """
        line = self.scenario[index_start + 1]
        var_name = self.scenario[index_start].split("::")[2].split(">")[1].strip()
        if line[-1] != " ":
            line += " "
        inp = input(f"{line}")
        Variables(file='variables.json').save(
            key=var_name,
            value=inp
        )
