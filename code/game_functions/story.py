from code import UsefullyMethods


class StoryTools:
    def __init__(self, cli_mode=False):
        self.cli_mode = cli_mode
        self.local_switches = {
            "A": None,
            "B": None,
            "C": None,
            "D": None
        }

    @staticmethod
    def text(text_content: str):
        return f"Système: {text_content}"

    def choices(self, variable_label: str, answer: str, **kwargs):
        UsefullyMethods(
            cli_mode=self.cli_mode
        ).run(
            return_value=kwargs
        )
        value = UsefullyMethods(
            cli_mode=self.cli_mode
        ).input("Contenu")
        UsefullyMethods().set_variables(
            variable_label=variable_label,
            variable_value=answer == value
        )

    def set_local_switch(self, switch_label: str, boolean: bool):
        self.local_switches[switch_label] = boolean
