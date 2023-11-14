from json import load, dumps


class Scenario:
    def __init__(self, fichier: str):
        self.scenario_fichier = fichier
        self.bad_syntaxe(
            search=True
        )

    def bad_syntaxe(self, search=True, index=None, line=None):
        if search:
            with open(self.scenario_fichier, 'r', encoding='utf8') as scenario:
                list_scenario = scenario.readlines()
                for [index, line] in enumerate(list_scenario):
                    if line.strip().__contains__('::'):
                        if self.instruction(line_str=line) not in [
                            'VARIABLES',
                            'VARIABLES_FIN',
                            'TEXTE',
                            'SAUT',
                            'ENTREE',
                            'CHOIX',
                            'CHOIX_FIN',
                            'SI',
                            'SINON_SI',
                            'SI_FIN'
                        ]:
                            raise ValueError(
                                f"Ligne {index + 1}: {line.strip()} n'est pas une instruction valide !\n"
                                f"Vérifiez que vous n'ayez pas mis d'espaces entre les ::")
        else:
            raise ValueError(
                f"Ligne {index + 1}: {line.strip()} n'est pas une instruction valide !\n"
                f"Vérifiez que vous n'ayez pas mis d'espaces entre les ::")

    def lire_scenario(self) -> None:
        with open(self.scenario_fichier, 'r', encoding='utf8') as scenario:
            list_scenario = scenario.readlines()
            for [index, line] in enumerate(list_scenario):
                if line != '':
                    if '::' == line[:2]:
                        if self.instruction(line_str=line) == 'VARIABLES':
                            self.variables(
                                index=index,
                                scenario_list=list_scenario
                            )
                        elif self.instruction(line_str=line) == 'TEXTE':
                            self.texte(
                                scenario_list=list_scenario,
                                index=index
                            )
                        elif self.instruction(line_str=line) == 'ENTREE':
                            self.entree(
                                scenario_list=list_scenario,
                                index=index
                            )
                        elif self.instruction(line_str=line) == 'SAUT':
                            print("")
                        elif self.instruction(line_str=line) == 'CHOIX':
                            self.choix(
                                scenario_list=list_scenario,
                                index=index
                            )
                        elif self.instruction(line_str=line) == 'SI':
                            self.conditions(
                                scenario_list=list_scenario,
                                index=index
                            )
                        elif self.instruction(line_str=line) in [
                            'VARIABLES_FIN',
                            'CHOIX_FIN',
                            'SINON_SI',
                            'SI_FIN'
                        ]:
                            pass
                        else:
                            self.bad_syntaxe(
                                search=False,
                                index=index,
                                line=line
                            )

    def instruction(self, line_str: str) -> str:
        return line_str.split('::')[1]

    def conditions(self, scenario_list: list, index: int) -> str:
        inc = 0
        # Boucle jusqu'a atteindre ::SI_FIN::
        while str(scenario_list[index + inc]).strip() != "::SI_FIN::":
            if str(scenario_list[index + inc].strip()).__contains__('SI'):
                condition = scenario_list[index + inc].split('::')[1].strip()
                condition_param = scenario_list[index + inc].split('::')[2:][0].strip()

                # Parser les conditions logiques OU et ET

                if 'OU' in condition_param and 'ET' in condition_param:
                    temp = []
                    conditions = condition_param.split(' OU ')
                    for cond in conditions:
                        temp.append(cond.split(' ET '))

                elif 'OU' in condition_param and 'ET' not in condition_param:
                    conditions = condition_param.split(' OU ')

                else:
                    conditions = condition_param.split(' ET ')

                for cond in conditions:
                    print(cond)

            inc = inc + 1

    def operation(self, operateur: str, **kwargs) -> bool:
        if operateur == "EST":
            return kwargs['var'] == kwargs['hard']
        elif operateur == "EST PAS":
            return kwargs['var'] != kwargs['hard']

    def entree(self, scenario_list: list, index: int) -> None:
        variable_name = str(scenario_list[index]).split(' > ')[1].strip()
        text = str(scenario_list[index + 1]).strip()
        self.definir_variable(
            variable_name=variable_name,
            variable_value=input(f'{text} ')
        )

    def texte(self, scenario_list: list, index: int) -> None:
        line = str(scenario_list[index + 1]).strip()
        line = line.split()
        for [index, word] in enumerate(line):
            if word[0] == '$':
                line[index] = self.lire_variables(word[1:])
        print(' '.join(line))

    def choix(self, scenario_list: list, index: int) -> None:
        choice_to_stock = []
        inc = 1
        while str(scenario_list[index + inc]).strip() != "::CHOIX_FIN::":
            choice_to_stock.append(str(scenario_list[index + inc]).strip())
            inc = inc + 1
        for line in choice_to_stock:
            print(f'{line.split(" = ")[0]}) {line.split(" = ")[1]}')

    def variables(self, index: int, scenario_list: list) -> None:
        var_to_stock = []
        inc = 1
        while str(scenario_list[index + inc]).strip() != "::VARIABLES_FIN::":
            var_to_stock.append(str(scenario_list[index + inc]).strip())
            inc = inc + 1

        with open('variables.json', 'r') as v_read:
            v_read = load(v_read)

        for varline in var_to_stock:
            v_read[varline.split('=')[0]] = varline.split("=")[1]

        with open('variables.json', 'w') as v_write:
            v_write.write(dumps(v_read))

    def definir_variable(self, variable_name: str, variable_value: str) -> None:
        var = self.lire_variables()
        var[variable_name] = variable_value
        with open('variables.json', 'w') as vwrite:
            vwrite.write(dumps(var))

    def lire_variables(self, key=None) -> str or int:
        with open('variables.json', 'r') as vread:
            return load(vread) if key is None else load(vread)[key]


scenario = Scenario(
    fichier='scenario.txt'
)
scenario.lire_scenario()
