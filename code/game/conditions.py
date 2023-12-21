from code.game.instructions import Instruction
from code.game.variables import GameVariables


class Si(Instruction):
    def si(self, index_start: int, scenario: dict) -> list or None:
        """
        si est une méthode qui va renvoyer un None ou une liste des des index de lignes qui se trouvent au sein
        d'un bloc de condition vraie.
        Exemple: [4, 9]
        Les lignes 4 à 9 devront être interprétées !

        __infos__:
        - index: index de scenario par lequel commencer l'itération
        - condition_lines: contient une liste de toutes le conditions du SI (TOUTES) + index de la condition, le tout
        dans une liste
        - end: boolean qui vaudra True si on est arrivé à la fin du SI [ref: :: E_SI ::]
        - response: contiendra l'index du début de bloc de la condition vraie jusqu'a l'index de fin de bloc
        """
        condition_split = None
        index = index_start
        conditions_lines = []
        response = []
        end = False
        while "E_SI" not in scenario[index]:
            if (self.is_instruction(line=scenario[index]) and self.instruction(line=scenario[index])
                    in ["SI", "SINON_SI", "SINON"]):
                conditions_lines.append([index, scenario[index]])
            index = index + 1
        conditions_lines.append([index, str(scenario[index]).strip()])
        for [line, condition] in conditions_lines:
            if end:
                response.append(line)
                response.append(conditions_lines[-1][0])
                return response
            if self.instruction(line=condition) != "E_SI" and self.is_instruction(line=condition):
                """
                Permet de ne garder que la condition après avoir convertit les variables en string et en ayant enlevé
                les instructions...
                """
                condition_split = GameVariables().set_variables(line=condition).split("::")[-1].strip()
            if self.operateur(conditions=condition_split.split()) and self.instruction(line=condition) != "E_SI":
                response.append(line)
                end = True
        return None

    @staticmethod
    def operateur(conditions: list) -> bool:
        """
        Opération logique en utilisant la comparaison de string
        """
        if "+EST+" in conditions:
            index = conditions.index("+EST+")
            return " ".join(conditions[0:index]) == " ".join(conditions[(index + 1):])
        elif "-EST-" in conditions:
            index = conditions.index("-EST-")
            return " ".join(conditions[0:index]) != " ".join(conditions[(index + 1):])
