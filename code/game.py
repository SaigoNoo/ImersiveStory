from code import Variables, File
from rich import print


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
                # Si TEXTE
                if self.instruction(line=line) == "TEXTE":
                    print(self.text(index=index))
                # Si VARIABLES
                elif self.instruction(line=line) == "VARIABLE":
                    self.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction(line=line)
                    )
                # Si SAUT DE LIGNE
                elif self.instruction(line=line) == "SAUT":
                    print("")
                # Si ENTREE TEXTE
                elif self.instruction(line=line) == "ENTREE":
                    pass

    def input_player(self, index_start: int, line: str) -> None:
        input(self.scenario[index_start + 1])

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

    @staticmethod
    def set_variables(line: str) -> str:
        var_color = File(file='config.ini').read()['COLOR_VAR']
        temp_line = line.split()
        for [index, word] in enumerate(temp_line):
            if '|' in word:
                replace = word.split('|')
                word = Variables(file='variables.json').get(key=replace[1])
                replace[1] = f"[bold {var_color}]{word}[/bold {var_color}]"
                temp_line[index] = ''.join(replace)
        return ' '.join(temp_line)
