from getpass import getpass
import curses
from code.game.texte import Texte
from code.game.instructions import Instruction
from code.variables import Variables
from code.game.conditions import Si
from code.game.variables import GameVariables
from code.game.inputs import PlayerInput
from code.game.choices import Choices
from code.game.saves import Sauvegardes
from code.game.free_control import FreeControl
from code.game.player import Player


class Main:
    """
    Main est la classe principale qui sera appellée afin d'itérer ligne par ligne le scénario.
    Avec ceci, l'utilisateur pourra effectuer des actions, des choix, ...
    """

    def __init__(self, file: str | bytes):
        # Variables d'instances
        self.file = file
        self.scenario = None
        self.si_result = None

        # Initialisation des objets
        self.instruction = None
        self.si = None
        self.player_input = None
        self.txt = None

    def initialize_objects(self):
        """
        Permet d'initialiser les objets dans les variables d'instances.
        On ne peut le faire dans le __init__ car les paramètres d'objets ne sont
        pas encore déclarés avant d'avoir avancé dans le play_scenario [cause: self.scenario]
        """
        self.txt = Texte(scenario=self.scenario)
        self.instruction = Instruction(scenario=self.scenario)
        self.si = Si(scenario=self.scenario)
        self.player_input = PlayerInput(scenario=self.scenario)

    def play_scenario(self, no_save=False) -> any:
        """
        En de termes simples:
        1. On mémorise une liste qui contient les instructions et données
        2. On boucle dans la liste ligne par ligne
        3. Si on lit une instruction, on fait appel à l'objet responsable de l'action

        __info__:
        - skip: boolean qui permettra lors d'un SI de sauter les lignes dont la condition est fausse
        - line_to_reach: liste qui contiendra (POUR UN SI) les index des blocs a lire d'une condition vrai
        - self.scenario: dictionnaire des lignes scénario
        - need_enter: boolean qui, si vrai, obligera l'utilisateur a presser ENTER pour poursuivre...
        - self.instruction.clear(): nettoie l'écran pour afficher un écran blank
        """
        # Variables utiles pour la boucle
        skip = False
        line_to_reach = None
        self.scenario = Variables(file=self.file).read()
        self.initialize_objects()
        self.instruction.clear()

        for [index, line] in enumerate(self.scenario):
            need_enter = False
            if not self.instruction.ignore(line=line) and self.instruction.is_instruction(line=line):

                # Si TEXTE
                if self.instruction.instruction(line=line) == "TEXTE" and not skip:
                    self.txt.texte(index_start=index)
                    need_enter = True

                # Si VARIABLES
                elif self.instruction.instruction(line=line) == "VARIABLE" and not skip:
                    table = self.instruction.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction.instruction(line=line)
                    )
                    GameVariables().saves_variables(list_var=table)

                # Si SAUT DE LIGNE
                elif self.instruction.instruction(line=line) == "SAUT" and not skip:
                    print("")

                # Si ENTREE TEXTE
                elif self.instruction.instruction(line=line) == "ENTREE" and not skip:
                    self.player_input.input_player(
                        index_start=index
                    )

                # Si CHOIX
                elif self.instruction.instruction(line=line) == "CHOIX" and not skip:
                    table = self.instruction.do_list_parameters(
                        index_start=index,
                        instruction_type=self.instruction.instruction(line=line)
                    )
                    string = table[-1]
                    variable = line.split('>')[-1].strip()
                    del table[-1]
                    curses.wrapper(Choices().run, table, string, variable)

                # Si SI
                elif self.instruction.instruction(line=line) == "SI" and not skip:
                    si = self.si.si(index_start=index, scenario=self.scenario)
                    line_to_reach = si[2]
                    self.instruction.run_range_lines(start_line=si[0], end_line=si[1])
                    need_enter = False
                    skip = True

                elif self.instruction.instruction(line=line) == "ARGENT" and not skip:
                    joueur = Player(file="save.json")
                    joueur.set_money(money=int(self.scenario[index + 1]))

                    # Si JOUEUR_CONTROLE
                elif self.instruction.instruction(line=line) == "JOUEUR_CONTROLE" and not skip:
                    FreeControl().run_mode()


                # Skip to line
                elif skip:
                    if line_to_reach == index:
                        skip = False
            else:
                if line_to_reach == index:
                    skip = False

            if need_enter:
                getpass("\nAppuyez sur Enter pour continuer...")
            self.instruction.clear()
        if not no_save:
            Sauvegardes(file="save.json").sauvegarder()
