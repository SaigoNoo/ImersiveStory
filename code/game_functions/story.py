from code import UsefullyMethods


class StoryTools:
    def __init__(self, cli_mode=False):
        self.cli_mode = cli_mode

    @staticmethod
    def text(text_content: str):
        return text_content

    def choices(self, variable_name: str, answer: str, **kwargs):
        for [key, value] in kwargs.items():
            print(f"{key}) {value}")
        value = UsefullyMethods(
            cli_mode=self.cli_mode
        ).input("Contenu")
        UsefullyMethods().set_variables(
            variable_name=variable_name,
            variable_value=answer == value
        )
