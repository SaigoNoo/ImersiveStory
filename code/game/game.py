from os import system
from code import Variables, File
from rich import print
from getpass import getpass
import curses


class Scenario:
    """
    Scenario is a class related to scenario's files.
    With it, the user will see text, interact by using inputs, ...
    """

    def __init__(self, file: str | bytes):
        self.file = file
        self.scenario = None
        self.si_result = None
        self.current_index = 0

    def play_scenario(self) -> any:
        self.clear()
        self.scenario = Variables(file=self.file).read()
        for [index, line] in enumerate(self.scenario):
            need_enter = False
            if not self.ignore(line=line) and self.is_instruction(line=line):

                # Si TEXTE
                if self.instruction(line=line) == "TEXTE":
                    print(self.texte(index_start=index))
                    need_enter = True

                # Si VARIABLES
                elif self.instruction(line=line) == "VARIABLE":
                    table = self.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction(line=line)
                    )
                    self.saves_variables(list_var=table)

                # Si SAUT DE LIGNE
                elif self.instruction(line=line) == "SAUT":
                    print("")

                # Si ENTREE TEXTE
                elif self.instruction(line=line) == "ENTREE":
                    self.input_player(
                        index_start=index
                    )

                # Si CHOIX
                elif self.instruction(line=line) == "CHOIX":
                    table = self.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction(line=line)
                    )
                    string = table[-1]
                    variable = line.split('>')[-1].strip()
                    del table[-1]
                    curses.wrapper(self.run, table, string, variable)

                # Si SI
                elif self.instruction(line=line) == "SI":
                    print(self.si(index_start=index))
                    need_enter = True

            if need_enter:
                getpass("\nAppuyez sur Enter pour continuer...")
            self.clear()

    def si(self, index_start: int) -> int or None:
        index = index_start
        while "E_SI" not in self.scenario[index]:
            if self.is_instruction(line=self.scenario[index]):
                if self.instruction(line=self.scenario[index]) in ["SI", "SINON_SI", "SINON"]:
                    cond = self.scenario[index].split("::")[-1].strip()
                    cond = self.set_variables(line=cond).split()
                    if self.operateur(conditions=cond):
                        return index
            index = index + 1
        return None

    def operateur(self, conditions: list) -> bool:
        if conditions[1].strip() == "EST":
            return conditions[0] == conditions[2]
        elif conditions[1].strip() == "EST_PAS":
            return conditions[0] != conditions[2]

    def input_player(self, index_start: int) -> None:
        variable = Variables(file="variables.json")
        line = self.scenario[index_start + 1]
        if line[-1] == ":":
            line += " "
        inp = input(line)
        var_name = self.scenario[index_start].split("::")[2].split(">")[1].strip()
        variable.save(
            key=var_name,
            value=inp
        )

    def do_list_parameters(self, index_start: int, instruction_type: str) -> list:
        index = index_start
        table = []

        # Si c'est un choix
        if instruction_type == 'CHOIX':
            while f"E_{instruction_type}" not in self.scenario[index]:
                table.append(self.scenario[index])
                index = index + 1
            index_keep = None
            table.append(self.scenario[index].split("::")[-1].strip())
            for [index2, line] in enumerate(table):
                if f":: {instruction_type} ::" in line:
                    index_keep = index2
            if index_keep is not None:
                del table[index_keep]

        # Si c'est des variables
        elif instruction_type == 'VARIABLE':
            while f"E_{instruction_type}" not in self.scenario[index]:
                table.append(self.scenario[index])
                index = index + 1
            table.remove(f":: {instruction_type} ::")
        return table

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
            'E_SI'
        ]
        return line in ignore

    def texte(self, index_start: int) -> str:
        """
        :param index:
        :return: str
        """
        output = self.set_variables(line=self.scenario[index_start + 1], color=True)
        return output

    @staticmethod
    def set_variables(line: str, color=False) -> str:
        var_color = File(file='config.ini').read()['COLOR_VAR']
        temp_line = line.split()
        for [index, word] in enumerate(temp_line):
            if '|' in word:
                replace = word.split('|')
                word = Variables(file='variables.json').get(key=replace[1])
                if color:
                    replace[1] = f"[bold {var_color}]{word}[/bold {var_color}]"
                else:
                    replace[1] = f"{word}"
                temp_line[index] = ''.join(replace)
        return ' '.join(temp_line)

    @staticmethod
    def clear():
        return system("clear")

    def display_options(self, options: list, texte: str, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, f"{texte}")
        for i, option in enumerate(options):
            prefix = "[*] " if i == self.current_index else "[ ] "
            stdscr.addstr(i + 1, 0, f"{prefix}{option}")

        stdscr.refresh()

    def decrement_index(self, options):
        self.current_index = (self.current_index - 1) % len(options)

    def increment_index(self, options):
        self.current_index = (self.current_index + 1) % len(options)

    def run(self, stdscr, options: list, texte: str, variable_key: str):
        curses.curs_set(0)  # Hide the cursor

        while True:
            self.display_options(
                options=options,
                texte=f"{texte}",
                stdscr=stdscr
            )

            key = stdscr.getch()

            if key == curses.KEY_UP:
                self.decrement_index(options)
            elif key == curses.KEY_DOWN:
                self.increment_index(options)
            elif key == 10:  # 10 c'est le code ASCII de la touche ENTER
                selected_option = options[self.current_index]
                Variables(file="variables.json").save(
                    key=variable_key,
                    value=selected_option
                )
                break
