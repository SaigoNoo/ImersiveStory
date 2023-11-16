from code import File


class System(File):
    """
    System is a class related to different system features,
    like "checking update version of IS", and much more...
    """

    def language(self) -> None:
        """
        This method will set the language of the game.
        :return: None
        """
        self.lang = str(self.read()['LANG']).lower()


class Scenario(File):
    """
    Scenario is a class related to scenario's files.
    With it, the user will see text, interact by using inputs, ...
    """

    def play_scenario(self) -> any:
        for line in self.read():
            if not self.ignore(line=line):
                print(self.instruction(line=line))

    @staticmethod
    def instruction(line: str) -> str:
        return str(line).split('::')[1]

    @staticmethod
    def ignore(line: str) -> bool:
        ignore = [
            '',
            'E_VARIABLE',
            'E_CHOIX',
            'E_SI'
        ]
        return line in ignore

    def text(self, line: str) -> str:
        """
        :param line:
        :return: str
        """
        return line
