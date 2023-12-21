from code.game.texte import Texte
from os import system
from platform import system as os
<<<<<<< HEAD
from getpass import getpass
=======
>>>>>>> main


class Instruction:
    def __init__(self, scenario: dict):
        self.scenario = scenario

    @staticmethod
    def instruction(line: str) -> str:
        """
        Affiche l'instruction sans les délimiteurs
        """
        return line.split('::')[1].strip()

    @staticmethod
    def is_instruction(line: str) -> bool:
        """
        vérifie si la ligne donné est une instruction
        """
        return '::' in line

    @staticmethod
    def ignore(line: str) -> bool:
        """
        Renvoie un boolean si line est dans [ignore]
        Sert lors de la lecture du play_scenario pour ne pas lire les END_<instruction>
        """
        ignore = [
            '',
            'E_VARIABLE',
            'E_SI'
        ]
        return line in ignore

    def do_list_parameters(self, index_start: int, instruction_type: str) -> list:
        """
        lorsque l'on a des instrctions de bloc, on va stocker tout les paramètres entre <option> E_<option>
        dans une liste.
        """
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

    def run_range_lines(self, start_line: int, end_line: int) -> bool:
<<<<<<< HEAD
        need_enter = False
=======
        """
        """
>>>>>>> main
        for line in range(start_line + 1, end_line):
            if not self.ignore(line=self.scenario[line]) and self.is_instruction(line=self.scenario[line]):
                if self.instruction(line=self.scenario[line]) == "TEXTE":
                    Texte(scenario=self.scenario).texte(index_start=line)
<<<<<<< HEAD
                    need_enter = True
                if need_enter:
                    getpass("\nAppuyez sur Enter pour continuer...")
                self.clear()
        return True
=======
                    return True
>>>>>>> main

    @staticmethod
    def clear():
        return system("clear") if os() in ["Linux", "Darwin"] else system("cls")
