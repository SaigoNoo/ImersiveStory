from code import Variables


class Scenario:
    """
    Scenario is a class related to scenario's files.
    With it, the user will see text, interact by using inputs, ...
    """

    def __init__(self, file: str | bytes):
        self.file = file
        self.scenario = None

    def play_scenario(self) -> any:
        self.scenario = Variables(file=self.file).read()
        for [index, line] in enumerate(self.scenario):
            if not self.ignore(line=line) and self.is_instruction(line=line):
                if self.instruction(line=line) == "TEXTE":
                    print(self.text(index=index))
                elif self.instruction(line=line) == "VARIABLE":
                    self.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction(line=line)
                    )

    def do_list_parameters(self, index_start: int, instruction_type: str) -> None:
        index = index_start
        table = []
        while self.scenario[index] != f":: E_{instruction_type} ::":
            table.append(self.scenario[index])
            index = index + 1
        table.remove(f":: {instruction_type} ::")
        self.saves_variables(list_var=table)

    @staticmethod
    def saves_variables(list_var: list) -> None:
        variables = Variables(file='variables.json')
        for item in list_var:
            variables.save(
                key=item.split('=')[0].strip(),
                value=item.split("=")[1].strip()
            )

    @staticmethod
    def instruction(line: str) -> str:
        return line.split('::')[1].strip()

    @staticmethod
    def is_instruction(line: str) -> bool:
        return '::' in line

    @staticmethod
    def ignore(line: str) -> bool:
        ignore = [
            '',
            'E_VARIABLE',
            'E_CHOIX',
            'E_SI'
        ]
        return line in ignore

    def text(self, index: int) -> str:
        """
        :param index:
        :return: str
        """
        return self.set_variables(line=self.scenario[index + 1])

    def set_variables(self, line: str) -> str:
        signs_to_ignore = [
            ":",
            ".",
            ";",
            ",",
            "$"
        ]
        temp_line = line.split()
        for [index, word] in enumerate(temp_line):
            if word[0] == "$" and word[-1] in signs_to_ignore:
                temp_line[index] = f"{Variables(file='variables.json').get(temp_line[index][1:-1])}{word[-1]}"
            elif word[0] == "$" and word[-1] not in signs_to_ignore:
                temp_line[index] = f"{Variables(file='variables.json').get(temp_line[index][1:])}"
        return ' '.join(temp_line)
